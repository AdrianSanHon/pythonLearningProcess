def summaArray(array1, array2):
    array3 = []
    for i in range(0, len(list(array1))):
        array3.append((array1[i])+(array2[i]))
    return array3

def printArray(array3):
    for i in array3:
        print(i)

array1 = [1, 2, 3]

printArray(summaArray(array1,array1))
