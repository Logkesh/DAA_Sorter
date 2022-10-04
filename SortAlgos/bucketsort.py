def swap(a,b):
    return b,a

def BubbleSort(array: list) -> list:
    SIZE = len(array)
    for i in range(SIZE):
        for j in range(SIZE-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = swap(array[j],array[j+1])
    return array

def BucketSort(array: list) -> list:
    # Size of the bucket will be the array length
    SIZE = len(array)
    MAX = max(array)
    HASH = MAX/SIZE 
    res = list()
    hash = [list() for i in range(SIZE+1)]
    for i in array:
        index  = int(i/HASH)
        hash[index].append(i)
    for i in range(SIZE+1):
        hash[i] = BubbleSort(hash[i])
        res.extend(hash[i])
    return res
        
