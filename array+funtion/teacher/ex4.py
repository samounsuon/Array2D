# def sum(array2D):
#     ap_array=[]
#     sum=0
#     index=0
#     n=0
#     for array in array2D:
#         if len(array) >n:
#             n=len(array)
#     while index<n:
#         for array in array2D:
#             for i in range(len(array)):
#                 if i==index:
#                     sum+=array[i]
#         ap_array.append(sum)
#         sum=0    
#         index+=1
#     return ap_array
# array2D=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# print(sum(array2D))
def sumColumns(array2D):
    numColumns = len(array2D[0])
    columnSums = [0] * numColumns
    for row in array2D:
        for j in range(numColumns):
            columnSums[j] += row[j]
    return columnSums
array2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sumColumns(array2D))