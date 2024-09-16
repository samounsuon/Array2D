# Exercise 4:
#   Find first 7 in array 2D
# example1:
#   input : [[7,7,7],[0,9,7],[0,0,0]]
#   output : This is first seven locating at row 0 col 0.
array2D=[[5,3,8,4],[3,8,7,1],[1,4,6,3]]
ap_array=[]
isFound=False
for i in range(len(array2D)):
    for j in range(len(array2D[i])):
        if array2D[i][j]==7 and isFound==False:
            ap_array.append(i)
            ap_array.append(j)
            isFound=True
print (ap_array)

