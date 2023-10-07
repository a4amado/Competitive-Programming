from math import ceil, floor
num_of_coins = int(input())
coins_values = [int(x) for x in input().split(" ")]
coins_values.sort()

if (num_of_coins < 2):
    print(num_of_coins)
    exit()




c_sum = 0
other_sum = sum(coins_values)
num = 0

for i in range(num_of_coins -1, -1 , -1):
    if (other_sum >= c_sum):
        c_sum += coins_values[i]
        other_sum -= coins_values[i]
        num += 1
    else:
        break

print(num)
