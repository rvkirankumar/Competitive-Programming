def nonzero(a, y, x):
    return 1 if a[y][x]=='.' else 0

w = 6
h = 5
a = ['......', '. .  .', '...  .', '. ....', '......']
r = [[0]*w for i in range(h)]
c = [[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        val = nonzero(a, i, j)
        if i==0:
            c[i][j] = val
        else:
            c[i][j] = c[i-1][j]  + val
        if j==0:
            r[i][j] = val
        else:
            r[i][j] = r[i][j-1] + val
count = 0
for i in range(h - 1):
    for j in range(w - 1):
        if nonzero(a, i, j):
            for k in range(1, min(h-i, w-j)):
                if nonzero(a, i+k, j+k):
                    if r[i][j+k] - r[i][j] != k :
                        break      #there are holes in this row between i and i+k
                    if c[i+k][j] - c[i][j] != k:
                        break
                    if r[i+k][j+k] - r[i+k][j] != k:
                        break
                    if c[i+k][j+k] - c[i][j+k] != k:
                        break
                    count += 1
                    print(i, j, k)
print(count)