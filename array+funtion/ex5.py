def change_num(array2D):
    count=0
    array_num=[]
    for array in array2D:
        for i in range(len(array)):
            if  array[i]==7:
                count+=1
        array_num.append(count)
        count=0
    return array_num
array2D= [[1,3,5,7,7,7],[2,7,2,7,7,7]]
print(change_num(array2D))