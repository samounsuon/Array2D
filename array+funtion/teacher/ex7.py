def to_array_string(string):
    array_str=[]
    for char in string:
        array_str.append(char.upper())
    return array_str
array2D=["banana","apple","coconut"]
new=[]
for array in array2D:
    # for i in range(len(array)):
        new.append(to_array_string(array))
        new.pop(1)
print(new)