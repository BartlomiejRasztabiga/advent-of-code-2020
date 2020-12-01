with open('input.txt', 'r') as file:
    numbers = [int(x) for x in file.readlines()]
    for number in numbers:
        looking_for = 2020 - number
        try:
            found_index = numbers.index(looking_for)
            result = numbers[found_index]
            print(result * number)
            break
        except:
            continue
