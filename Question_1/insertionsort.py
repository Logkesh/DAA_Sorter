from Analyser import Analyse            # User Defined Class to Analyse the Sorting Alogorithm

def InsertionSort(arr, A: Analyse):
    n = A.ret(len(arr))
    A.mem(n)

    # Iterating from 1 to n
    for i in range(1,n): 
        
        min = A.ret(arr[i])
        
        # Previous element to i
        j = A.sub(i)  

        # Takes the elements which are greater than min
        while (A.comparegt(j,0) or A.equate(j,0)) and (A.comparelt(min,arr[j])): 
            
            # Swaps the elements to one position forward
            arr[j+1] = A.ret(arr[j])
            
            j = A.sub(j)
        
        # Keeps the element next to smallest number
        arr[j+1] = A.ret(min) 
    
    return arr