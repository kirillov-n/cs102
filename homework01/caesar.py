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
    ciphertext = ''
    for abcd in plaintext:
        if  abcd >= 'a' and abcd <= 'z' or abcd >= 'A' and abcd <= 'Z':
            code = ord(abcd) + 3
            if code > ord('Z') and code < ord('a') or code > ord('z'):
                code -= 26
            ciphertext += chr(code)
        else:
            ciphertext += abcd
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
    plaintext = ''
    for abcd in ciphertext:
        if abcd >= 'a' and abcd <= 'z' or abcd >= 'A' and abcd <= 'Z':
           code = ord(abcd) - 3
           if code < ord('a') and code > ord('Z') or code < ord('A'):
                code += 26
           plaintext += chr(code)
        else:
            plaintext += abcd
    return plaintext