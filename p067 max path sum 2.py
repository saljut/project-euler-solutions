# Maximum path sum II, Problem 67
# Problem description:
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.

# Task: Find the maximum total from top to bottom in triangle.txt 
# (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
# NOTE: This is a much more difficult version of Problem 18. 
# It is not possible to try every route to solve this problem,as there are 299 altogether! 
# If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
# There is an efficient algorithm to solve it. ;o)
# https://projecteuler.net/problem=67

# Note: this is the exact same solution as the one for problem 18

def triangleFromFile(filename):
    ''' reads the triangle from filename into a list of lists '''
    triangle = []
    with open(filename, "r") as infile:
        line = infile.readline().strip()
        while line:
            sList = line.split(" ")
            numList = [int(s) for s in sList]
            triangle.append(numList)
            line = infile.readline().strip()
    return triangle


def maxPathSumHelper(triangle, memoTri, i, j):
    ''' returns path with highest value from current spot to top '''
    if i == -1 or j == -1 or j >= len(triangle[i]):
        return 0
    if memoTri[i][j] != 0:
        return memoTri[i][j]
    else:
        costLeft = maxPathSumHelper(triangle[:-1], memoTri, i-1, j-1)
        costRight = maxPathSumHelper(triangle[:-1], memoTri, i-1, j)
        if costLeft > costRight:
            memoTri[i][j] = costLeft + triangle[i][j]
        else:
            memoTri[i][j] = costRight + triangle[i][j]
    return memoTri[i][j]


def maxPathSum(triangle, memoTri):
    ''' finds value for every bottom spot to top,
        and returns the greatest one '''
    i = len(triangle) - 1
    highest = 0
    for j in range(len(triangle[-1])):
        current = maxPathSumHelper(triangle, memoTri, i, j)
        if current > highest:
            highest = current
    return highest


triangle = triangleFromFile("p067_triangle.txt")
memoTri = [[0 for j in range(len(triangle[i]))] for i in range(
    len(triangle))] #creates the triangle for values to be saved in, with same size as original triangle
score = maxPathSum(triangle, memoTri)
print("Answer: {}".format(score))