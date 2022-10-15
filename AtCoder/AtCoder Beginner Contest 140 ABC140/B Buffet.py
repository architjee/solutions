n = int(input())
orderOfDishesEaten = list(map(int,input().split()))
pointsForRespectiveDish = list(map(int, input().split()))
additionalPoints = list(map(int,input().split()))
pointsEarned = 0
prevDishEaten = -2
for dish in orderOfDishesEaten:
    pointsEarned += pointsForRespectiveDish[dish-1]
    if dish == prevDishEaten+1:
        pointsEarned += additionalPoints[prevDishEaten-1]
    prevDishEaten = dish
print(pointsEarned)