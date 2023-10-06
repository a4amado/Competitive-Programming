n = int(input())
a = list(map(int, input().split()))

if n < 3:
    print(0)
    exit()

a.sort()
sol = 0

for i in range( n ):
    if a[i] > a[0] and a[i] < a[n - 1] and i != 0 and i != len(a) - 1:
        sol += 1

print(sol)
