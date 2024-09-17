array2D=[
['B', 'A', 'N', 'A', 'N', 'A'],
['C', 'O', 'C', 'O', 'N', 'U', 'T']
]
result=[]
for array in array2D:
    sum=""
    for i in range(len(array)):
        sum+=array[i]
    result.append(sum.lower())
print(result)
