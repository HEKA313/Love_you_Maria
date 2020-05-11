N, M = input().split()
N, M = int(N), int(M)
a = []
k = 0
ind = 1

for i in range(N):
	a.append([int(j) for j in input(). split()])

for i in range(N):
	z = 0
	for j in range(M):
		z += a[i][j]
	if i == 1:
		k = z
		continue
	if z < k:
		k = z
		ind = i

for row in a[ind]:
	print(row, end=' ')