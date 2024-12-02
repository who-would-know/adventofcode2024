list_1 = []
list_2 = []
similarity_score = 0

with open ("puzzle.txt", 'r', encoding="utf-8") as f:
    for line in f:
        numbers = list(map(int, line.split()))
        list_1.append(numbers[0])
        list_2.append(numbers[1])
    
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    for num in list_1:
        similarity_score += num * list_2.count(num)

print(f'Similarity Score: {similarity_score}')