def find(numbers):
    array2D=[]
    for value in numbers:
        array=[]
        for i in value:
            if i == 7 :
                array.append(8)
            else:
                array.append(i)
        array2D.append(array)
    return array2D
number=[[1,4,5,7,7,7],[1,2,7,7,7,7]]
print(find(number))