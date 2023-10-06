number_of_stewards  = int(input())

if number_of_stewards < 3:
    print(0)
    exit()


s = [int(x) for x in input().split(" ")]
s.sort()

print(len(s) - 2)