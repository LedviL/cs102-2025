def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for c in plaintext:
        if not c.isalpha():
            ciphertext += c
            continue
        if (
            (ord("A") <= ord(c) + shift <= ord("Z") and ord("A") <= ord(c) <= ord("Z"))
            or (ord("a") <= ord(c) + shift <= ord("z"))
            and ord("a") <= ord(c) <= ord("z")
        ):
            ciphertext += chr(ord(c) + shift)
        elif c == c.upper():
            ciphertext += chr(ord("A") + (ord(c) + shift) % ord("Z") - 1)
        else:
            ciphertext += chr(ord("a") + (ord(c) + shift) % ord("z") - 1)

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for c in ciphertext:
        if not c.isalpha():
            plaintext += c
            continue
        if (
            (ord("A") <= ord(c) - shift <= ord("Z") and ord("A") <= ord(c) <= ord("Z"))
            or (ord("a") <= ord(c) - shift <= ord("z"))
            and ord("a") <= ord(c) <= ord("z")
        ):
            plaintext += chr(ord(c) - shift)
        elif c == c.upper():
            plaintext += chr(ord(c) + (ord("Z") - shift - ord("A") + 1) % 26)
        else:
            plaintext += chr(ord(c) + (ord("z") - shift - ord("a") + 1) % 26)

    return plaintext
