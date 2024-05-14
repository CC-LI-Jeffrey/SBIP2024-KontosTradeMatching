import time
import enumer
import dp
import Greedy

td = 0
te = 0
tg = 0
x_ = 0
y_ = 0
w_ = 0
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
    x = dp.find_min_cost(mt, n, c, z1, z2, v)
    t2 = time.time()
    x_ += x
    t3 = time.time()
    y = enumer.find_min_cost(mt, n, c, z1, z2, v)
    t4 = time.time()
    y_ += y
    t5 = time.time()
    w = Greedy.findmin(mt, n, c, z1, z2, v)
    t6 = time.time()
    w_ += w
    td += t2 - t1
    te += t4 - t3
    tg += t6 - t5
    f.readline()
print(str(td / 370) + "  " + str(x_ / 370) + "\n")
print(str(te / 370) + "  " + str(y_ / 370) + "\n")
print(str(tg / 370) + "  " + str(w_ / 370) + "\n")
f.close()

td = 0
te = 0
tg = 0
x_ = 0
y_ = 0
w_ = 0
f = open('data3.txt')
for i in range(100):
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
        line = f.readline()
        c[j], z1[j], z2[j] = map(int, line.split())
        for p in range(c[j]):
            v[j].append(int(f.readline()))
    t1 = time.time()
    x = dp.find_min_cost(mt, n, c, z1, z2, v)
    t2 = time.time()
    x_ += x
    t3 = time.time()
    y = enumer.find_min_cost(mt, n, c, z1, z2, v)
    t4 = time.time()
    y_ += y
    t5 = time.time()
    w = Greedy.findmin(mt, n, c, z1, z2, v)
    t6 = time.time()
    w_ += w
    td += t2 - t1
    te += t4 - t3
    tg += t6 - t5
    f.readline()
print(str(td / 100) + "  " + str(x_ / 100) + "\n")
print(str(te / 100) + "  " + str(y_ / 100) + "\n")
print(str(tg / 100) + "  " + str(w_ / 100) + "\n")
f.close()
