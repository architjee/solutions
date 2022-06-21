def rightBody(cols):
    return "."*(cols-1)+"#"

def leftBody(cols):
    return "#"+"."*(cols-1)
# Fox and Snake program 
rows, cols = map(int, input().split());
# Given that n is an odd no.
# n-1/2 Iterations work karna hai.
i = 0;
pos = True;
while(i<rows):
    if(i%2==0):
        print("#"*cols)
    else:
        if(pos):
            print(rightBody(cols))
        else :
            print(leftBody(cols))
        pos = not pos
    i+=1;