number_of_cities = input()

l_of_cities = []

cities = input().split(" ")

for idx, element in enumerate(cities):
    l_of_cities.append(int(element))

l_of_cities.sort()


for idx, element in enumerate(l_of_cities):
    # if first city
    if idx == 0:
        print(abs(l_of_cities[idx + 1]  - element) ,  abs(element - (l_of_cities[len(l_of_cities)  -1])))
        continue
    # if last city
    if idx == len(l_of_cities) - 1:
        print(abs(element - l_of_cities[idx - 1]),  abs(element  - (l_of_cities[0])))
        continue
    else:
        min_i = min(abs(element - l_of_cities[idx - 1]), abs(l_of_cities[idx + 1] - element))
        max_i = max(abs(element - l_of_cities[0]), abs(l_of_cities[len(l_of_cities)  -1] - element))

        print(min_i, max_i)
        