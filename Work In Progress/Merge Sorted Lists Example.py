# Implementing Merging of Sorted Lists (in Python 128).
def merge(x, y):
    z = []
    i=0
    j=0
    while i < len(x) or j < len(y):
        if j == len(y) or i < len(x) and x[i] <= y[j]: # priority on x
            z.append(x[i])
            i += 1
        else:
            z.append(y[j]) # now switch to y
            j += 1
    return z

