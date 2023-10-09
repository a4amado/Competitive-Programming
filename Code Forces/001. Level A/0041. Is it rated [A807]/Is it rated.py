number_of_lines = int(input())

lis = []
lis_2 = []

for i in range(number_of_lines):
    s = input().split(" ")
    lis.append(s[0])
    lis_2.append(s[1])

if lis_2 != lis:
    print("rated")
    exit()

lis_2_reversed = sorted(lis_2, reverse=True)

if (lis_2_reversed != lis_2):
    print("unrated")
    exit()


print("maybe")

