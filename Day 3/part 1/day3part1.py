import re

def find_mul(numbers_list):
    return re.findall(r'mul\(\d*\,\d*\)', numbers_list)

def total_mul(mul_list):
    total_mul = 0
    for mul in mul_list:
        match = re.search(r'mul\((\d+),(\d+)\)', mul)
        if match:
            num1, num2 = int(match.group(1)), int(match.group(2))
            total_mul += num1 * num2
    return total_mul

def main():
    f = open("puzzle.txt", 'r')
    mul_total = 0
    for line in f:
        muls_list = find_mul(line)
        mul_total += total_mul(muls_list)

    print(f'Total is: {mul_total}')

if __name__ == "__main__":
    main()