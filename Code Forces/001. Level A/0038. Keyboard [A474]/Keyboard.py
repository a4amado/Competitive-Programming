

key_board = [
    "qwertyuiop",
    "asdfghjkl;",
    "zxcvbnm,./"
]



direction = input()
chars = input()

def getLetter(letter, p):

    for idx, row in enumerate(key_board):
        for nd_idx in range(len(row)):
            if (row[nd_idx] == letter):
                is_first_char = 0 == nd_idx
                is_last_char = len(row) -1 == nd_idx
                if (is_first_char):
                    if p == "L":
                        return   row[nd_idx + 1]
                    elif p == "R":
                        return letter
                elif is_last_char:
                    if p == "L":
                        return letter
                    elif p == "R":
                        return  row[nd_idx - 1]   
                else:
                    if p == "R":
                        return row[nd_idx - 1] 
                    else:
                        return row[nd_idx + 1]

w = ""
for i in range(len(chars)):
    w += getLetter(chars[i], direction)

print(w)