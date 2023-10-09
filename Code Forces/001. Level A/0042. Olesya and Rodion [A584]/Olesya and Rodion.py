digts, divider = map(int, input().split(" "))
NumOfZero = digts - (len(str(divider))) - 1

if (digts == 1 and divider == 10):
    print(-1)
    exit()


if (digts == 1):
    print(divider)
    exit()

if (divider == 2 and divider == 10):
    print(10)

if (divider == 10):
    print("1" + "0" * (digts - 1))

    exit()

s = str(divider) + ("0" * NumOfZero) + str(divider)

print(s)
