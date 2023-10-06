import sys




num_of_friends = input()

ps = input().split(" ")

res = [None for _ in range(int(num_of_friends))]

for index, element in enumerate(ps):
    res[int(element) -1] = index +1



print(*res)