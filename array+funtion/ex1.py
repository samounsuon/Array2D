def sum(array):
    sum=0
    for num in array:
        sum+=num
    return sum
def sum_array2D(array2D):
    total=0
    for array in array2D:
        total +=sum(array)
    return total
array2D=[[1,2,3],[4,5,6]]
print(sum_array2D(array2D))
