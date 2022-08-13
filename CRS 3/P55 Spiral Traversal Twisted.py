# Atleast read the question properly. The question is a variant of that taught in the class. Hwre we are trying to spiral Outwards


# We  are given a matrix with P rows and q columns All filled with zero.
p, q, n = map(int, input().split())
bigList = [[0 for _ in range(q)] for __ in range(p)]
initialX , initialY = map(int, input().split())

for _ in range(n):
    y, x, val = map(int, input().split())
    bigList[y][x] = val
print(bigList)
directionsArr = [1,2,3,4]
# We are going to initialize limits for x(both start and end) and same for y.
llX = 0
llY = 0
ulX = q - 1
ulY = p - 1
# Intial position of x and y
x = initialX
y = initialY
# Using direction
currentDirection = 0
def printUtilFunc(x, y, moveX , moveY, llX, ulX, llY, ulY):
    while y <= ulY and y >= llY and x <= ulX and x >= llX:
        print(x, y, bigList[y][x], currentDirection+1)
        x += moveX
        y += moveY
    return y, x
while llX<=ulX and llY<=ulY and ulX<q and ulY<p and llX>=0 and llY:
    if currentDirection==0:
        # moving downwards
        moveX = 0
        moveY = 1
        y, x = printUtilFunc(x, y)
        # When we have finished printing. Let us modify the limits somehow.

    elif currentDirection==1):
        # moving right
        moveX = 1
        moveY = 0
    elif currentDirection==2:
        # moving upwards
        moveX =0
        moveY = -1
    elif currentDirection==3:
        # Moving left
        moveX = -1
        moveY = 0
    currentDirection += 1