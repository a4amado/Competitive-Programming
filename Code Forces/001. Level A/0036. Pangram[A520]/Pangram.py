# Name: A. Pangram
# Link: https://codeforces.com/contest/520/problem/A


num_of_chars = int(input())

word = input()


if (num_of_chars < 26):
    print("NO")
    exit()

chars = set()

for idx in range(num_of_chars):
    char = word[idx]
    l = char.lower()
    chars.add(l)


if (len(chars) >= 26):
    print("YES")
else:
    print("NO")