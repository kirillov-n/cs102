<<<<<<< HEAD
def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    for index, alph in enumerate(plaintext):
        if 'a' <= alph and alph <= 'z' or 'A' <= alph and alph <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= alph <= 'z' else ord('A')
            code = ord(alph) + shift
            if 'a' <= alph and alph <= 'z' and code > ord('z'):
                code -= 26
            elif 'A' <= alph and alph <= 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:
            chiphertext += alph
    return ciphertext
    


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    for index, alph in enumerate(ciphertext):
        if 'a' <= alph and alph <= 'z' or 'A' <= alph and alph <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= alph <= 'z' else ord('A')
            code = ord(alph) - shift
            if 'a' <= alph and alph <= 'z' and code < ord('a'):
                code += 26
            elif 'A' <= alph and alph <= 'Z' and code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += alph
=======
def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    for index, alph in enumerate(plaintext):
        if 'a' <= alph and alph <= 'z' or 'A' <= alph and alph <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= alph <= 'z' else ord('A')
            code = ord(alph) + shift
            if 'a' <= alph and alph <= 'z' and code > ord('z'):
                code -= 26
            elif 'A' <= alph and alph <= 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:
            chiphertext += alph
    return ciphertext
    


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    for index, alph in enumerate(ciphertext):
        if 'a' <= alph and alph <= 'z' or 'A' <= alph and alph <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= alph <= 'z' else ord('A')
            code = ord(alph) - shift
            if 'a' <= alph and alph <= 'z' and code < ord('a'):
                code += 26
            elif 'A' <= alph and alph <= 'Z' and code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += alph
>>>>>>> e7ad8461011a7c1f6ea67f46786a598d87ac01f1
    return plaintext