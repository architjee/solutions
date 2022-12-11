def main():
    size_A, size_B = map(int,input().split())
    A = input()
    B = input()
    def levenstein_distance(A, B):
        distance_between_prefixes= [[-1]*len(B) for _1 in A]
    
        def helper_function(a_index, b_index):
            ## Basically means that we have to add all elements of B.
            if a_index<0:
                return b_index+1
            ## Basically means that we have to delete all elments of A
            if b_index<0:
                return a_index+1

            if distance_between_prefixes[a_index][b_index]==-1:
                ## THis means we should calculate this distance.
                if A[a_index]==B[b_index]:
                    ## Last character same remove them from consideration and move on.
                    return helper_function(a_index-1, b_index-1)
                else:
                    substituting_last = 1 + helper_function(a_index-1, b_index-1)
                    insert_last = 1 + helper_function(a_index, b_index-1)
                    delete_last = 1 + helper_function(a_index-1, b_index)
                    distance_between_prefixes[a_index][b_index] = min(substituting_last, insert_last, delete_last)
            return distance_between_prefixes[a_index][b_index]
        return helper_function(len(A)-1, len(B)-1)
    print(levenstein_distance(A,B))
t = int(input())

for testCase in range(t):
    main()