from Analyser import Analyse

def BubbleSort(array: list,A: Analyse) -> list:
    SIZE = A.ret(len(array))
    i = A.ret(0)
    while A.comparelt(i, SIZE):
        j = A.ret(0)
        while A.comparelt(j, SIZE-1):
            if A.comparegt(array[j], array[j + 1]):
                array[j],array[j+1] = A.swap(array[j],array[j+1])
            j = A.add(j)
        i = A.add(i)
    return A.ret(array)

def BucketSort(array: list, A: Analyse) -> list:
    # Size of the bucket will be the array length
    SIZE = A.ret(len(array))
    A.mem(SIZE)
    
    MAX = A.ret(max(array))
    A.mem(MAX)
    
    HASH = A.ret(A.div(MAX,SIZE))
    A.mem(HASH)
    
    res = A.ret(list())
    
    hash = A.ret([A.ret(list()) for i in range(SIZE+1)])
    A.mem(hash)
    
    for i in map(A.ret,array):
        index  = A.ret(int(A.div(i,HASH)))
        hash[A.ret(index)].append(A.ret(i))
    i = A.ret(0)
    
    while A.comparelt(i, SIZE) or A.equate(i, SIZE):
        hash[A.ret(i)] = A.ret(BubbleSort(hash[A.ret(i)],A))
        res.extend(hash[i])
        i = A.add(i)
    A.mem(res)
    return A.ret(res)
        
