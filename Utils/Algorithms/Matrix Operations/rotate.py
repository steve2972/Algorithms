from this import d
from transpose import transpose

def rotate_clockwise(arr):
    transpose(arr)
    for l in range(len(arr)):
        i,j = 0,len(arr[l])-1
        while i < j:
            arr[l][i],arr[l][j] = arr[l][j],arr[l][i]
            i+=1
            j-=1

def rotate():
    transpose(arr)
    for l in range(len(arr)):
        i,j=0,len(arr)-1
        while i<j:
            arr[i][l],arr[j][l]=arr[j][l],arr[i][l]
            i+=1;j-=1

arr = [
    [1,2,3,4,5],
    [6,7,8,9,8],
    [7,6,5,4,3],
    [2,1,2,3,4],
    [5,6,7,8,9]
]