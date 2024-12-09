def find_mas(matrix):
    total_mas = 0
    #Loop through a Matrix
    for i, row in enumerate(matrix):
       if i + 2 < len(matrix):
            for j, element in enumerate(row):
                if j + 2 < len(row):
                    get_first_row = element + matrix[i][j+2]
                    get_second_row = matrix[i+1][j+1]
                    get_third_row = matrix[i+2][j] + matrix[i+2][j+2]
                    get_all = get_first_row + get_second_row + get_third_row
                    # Fist Combo
                    if get_first_row in "MM" and get_second_row in "A" and get_third_row in "SS":
                        print(f'Found first combo: {get_all}')
                        total_mas += 1
                    # Second Combo
                    if get_first_row in "SS" and get_second_row in "A" and get_third_row in "MM":
                        print(f'Found second combo: {get_all}')
                        total_mas += 1
                    # Third Combo
                    if get_first_row in "MS" and get_second_row in "A" and get_third_row in "MS":
                        print(f'Found third combo: {get_all}')
                        total_mas += 1
                    # Fourth Combo
                    if get_first_row in "SM" and get_second_row in "A" and get_third_row in "SM":
                        print(f'Found four combo: {get_all}')
                        total_mas += 1
                    

    return total_mas


def main():
    f = open("puzzle.txt", 'r')
    xmas_total = 0
    f_matrix = [line.strip() for line in f]

    xmas_total = find_mas(f_matrix)

    print(f'Total XMAS found: {xmas_total}')

    f.close()

if __name__ == "__main__":
    main()