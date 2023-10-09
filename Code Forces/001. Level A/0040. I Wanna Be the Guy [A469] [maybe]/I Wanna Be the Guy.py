n_of_line = int(input())

n_1 = [int(x) for x in input().split(" ")]
n_2 = [int(x) for x in input().split(" ")]

range_ = max(len(n_2), len(n_1))

s = set()

for i in range(range_):
    try:
        i_1 = n_1[i]
        if (i_1 == 0):
            continue
        s.add(i_1)
    except IndexError:
        None
    try:
        i_2 = n_2[i]
        if (i_2 == 0):
            continue
        s.add(i_2)
    except IndexError:
        None

if (len(s) >= n_of_line):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")