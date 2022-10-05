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
