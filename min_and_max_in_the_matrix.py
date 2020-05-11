N, M = input().split()
N, M = int(N), int(M)
a = []
b = [0 for i in range(6)]

for i in range(N):
	a.append([int(j) for j in input().split()])

b[0], b[1], b[2] = a[0][0], 0, 0
b[3], b[4], b[5] = a[0][0], 0, 0

for i in range(N):
	for j in range(M):
		if b[0] < a[i][j]:
			b[0], b[1], b[2] = a[i][j], j, i

		if b[3] > a[i][j]:
			b[3], b[4], b[5] = a[i][j], j, i

print(b[5] + 1, b[4] + 1, b[3])
print(b[2] + 1, b[1] + 1, b[0])
