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

    j = 0
    for i in range(len(plaintext)):
        char = plaintext[i]
        if not char.isalpha():
            ciphertext += char
            j = (j + 1) % len(keyword)
            continue
        key = keyword[j]
        if char.isupper() and key.islower():
            key = key.upper()
        elif char.islower() and key.isupper():
            key = key.lower()
        shift = ord(key) - ord("A" if char.isupper() else "a")
        ciphertext += caesar.encrypt_caesar(char, shift)
        j = (j + 1) % len(keyword)

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

    j = 0
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if not char.isalpha():
            plaintext += char
            j = (j + 1) % len(keyword)
            continue
        key = keyword[j]
        if char.isupper() and key.islower():
            key = key.upper()
        elif char.islower() and key.isupper():
            key = key.lower()
        shift = ord(key) - ord("A" if char.isupper() else "a")
        plaintext += caesar.decrypt_caesar(char, shift)
        j = (j + 1) % len(keyword)
    return plaintext
