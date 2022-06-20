n = int(input())
result = 'I hate'
if(n==1):
    result = 'I hate'
boolvar = True;
n-=1
while(n):
    if(boolvar):
        result += ' that I love'
    else:
        result += ' that I hate'
    boolvar = not boolvar
    n-=1
result+=' it'
print(result)