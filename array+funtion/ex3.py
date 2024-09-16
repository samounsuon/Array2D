# Input: [[1,2,5,6,7],[1,5,9,12,7]]
# Output: [[1,2,5,6,8],[1,5,9,12,8]]
def change_num(array2D):
    for array in array2D:
        for i in range(len(array)):
            if  array[i]==7:
                array[i]=8
    return array2D
array2D=eval(input("enter array number: "))
print(change_num(array2D))