def decrypt_scytale(plaintext, n):
    """decrypts scytale cypher"""
    rows, cols = n, len(plaintext) // n
    matrix = [[""] * cols for _ in range(rows)]
    c = -1
    for i, char in enumerate(plaintext):
        if i % rows == 0:
            c += 1
        matrix[i % rows][c] = char
    return "".join(["".join(s) for s in matrix])
