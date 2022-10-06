<<<<<<< HEAD:Question_1/SortAlgos/insertionsort.py
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
        
=======
#insertionsort
def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n): #iterating from 1 to n
        min = arr[i]
        j = i-1 #previous element to i 
        while j >= 0 and max < arr[j]: #takes the elements which are greater than min
            arr[j+1] = arr[j] # swaps the elements to one position forward
            j -= 1
        arr[j+1] = min #keeps the element next to smallest number
    return arr
        
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(InsertionSort(arr))
>>>>>>> 7b60bd3591363a8ef22acabdc70996cdc4b38e07:SortAlgos/insertionsort.py
