## Matrix is one og the easiest topic. But implementation is important.
## Assignment will be based on this class.

## Java mein pass by reference. In c++ pass by value but with & its pass by reference.
## For python


# P1 How to print a matrix in snake pattern
# 1 2 3
# 4 5 6
# 7 8 9

# 123654789

# Try to write code in a function.

# Solved the question in file P1.py

##
## P2 Matrix boundary traversal problem. Example:
## 1 2 3 4
## 5 6 7 8
## 9 10 11 12
## 13 14 15 16
## Output 
# 1 2 3 4 
# 5     8 
# 9     12 
# 13 14 15 16 

## P3 Find the transpose of a matrix
##      By defination rows and columns are interchanged.
## 1 2 3
## 4 5 6
## 7 8 9 
## Both ways are allowed, you can create a new matrix or do it in place.


## P4 search in a row-wise & column wise sorted matrix.
## Matrix example looks like this:
## 1 2 3 4
## 2 5 6 8
## 3 10 15 18
## 4 12 20 40


## Moving on to P5
## P5 Rotate matrix anti-clockwise by 90 degree.
# 1 2 3
# 4 5 6
# 7 8 9

## 3 6 9
## 2 5 8
## 1 4 7

# Try To also look at transpose in terms of rotation.

## You will be able to see that transpose is just rotation but 90 clockwise.

## Transpose mirror image in x-axis.
## 1. Take transpose inplace and 2. reverse its column.

## Based on the spiral traversal there might be a question in the assignment.
## Spiral traversal.

## Think of variants for spiral traversal. 1. based on initial position of the starting point.
## Or you can think of variant with different direction of the spiral.
## Spiral Traversal TODO is availble in EPI


## Final Optional, 
## Array 
## 1 2 3 4 5
## 1 3 6 10 15
## Now think of prefix sum: prefix sum of a matrix How do you calculate it, 
## for prefix Sum of an array prefix[i] = prefix[i-1] + arr[i]
## Similarly we can think of a formula for prefix sum of a matrix prefix[i,j] = prefix[i-1,j]+prefix[i,j-1]-prefix[i-1,j-1]


## 1,2,3 will be easy questions in the assignment.
