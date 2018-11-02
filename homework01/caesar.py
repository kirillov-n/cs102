def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    shift = 3
    ciphertext = ''

    for alph in plaintext:
        if  alph >= 'a' and alph <= 'z' or alph >= 'A' and alph <= 'Z':
            code = ord(alph) + shift

    for alph in plaintext:
        if  alph >= 'a' and alph <= 'z' or alph >= 'A' and alph <= 'Z':
            code = ord(abcd) + shift

            if code > ord('Z') and code < ord('a') or code > ord('z'):
                code -= 26
            ciphertext += chr(code)
        else:

            ciphertext += alph

    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    shift = 3 
    plaintext = ''

    for alph in ciphertext:
        if alph >= 'a' and alph <= 'z' or alph >= 'A' and alph <= 'Z':
           code = ord(alph) - shift

    for alph in ciphertext:
        if alph >= 'a' and alph <= 'z' or alph >= 'A' and alph <= 'Z':
           code = ord(alph) - shift

           if code < ord('a') and code > ord('Z') or code < ord('A'):
                code += 26
           plaintext += chr(code)
        else:

            plaintext += alph

    return plaintext
