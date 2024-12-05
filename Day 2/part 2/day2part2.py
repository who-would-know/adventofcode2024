def is_increasing(numbers_list):
    # is increasing?
    for i in range(len(numbers_list) - 1):
        if  not numbers_list[i] < numbers_list[i + 1]:
            return False
    return True

def is_decreasing(numbers_list):
    # is decreasing?
    for i in range(len(numbers_list) - 1):
        if  not numbers_list[i] > numbers_list[i + 1]:
            return False
    return True

def is_diff(numbers):
# is diff by at least 1 or less than 3?
    for i in range(len(numbers) - 1):
        num_diff = abs(numbers[i] - numbers[i+1])
        if not num_diff < 4 and num_diff != 0:
            return False
    return True

def main():
    total_safe_reports = 0

    with open ("puzzle.txt", 'r', encoding="utf-8") as f:
        for line in f:
            numbers = list(map(int, line.split()))

            if (is_increasing(numbers) or is_decreasing(numbers)) and is_diff(numbers):
                print(f'number list nothing changed: {numbers}')
                total_safe_reports += 1
            else:
                # Check if validate by removing 1 element
                for i in range(len(numbers)):
                    temp_list = numbers[:i] + numbers[i + 1:]
                    if (is_increasing(temp_list) or is_decreasing(temp_list)) and is_diff(temp_list):
                        print(f'removed element from list: {temp_list}')
                        total_safe_reports += 1
                        break

    print(f'Total Safe Reports: {total_safe_reports} ')

if __name__ == "__main__":
    main()