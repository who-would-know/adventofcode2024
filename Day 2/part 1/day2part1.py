total_safe_reports = 0

with open ("puzzle.txt", 'r', encoding="utf-8") as f:
    for line in f:
        increasing = True
        decreasing = True
        is_diff = True

        numbers = list(map(int, line.split()))

        # is increasing?
        for i in range(len(numbers) - 1):
           if  not numbers[i] < numbers[i + 1]:
               increasing = False
               break
           
        # is decreasing?
        for i in range(len(numbers) - 1):
            if not numbers[i] > numbers[i + 1]:
                decreasing = False
                break

        # is diff by at least 1 or less than 3?
        if increasing or decreasing:
            for i in range(len(numbers) - 1):
                num_diff = abs(numbers[i] - numbers[i+1])
                if not num_diff < 4 and num_diff != 0:
                    is_diff = False
                    break

        if (increasing or decreasing) and is_diff:
            total_safe_reports += 1

print(f'Total Safe Reports: {total_safe_reports} ')