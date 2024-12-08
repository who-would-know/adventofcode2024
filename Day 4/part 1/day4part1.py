def find_horizontal(horiz_matrix):
    total_horizontal = 0

    for line in horiz_matrix:
        for index, char in enumerate(line):
            if line[index:index + 4] in ("XMAS","SAMX"):
                total_horizontal += 1
                #DEBUG
                # print(f'Found Horiz: {line[index:index + 4]}')
    
    return total_horizontal
                
def find_vertical(vert_matrix):
    total_vertical = 0

    #Loop through a Matrix
    for i, row in enumerate(vert_matrix):
       if i + 3 < len(vert_matrix):
            for j, element in enumerate(row):
                vertical_string = vert_matrix[i][j] + vert_matrix[i + 1][j] + vert_matrix[i + 2][j] + vert_matrix[i + 3][j]
                if vertical_string in ("XMAS","SAMX"):
                    total_vertical += 1
                    #DEBUG
                    # print(f'Found Vert: {vertical_string}')     

    return total_vertical

def find_diagonal(diag_matrix):
    total_diagonal = 0
    #Loop through a Matrix
    for i, row in enumerate(diag_matrix):
       if i + 3 < len(diag_matrix):
            for j, element in enumerate(row):
                #Look right
                if j + 3 < len(row):
                    diagnal_right_string = diag_matrix[i][j] + diag_matrix[i + 1][j + 1] + diag_matrix[i + 2][j + 2] + diag_matrix[i + 3][j + 3]
                    if diagnal_right_string in ("XMAS", "SAMX"):
                        total_diagonal += 1
                        #DEBUG
                        # print(f'Found diag right: {diagnal_right_string}')   
                #Look left
                if j - 3 > -1:
                    diagnal_left_string = diag_matrix[i][j] + diag_matrix[i + 1][j - 1] + diag_matrix[i + 2][j - 2] + diag_matrix[i + 3][j - 3]
                    if diagnal_left_string in ("XMAS", "SAMX"):
                        total_diagonal += 1
                        #DEBUG
                        # print(f'Found diag right: {diagnal_left_string}')   
  
    
    return total_diagonal
    
def main():
    f = open("puzzle.txt", 'r')
    xmas_total = 0
    f_matrix = [line.strip() for line in f]

    xmas_total += find_horizontal(f_matrix)
    xmas_total += find_vertical(f_matrix)
    xmas_total += find_diagonal(f_matrix)


    print(f'Total XMAS found: {xmas_total}')

    f.close()

if __name__ == "__main__":
    main()