def local_num(array2D):
    array=[]
    isSeven=False
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j]==7 and isSeven==False:
                array.append(i)
                array.append(j)
                isSeven=True
    return array
array2D=[[5,3,8,4],[3,8,7,1],[1,4,6,3]]
print(local_num(array2D))