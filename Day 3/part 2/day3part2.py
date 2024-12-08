import re

def find_mul(numbers_list):
    pattern = r'mul\(\d*\,\d*\)|do\(\)|don\'t\(\)'
    return re.findall(pattern, numbers_list)

def total_mul(mul_list, do_flag):
    total_mul = 0

    for mul in mul_list:
        print(f'going through mul_list {mul}')
        if 'do()' in mul:
            do_flag = True

        if 'don\'t()' in mul:
            do_flag = False

        if do_flag:
            print(f'do_flag {do_flag}, mul {mul}')
            match = re.search(r'mul\((\d+),(\d+)\)', mul)
            if match:
                num1, num2 = int(match.group(1)), int(match.group(2))
                total_mul += num1 * num2

    return total_mul, do_flag

def main():
    f = open("puzzle.txt", 'r')
    mul_total = 0
    flag_state = True
    for line in f:
        muls_list = find_mul(line)
        total_temp, flag_state = total_mul(muls_list, flag_state)
        mul_total += total_temp

    print(f'Total is: {mul_total}')

if __name__ == "__main__":
    main()