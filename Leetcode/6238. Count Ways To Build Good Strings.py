
def countGoodStrings(low, high, zero, one):
    result = 0
    print("Using range of m as ", low//zero, (high+1)//zero)
    for m in range(low//zero, (high+1)//zero):
        print("Using range of m as ", low//one, (high+1)//one)
        for n in range(low//one, (high+1)//one):
            combination_length = (m*zero)+(n*one)
            print(combination_length)
            if low<=combination_length and high>=combination_length:
                print("Consider this combination")
                # So it has been decided that there are m*zero 0s and n*1 1s

print(countGoodStrings(3,3,1,1))