# CodeForces Round 827 Div.4
# A.Stripes.py
def main():
    n = 8
    empty_block = input()
    big_arr = []
    for i in range(n):
        big_arr.append(list(input()))
    
    def is_pure_row(big_arr, i):
        row = big_arr[i]
        for element in row:
            if element!=row[0]:
                return False
        return True
    
    def is_pure_col(big_arr, j):
        prevElement=big_arr[0][j]
        for k in range(n):
            element = big_arr[k][j]
            if element!=prevElement:
                return False
            prevElement = element
        return True
 

    # Iterate in all rows
    def get_first_pure_row_or_col_color(big_arr):
        for row_idx in range(n):
            if big_arr[row_idx][0]!='.' and is_pure_row(big_arr, row_idx):
                return big_arr[row_idx][0]
        for col_idx in range(n):
            if big_arr[0][col_idx]!='.' and is_pure_col(big_arr, col_idx):
                return big_arr[0][col_idx]
        return 'B'
    print(get_first_pure_row_or_col_color(big_arr))
t = int(input())
for _ in range(t):
    main()