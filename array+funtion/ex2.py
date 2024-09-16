# def sum (array):
#     sum=0
#     for num in array:
#         sum+=num
#     return sum 
# def max_numbers(array2D):
#     total=0
#     for array in array2D:
#         if total==0:
#             total = sum(array)
#         elif total <sum(array):
#             total = sum(array)
#     return total
# array2D = [[1,2,3],[4,3,5],[1,0,7],[2,2,2]]
# print (max_numbers(array2D))# array2D = [[1,2,3],[4,3,5],[1,0,7],[2,2,2]]
# print(max_numbers(array2D))
def sum(array):
    sum = 0
    for number in array:
        sum += number
    return sum
def max_array(array2d):
    max_array = []
    max = 0
    for array in array2d:
        if sum(array) > max:
            max = sum(array)
            max_array = array
    return max_array
array2d = [[1,2,3],[4,3,5],[1,0,7],[2,2,2]]
print(max_array(array2d))