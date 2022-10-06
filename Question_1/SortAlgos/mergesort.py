<<<<<<< HEAD:Question_1/SortAlgos/mergesort.py
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
=======
#mergesort
def MergeSort(A):
    n=len(A)
    if (n<2):
        return A
    else:
        mid = n//2
        A1=A[:mid] #declaring half of the array as A1
        A2=A[mid:] #declaring the remaining half as A2
        mergesort(A1) #recursive call for sorting subarray 1 & 2
        mergesort(A2)
        merge(A1,A2,A)
    return A

def merge(A1,A2,A):
    i=j=k=0 #index of subarray1- i, subarray2- j,combined array- k
    n=len(A)
    n1=len(A1)
    n2=len(A2)
    while(i < n1 and j < n2): #picks the largest element from the two subarrays
        if A1[i] < A2[j]:
            A[k] = A1[i]
            i+=1
        else:
            A[k] = A2[j]
            j+=1
        k+=1
        
    while i < n1: #copies the rest of the elements in subarray 1 
        A[k] = A1[i]
        i +=1
        k +=1
        
    while j < n2: #copies the rest of the elements in subarray 2
        A[k] = A2[j]
        j +=1    
        k +=1

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(MergeSort(arr))
>>>>>>> 7b60bd3591363a8ef22acabdc70996cdc4b38e07:SortAlgos/mergesort.py
