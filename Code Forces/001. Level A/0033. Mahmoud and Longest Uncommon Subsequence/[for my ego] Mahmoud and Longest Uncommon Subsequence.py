from itertools import combinations


s_1 = input()
s_2 = input()


if s_1 == s_2:
    print(-1)
    exit()
    
list_1 = []
list_2 = []

for i in range(len(s_1)):
    for j in range(len(s_1)):
        if (s_1[i:j+1] != ""):
            list_1.append(s_1[i:j+1])


for i in range(len(s_2)):
    for j in range(len(s_2)):
        list_2.append(s_2[i:j+1])

le = 0


for idx, element in enumerate(list_1):
    try:
        list_2.index(element)
    except ValueError:
        if len(element) > le:
            le = len(element)


for idx, element in enumerate(list_2):
    try:
        list_1.index(element)
    except ValueError:
        if len(element) > le:
            le = len(element)


print(le)
