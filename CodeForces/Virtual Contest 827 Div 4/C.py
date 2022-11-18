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
            if element!='R':
                return False
        return True
    
 

    # Iterate in all rows
    def get_first_pure_row_or_col_color(big_arr):
        for row_idx in range(n):
            if big_arr[row_idx][0]!='.' and is_pure_row(big_arr, row_idx):
                return 'R'
        return 'B'
    print(get_first_pure_row_or_col_color(big_arr))
t = int(input())
for _ in range(t):
    main()