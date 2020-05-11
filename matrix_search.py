N, M = input().split()
N, M = int(N), int(M)
a = []
count = 0

for i in range(N):
	a.append([int(j) for j in input().split()])

K = int(input())

for row in a:
	for item in row:
		if item == K:
			count += 1

print(count)
