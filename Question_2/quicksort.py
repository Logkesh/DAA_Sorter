from Analyser import Analyse        # User Defined Class to Analyse the Sorting Alogorithm 

# A.mem is a function is used to calculate the size of the object 

# The Partition funtion which swaps elements with respect to left most element of the portion of array (In Place)
# And returns new pivot
def Partition(array: list, left: int, right: int,A: Analyse):
    A.mem(left)
    A.mem(right)
    
    # Pointer pointing to the left most element 
    i = left - 1
    A.mem(i)
    
    # The Right most value of the array as pivot (In Place)
    pivot = A.ret(array[right])
    A.mem(pivot)
    
    # Loop from left to right part of the array
    x = A.ret(left)
    A.mem(x)
    
    while A.comparelt(x, right):
        
        # Comparing the array value with the pivot value
        if A.comparelt(array[x],pivot) or A.equate(array[x], pivot):
            # Updating the pointer
            i = A.add(i)
            # Swaping the elements if teh condition is true
            array[i],array[x] = A.swap(array[i],array[x])
        
        x = A.add(x)
    
    # Placing the right most value at its corresponding place
    array[i+1],array[right] = A.swap(array[A.add(i)],array[right])
    
    return A.add(i)   

# Base Recursive Quicksort function which do actual partition and sorting through recursion 
def QuickSort(array: list, A: Analyse, left = 0, right = None) -> list:
    
    A.mem(array)
    
    if right is None: right = A.sub(len(array))
    
    # Comparing the left and right pointer
    if(A.comparelt(left, right)):
        #Partitioning the array and gaining the new pivot value
        pivot = Partition(array, left, right, A)

        # Quick Sort for left sub array
        QuickSort(array,A,left,A.sub(pivot))
        # Quick Sort for right sub array 
        QuickSort(array,A,A.add(pivot),right)
    
    return A.ret(array)
