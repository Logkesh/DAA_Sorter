from Analyser import Analyse

def Partition(array: list, left: int, right: int,A: Analyse):
    A.mem(left)
    A.mem(right)
    i = left - 1
    A.mem(i)
    
    pivot = A.ret(array[right])
    A.mem(pivot)
    
    x = A.ret(left)
    A.mem(x)
    while A.comparelt(x, right):
        if A.comparelt(array[x],pivot) or A.equate(array[x], pivot):
            i = A.add(i)
            array[i],array[x] = A.swap(array[i],array[x])
        x = A.add(x)
    array[i+1],array[right] = A.swap(array[A.add(i)],array[right])
    return A.add(i)   
            
def QuickSort(array: list, A: Analyse, left = 0, right = None) -> list:
    A.mem(array)
    if right is None: right = A.sub(len(array))
    if(A.comparelt(left, right)):
        pivot = Partition(array, left, right, A)

        QuickSort(array,A,left,A.sub(pivot))
        QuickSort(array,A,A.add(pivot),right)
    return A.ret(array)
