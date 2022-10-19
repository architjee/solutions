p1, reloadTime1 = map(int, input().split())
p2, reloadTime2 = map(int, input().split())
health, shield = map(int, input().split())
# Each time a laser/lasers are fired. health is dealt/reduced by power - shield
# When health becomes negative stop. 
globalClock = 0
n1 = 1
n2 = 1
while health>0:
    attackPower = 0
    # We can fire l1 when globalClock is at every globalClock%reloadTime1==0 time.
    # Or we can say in other terms l1 fired at reloadTime * 1 + reloadTime *2
    if n1*reloadTime1 > n2*reloadTime2:
        # Fire l2
        globalClock += n2*reloadTime2-globalClock
        n2+=1
        attackPower = p1
    elif n1*reloadTime1 < n2*reloadTime2 :
        # Fire le
        globalClock += n1*reloadTime1-globalClock
        n1+=1
        attackPower= p2
    else:
        # Fire both
        globalClock += n1*reloadTime1
        n1+=1
        n2+=1
        attackPower = p1 + p2
    health-=(attackPower-shield)
print(globalClock)