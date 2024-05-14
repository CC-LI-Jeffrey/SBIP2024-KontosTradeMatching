import time
import enumer
import dp
import dwriter


dest1 = 'tdata_dp.txt'
dest2 = 'tdata_enum.txt'
f = open('data.txt')
for i in range(370):
    z1 = []
    z2 = []
    c = []
    v = []
    mt = int(f.readline())
    n = int(f.readline())
    for j in range(n):
        c.append(0)
        v.append([])
        z1.append(0)
        z2.append(0)
        c[j], z1[j], z2[j] = map(int, f.readline().split())
        v[j] = list(map(int, f.readline().split()))
    t1 = time.time()
    dp.find_min_cost(mt, n, c, z1, z2, v)
    t2 = time.time()
    td = (t2-t1)*1000
    t3 = time.time()
    enumer.find_min_cost(mt, n, c, z1, z2, v)
    t4 = time.time()
    te = (t4-t3)*1000
    dwriter.dwriter(z1, z2, v, c, mt, n, dest1, td)
    dwriter.dwriter(z1, z2, v, c, mt, n, dest2, te)
    f.readline()
f.close()
