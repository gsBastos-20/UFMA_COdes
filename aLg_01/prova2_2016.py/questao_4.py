def encontrarUfma(m):
    count_ufma = 0
    for i in range(len(m[0])):
        for j in range(len(m)):
            if m[i][j] == "UFMA":
                count_ufma += 1
                break
            return count_ufma