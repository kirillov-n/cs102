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
    for index, abcd in enumerate(plaintext):
        if 'a' <= abcd and abcd <= 'z' or 'A' <= abcd and abcd <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= abcd <= 'z' else ord('A')
            code = ord(abcd) + shift
            if 'a' <= abcd and abcd <= 'z' and code > ord('z'):
                code -= 26
            elif 'A' <= abcd and abcd <= 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:
            chiphertext += abcd
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
    for index, abcd in enumerate(ciphertext):
        if 'a' <= abcd and abcd <= 'z' or 'A' <= abcd and abcd <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= abcd <= 'z' else ord('A')
            code = ord(abcd) - shift
            if 'a' <= abcd and abcd <= 'z' and code < ord('a'):
                code += 26
            elif 'A' <= abcd and abcd <= 'Z' and code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += abcd
    return plaintext