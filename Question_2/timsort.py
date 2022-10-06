from Analyser import Analyse           # User Defined Class to Analyse the Sorting Alogorithm 

def calcMinRun(n):
    
    r = 0
    while n < 32:
        r  |= n & 1
        n >>= 1
    return n + r
 
def InsertionSort(arr, A: Analyse,left,right):
    
    i = A.ret(A.add(left))
    while(i < A.add(right)):
        
        j = A.ret(i)
        while A.comparegt(j,left) and A.comparelt(arr[j], arr[A.sub(j)]):
            arr[j], arr[j - 1] = A.swap(arr[j], arr[A.sub(j)])
            j = A.sub(j)
        i = A.add(i)
 
 
# Merge function merges the sorted runs
def merge(arr, left, mid, right, A: Analyse):
 
    # original array is broken in two parts
    # left and right array
    L1 = A.add(A.sub(mid,left))
    L2 = A.sub(right,mid)
    
    A1 = A.ret(list())
    A2 = A.ret(list())
    
    i = A.ret(0)
    while A.comparelt(i, L1):
        A1.append(arr[A.add(left,i)])
        i = A.add(i)
        
    i = A.ret(0)
    while A.comparelt(i, L2):
        A2.append(arr[A.add(mid,i+1)])
        i = A.add(i)
 
    i = A.ret(0)
    j = A.ret(0)
    k = A.ret(left)
 
    # after comparing, we merge those two array
    # in larger sub array
    while A.comparelt(i, L1) and A.comparelt(j, L2):
        
        if A.comparelt(A1[i], A2[j]) or A.equate(A1[i], A2[j]):
            arr[k] = A.ret(A1[i])
            i = A.add(i)
 
        else:
            arr[k] = A.ret(A2[j])
            j = A.add(j)
 
        k = A.add(k)
 
    # Copy remaining elements of left, if any
    while A.comparelt(i, L1):
        arr[k] = A.ret(A1[i])
        k = A.add(k)
        i = A.add(i)
 
    # Copy remaining element of right, if any
    while A.comparelt(j, L2):
        arr[k] = A.ret(A2[j])
        k = A.add(k)
        j = A.add(j)
 
 
 
def TimSortHelp(arr, A: Analyse):
    n = len(arr)
    minRun = calcMinRun(n)
 
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(A.sub(A.add(start,minRun)), A.sub(n))
        
        InsertionSort(arr, A,start, end)
 
    
    size = A.ret(minRun)
    while A.comparelt(size, n):
 
        left = A.ret(0)
        while A.comparelt(left, n):
            
            mid = min(A.sub(n), A.sub(A.add(left,size)))
            right = min(A.sub(A.add(left,A.mul(2,size))), A.sub(n))
            
            if A.comparelt(mid, right):
                merge(arr, left, mid, right, A)
            
            left = A.add(left,A.mul(size,2))
            
                
 
        size = A.mul(2,size)

def TimSort(array, A: Analyse):
    A.mem(array)
    TimSortHelp(array, A)
    return array
    
	
