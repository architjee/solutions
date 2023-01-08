class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ## We create a line by choosing 2 points
        if not points:
            return 0
        no_points_pass_through = 1
        def create_line(point_1, point_2):
            if point_2[0]-point_1[0]==0:
                return (float('inf'), point_2[0])
            m = (point_2[1]-point_1[1])/(point_2[0]-point_1[0])
            equation = (m, point_1[1]-(point_1[0]*m))
            return equation
        
        def check_points_pass_through_l(line, points_array):
            if line[0]==float('inf'):
                num_points_pass=0
                for point in points_array:
                    if point[0]==line[1]:
                        num_points_pass +=1
                return num_points_pass
            else:
                num_points_pass=0
                for point in points_array:
                    if math.isclose(point[1],(line[0]*point[0])+line[1]):
                        num_points_pass +=1
                return num_points_pass

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                l = create_line(points[i], points[j])
                # print('l is the line created', l)
                no_points_pass_through = max(no_points_pass_through, check_points_pass_through_l(l, points))
        return no_points_pass_through

        ## I solved it using a brute-force method.