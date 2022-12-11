## Distance between two strings, A and B
## if we were allowed three operations insert, edit, or delete.
## Sundays and Saturdays differ by 4
## One must understand that there can be only two possible cases considering last character of each A and B.
### 1. Either A[-1]=B[-1] which means we should focus on A[:len(A)-2] and B[:len(B)-2]
### 2. EIther they may not be equal which again puts us at 3 possibilities.
##  ## i. either you can substitute A[-1] with B[-1] => 1+costOF(A[:len(A)-2],B[:len(B)-2])
##  ## ii. Or we can simply delete A[-1] => This cost + 1
##  ## iii. Or we can insert B[-1] in hopes that now the distance between len(old A)-1 , len(B)-2 => This cost + 1

## Now let us implement this in a fashion.
def levenstein_distance(A, B):
    ## Obnective will be to convert A to B.
    
    def distance_helper_between_prefixes(a_idx, b_idx):
        if a_idx<0:
            # A is completely empty so we have to add all the letters till b_idx.
            return  b_idx + 1
        if b_idx<0:
            # we have to delete all the elements of from a_idx.
            return a_idx + 1
        
        if distance_between_prefixes[a_idx][b_idx]==-1:
            if A[a_idx]==B[b_idx]:
                distance_between_prefixes[a_idx][b_idx]= distance_helper_between_prefixes(a_idx-1, b_idx-1)
            else:
                ## Now here are 3 possible different scenarios.
                substitute_last = distance_helper_between_prefixes(a_idx-1, b_idx-1)
                add_last = distance_helper_between_prefixes(a_idx-1, b_idx)
                delete_last = distance_helper_between_prefixes(a_idx, b_idx-1)
                distance_between_prefixes[a_idx][b_idx] = 1 + min(substitute_last, add_last, delete_last)
        return distance_between_prefixes[a_idx][b_idx]

    distance_between_prefixes=[[-1]*len(B) for _ in range(len(A))]
    return distance_helper_between_prefixes(len(A)-1, len(B)-1)
        
print(levenstein_distance('saturday', 'sundays'))
