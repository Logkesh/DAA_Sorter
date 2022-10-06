from Analyser import Analyse            # User Defined Class to Analyse the Sorting Alogorithm 

# Bubble Sort used for sorting the elements in each bucket
def BubbleSort(array: list, A: Analyse) -> list:
    # Size of the bucket
    SIZE = A.ret(len(array))
    A.mem(SIZE)
    
    # Traversing over the bucket
    i = A.ret(0)
    while A.comparelt(i, SIZE):
        
        # Traversingb the bucket again to compare and swaps 
        j = A.ret(0)
        while A.comparelt(j, SIZE-1):
            
            # Comparing the corresponding elements 
            if A.comparegt(array[j], array[j + 1]):

                # Swaping the elements if the condition is true
                array[j],array[j+1] = A.swap(array[j],array[j+1])

            j = A.add(j)

        i = A.add(i)
    
    #Returning the sorted array
    return A.ret(array)

def BucketSort(array: list, A: Analyse) -> list:
    # Size of the actual array
    SIZE = A.ret(len(array))
    A.mem(SIZE)
    
    # Maximum value in the array
    MAX = A.ret(max(array))
    A.mem(MAX)
    
    # Hash value for the hashtable from MAX ans SIZE
    HASH = A.ret(A.div(MAX,SIZE))
    A.mem(HASH)
    
    # Result Array
    res = A.ret(list())
    
    # Hash table containing buckets for sorting the elements
    hash = A.ret([A.ret(list()) for i in range(SIZE+1)])
    
    # Calculating the hash value for each element in array
    # And storing the element in hash table
    for i in map(A.ret,array):
        index  = A.ret(int(A.div(i,HASH)))
        hash[A.ret(index)].append(A.ret(i))
    i = A.ret(0)
    
    # Sorting the each bucket and storing into the resultant array
    while A.comparelt(i, SIZE) or A.equate(i, SIZE):
        hash[A.ret(i)] = A.ret(BubbleSort(hash[A.ret(i)],A))
        res.extend(hash[i])
        i = A.add(i)
        
    A.mem(res)
    A.mem(hash)
    return A.ret(res)
        
