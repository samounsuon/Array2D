def replace_char(array2D):
    isFond=False
    for char in array2D:
        for i in range(len(char)):
            if i ==len(char)-1:
                char[i]="*"
            if len(char)<3:
                isFond=True
    if not isFond:
        result=array2D
    else:
        result="Column error"
    return result
array2D=[
["A", "B","D"],
["D", "F","C"],
["A", "A","E"],
["V", "B","A"],
]
print(replace_char(array2D))