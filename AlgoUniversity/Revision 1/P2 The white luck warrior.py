
# ll -> lower_left
# ur -> upper_right 
lower_left_x1, lower_left_y1 , upper_right_x1, upper_right_y1 = map(int, input().split())
lower_left_x2, lower_left_y2 , upper_right_x2, upper_right_y2 = map(int, input().split())
side = max(upper_right_x1, upper_right_x2) - min(lower_left_x1, lower_left_x2) 
height = max(upper_right_y1, upper_right_y2) - min(lower_left_y1, lower_left_y2)
print(max(side, height)**2)