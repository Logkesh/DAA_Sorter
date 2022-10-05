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
