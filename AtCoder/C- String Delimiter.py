n = int(input())
str = input()
i=0
result = ['' for x in range(n)]
while i<len(str):
    curr_character = str[i]
    if curr_character=='"':
        result[i] = curr_character
        i+=1
        while str[i]!='"':
            result[i] = str[i]
            i+=1
        ## Now str=='"'
        result[i]=str[i]
        i+=1
        continue
    if curr_character==',':
        result[i] = '.'
    else:
        result[i]=str[i]
    i+=1
print(''.join(result))