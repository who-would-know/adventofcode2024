list_1 = []
list_2 = []
total_distance = 0

with open ("puzzle.txt", 'r', encoding="utf-8") as f:
    for line in f:
        numbers = list(map(int, line.split()))
        list_1.append(numbers[0])
        list_2.append(numbers[1])
    
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    for num1, num2 in zip(list_1, list_2):
        total_distance += abs(num1 - num2)
    
print(f'Total Distance: {total_distance} ')
