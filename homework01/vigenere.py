def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    import caesar

    keyword_char_index = 0
    for i, char in enumerate(plaintext):
        if not char.isalpha():
            ciphertext += char
            keyword_char_index = (keyword_char_index + 1) % len(keyword)
            continue
        key = keyword[keyword_char_index]
        if char.isupper() and key.islower():
            key = key.upper()
        elif char.islower() and key.isupper():
            key = key.lower()
        shift = ord(key) - ord("A" if char.isupper() else "a")
        ciphertext += caesar.encrypt_caesar(char, shift)
        keyword_char_index = (keyword_char_index + 1) % len(keyword)

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    import caesar

    keyword_char_index = 0
    for i, char in enumerate(ciphertext):
        if not char.isalpha():
            plaintext += char
            keyword_char_index = (keyword_char_index + 1) % len(keyword)
            continue
        key = keyword[keyword_char_index]
        if char.isupper() and key.islower():
            key = key.upper()
        elif char.islower() and key.isupper():
            key = key.lower()
        shift = ord(key) - ord("A" if char.isupper() else "a")
        plaintext += caesar.decrypt_caesar(char, shift)
        keyword_char_index = (keyword_char_index + 1) % len(keyword)
    return plaintext
