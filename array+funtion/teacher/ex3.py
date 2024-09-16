def replace(array2D):
    isSeven=False
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j]==7 and isSeven==False:
                array2D[i][j]=8
        if  array2D[i][j]==[]:
            array2D=[]
    return array2D 
array2D=[[5, 7, 8, 4], [5, 7, 8, 4], [5, 7, 8, 4]]
print(replace(array2D))