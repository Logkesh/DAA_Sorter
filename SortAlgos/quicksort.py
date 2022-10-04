def Partition(array: list, left: int, right: int):
    i = left - 1
    pivot = array[right]
    
    for x in range(left,right):
        if array[x] <= pivot:
            i+=1
            array[i],array[x] = array[x],array[i]
    array[i+1],array[right] = array[right],array[i+1]
    return i + 1   
            
def QuickSort(array: list, left = 0, right = None) -> list:
    if right is None: right = len(array)-1
    if(left < right):
        pivot = Partition(array, left, right)

        QuickSort(array,left,pivot-1)
        QuickSort(array,pivot+1,right)
    return array
