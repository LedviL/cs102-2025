def decrypt_scytale(plaintext, n):
    rows, cols = n, len(plaintext) // n
    matrix = [[""]*cols for _ in range(rows)]
    c = -1
    for i in range(len(plaintext)):
        if i % rows == 0:
            c += 1
        matrix[i % rows][c] = plaintext[i]
    return "".join(["".join(s) for s in matrix])
