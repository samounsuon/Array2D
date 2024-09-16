def sum(array):
    sum=0
    for number in array:
        sum+=number
    return sum
def max_2D(array2D):
    max_number=sum(array2D[0])
    max_array=[]
    for array in array2D:
        if sum(array)>max_number:
            max_number = sum(array)
            max_array=array
    return max_array,max_number
array2D=[
    [-1,-2],
    [-8,-9],
    [-0,-1],
    [-1,-4]
]
print("Max number is "+str(max_2D(array2D)[0])+" with sum is "+ str(max_2D(array2D)[1]))