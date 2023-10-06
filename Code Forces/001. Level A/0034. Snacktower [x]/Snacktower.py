n_of_snakes = int(input())


sizes = input().split(" ")



days = [None for int in sizes]

def generate_descending_numbers_string(start, end):
    start, end = max(start, end), min(start, end)
    if (start == end):
        return str(start)
    # Generate a list of numbers in descending order
    numbers = [str(x) for x in range(start, end - 1, -1)]

    # Join the numbers into a single string with spaces
    result = ' '.join(numbers)
    
    return result

done = n_of_snakes

for idx, item in enumerate(sizes):
    should_be = int(n_of_snakes) - int(idx)
    current_value = int(item)
    should_shkip = should_be > current_value

    starting_gen = int(done) 
    end_gen = n_of_snakes - idx

    if not should_shkip:
        ss = generate_descending_numbers_string(starting_gen, end_gen)
        days[idx] = ss
        if (done <= current_value):
            done = done -1 


for i, item in enumerate(days):
    if (item == None):
        print("")
    else:
        print(item)


