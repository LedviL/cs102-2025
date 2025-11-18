def decrypt_scytale(plaintext, n):
    """decrypts scytale cypher"""
    text_size = len(plaintext)
    decrypted_text = ""
    for start in range(n):
        for i in range(start, text_size, n):
            decrypted_text += plaintext[i]
    return decrypted_text
