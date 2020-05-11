def sum(num):
	z = 0
	for x in num:
		z = z + int(x)
	return z


N, M = input().split()
N, M = int(N), int(M)
a = []
count_num = 0

for i in range(N):
	a.append([int(j) for j in input(). split()])

K = int(input())
R = int(input())

for i in range(N):
	for j in range(M):
		if len(str(a[i][j])) == K and sum(str(a[i][j])) % R == 0:
			count_num += 1

print(count_num)