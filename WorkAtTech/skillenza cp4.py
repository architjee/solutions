size = int(input())
red_shirt_speeds = list(map(int,input().split()))
red_shirt_speeds.sort()
blue_shirt_speeds = list(map(int,input().split()))
blue_shirt_speeds.sort()
def get_total_speed(fastest = True):
    total_speed = 0
    for i in range(len(red_shirt_speeds)):
        if fastest:
            total_speed += max(red_shirt_speeds[i], blue_shirt_speeds[~i]) 
        else:
            total_speed += min(red_shirt_speeds[i], blue_shirt_speeds[i])
    return total_speed
print(get_total_speed())