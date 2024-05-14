def dwriter(z1, z2, v, c, mt, n, s, t):
    f = open(s, 'a')
    f.write(str(mt) + "\n")
    f.write(str(n) + "\n")
    for i in range(n):
        f.write(str(c[i]) + " " + str(z1[i]) + " " + str(z2[i]) + "\n")
        for j in range(c[i]):
            f.write(str(v[i][j]) + " ")
        f.write("\n")
    f.write(str(t) + "\n")
    f.close()

