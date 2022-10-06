from Analyser import Analyse            # User Defined Class to Analyse the Sorting Alogorithm

# Merge Sort Function
def MergeSort(array, A: Analyse):

    n = A.ret(len(array))
    A.mem(n)
    if A.comparelt(n,2):
        return A.ret(array)
    else:
        mid = A.divf(n,2)
        # Declaring half of the array as A1
        A1 = A.ret(array[:mid]) 
        A.mem(A1)
        # Declaring the remaining half as A2
        A2 = A.ret(array[mid:]) 
        A.mem(A1)
        # Recursive call for sorting subarray A1 & A2
        MergeSort(A1,A) 
        MergeSort(A2,A)
        # Merge those subarrays
        merge(A,A1,A2,array)
        A.mem(array)
    return array

def merge(A: Analyse,A1,A2,array):
    # Index of subarray1- i,
    # Subarray2- j,
    # Combined array- k

    i = A.ret(0) 
    j = A.ret(0) 
    k = A.ret(0) 
    A.mem(i)
    A.mem(j)
    A.mem(k)

    n1 = A.ret(len(A1))
    n2 = A.ret(len(A2))
    A.mem(n1)
    A.mem(n2)

    # Picks the largest element from the two subarrays
    while A.comparelt(i,n1) and A.comparelt(j,n2): 
        if A.comparelt(A1[i],A2[j]):
            array[k] = A.ret(A1[i])
            i = A.add(i)
        else:
            array[k] = A.ret(A2[j])
            j = A.add(j)
        k = A.add(k)
    
    # Copies the rest of the elements in subarray 1 
    while A.comparelt(i,n1): 
        array[k] = A.ret(A1[i])
        i = A.add(i)
        k = A.add(k)
        
    # Copies the rest of the elements in subarray 2
    while A.comparelt(j,n2): 
        array[k] = A.ret(A2[j])
        j = A.add(j)
        k = A.add(k)