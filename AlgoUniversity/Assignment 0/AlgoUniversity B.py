
x1, y1 , x2 , y2 = map(int, input().split());

x3, y3 , x4 , y4 = map(int, input().split());

minX = min(x1,x2, x3, x4)
maxX = max(x1,x2,x3,x4);
ax = maxX-minX 
minY = min(y1,y2,y3,y4);
maxY = max(y1,y2,y3,y4);
ay = maxY - minY;
store = max(ax,ay);
print(store**2)