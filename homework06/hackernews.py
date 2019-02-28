from bottle import (
    route, run, template, request, redirect
)

from scraputils import get_news
from db import News, session
from bayes import NaiveBayesClassifier


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    news_id = request.query.id
    label = request.query.label
    s = session()
    qurent = s.query(News).filter(News.id == news_id).one()
    qurent.label = label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    s = session()
    latest_news = get_news("https://news.ycombinator.com/newest", n_pages=5)
    authors = [news['author'] for news in latest_news]
    titles = s.query(News.title).filter(News.author.in_(authors)).subquery()
    existing_news = s.query(News).filter(News.title.in_(titles)).all()
    for item in latest_news:
        if not existing_news or item not in existing_news:
            s.add(News(**item))
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    classifier = NaiveBayesClassifier(1)
    s = session()
    labeled_news = s.query(News).filter(News.label != None).all()
    x_train = [clean(news.title) for news in labeled_news]
    y_train = [news.label for news in labeled_news]
    classifier.fit(x_train, y_train)

    new_news = s.query(News).filter(News.label == None).all()
    for current in new_news:
        [prediction] = classifier.predict([clean(current.title)])
        if prediction == 'good':
            current.label = 'good'
        elif prediction == 'maybe':
            current.label = 'maybe'
        else:
            current.label = 'never'


def clean(s):
    translator = str.maketrans("", "", string.punctuation)
    return s.translate(translator).lower()


if __name__ == "__main__":
    run(host="localhost", port=8080)

