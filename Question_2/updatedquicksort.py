from Analyser import Analyse        # User Defined Class to Analyse the Sorting Alogorithm 

# A.mem is a function is used to calculate the size of the object 

# An Updated Quick Sort Function which runs quick sort algorithm to threshhold point in the array
# and runs an insertion sort for smaller sub arrays
def Updated_QuickSort(array, A: Analyse):

    # Threshhold value is defined as the 1/3 of the total array length
    THRESHHOLD = A.divf(len(array),3)

    # Calling actual Quick Sort
    return A.ret(QuickSort(array,THRESHHOLD,A))

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
def QuickSort(array: list,THRESHOLD: int, A: Analyse, left = 0, right = None) -> list:
    
    A.mem(array)
    
    if right is None: right = A.sub(len(array))
    
    # Comparing the left and right pointer
    if (A.sub(right,left) > THRESHOLD):
        # Partitioning the array and gaining the new pivot value
        pivot = Partition(array, left, right, A)

        # Quick Sort for left sub array
        QuickSort(array,THRESHOLD,A,left,A.sub(pivot))
        # Quick Sort for right sub array 
        QuickSort(array,THRESHOLD,A,A.add(pivot),right)
    
    elif (A.comparelt(left,right)):
        # Insertion Sort

        # Iterating from 1 to n
        for i in range(left,right+1): 
            
            min = A.ret(array[i])
            
            # Previous element to i
            j = A.sub(i)  

            # Takes the elements which are greater than min
            while (A.comparegt(j,left) or A.equate(j,left)) and (A.comparelt(min,array[j])): 
                
                # Swaps the elements to one position forward
                array[j+1] = A.ret(array[j])
                j = A.sub(j)
            
            # Keeps the element next to smallest number
            array[j+1] = A.ret(min) 
            
    return A.ret(array)
