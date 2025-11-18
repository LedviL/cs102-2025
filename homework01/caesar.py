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
    a_code = ord("a")
    z_code = ord("z")
    A_code = ord("A")
    Z_code = ord("Z")
    for c in plaintext:
        if not c.isalpha():
            ciphertext += c
            continue
        if (
            (A_code <= ord(c) + shift <= Z_code and A_code <= ord(c) <= Z_code)
            or (a_code <= ord(c) + shift <= z_code)
            and a_code <= ord(c) <= z_code
        ):
            ciphertext += chr(ord(c) + shift)
        elif c == c.upper():
            ciphertext += chr(A_code + (ord(c) + shift) % Z_code - 1)
        else:
            ciphertext += chr(a_code + (ord(c) + shift) % z_code - 1)

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
    a_code = ord("a")
    z_code = ord("z")
    A_code = ord("A")
    Z_code = ord("Z")
    for char in ciphertext:
        if not char.isalpha():
            plaintext += char
            continue
        if (
            (A_code <= ord(char) - shift <= Z_code and A_code <= ord(char) <= Z_code)
            or (a_code <= ord(char) - shift <= z_code)
            and a_code <= ord(char) <= z_code
        ):
            plaintext += chr(ord(char) - shift)
        elif char.isupper():
            plaintext += chr(ord(char) + (Z_code - shift - A_code + 1) % 26)
        else:
            plaintext += chr(ord(char) + (z_code - shift - a_code + 1) % 26)

    return plaintext
