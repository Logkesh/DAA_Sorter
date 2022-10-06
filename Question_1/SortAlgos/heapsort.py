from Analyser import Analyse            # User Defined Class to Analyse the Sorting Alogorithm

# Heap Class
class Heap:
    def _init_(self,A: Analyse):
        
        # Temporary list to store elements
        self.heapList = A.ret(list()) 

        self.currentSize = A.ret(0)

    # Moves the new element down the heap
    def downheap(self,i,A: Analyse):    

        while A.comparelt(A.mul(i,2),self.currentSize) or A.equate(A.mul(i,2),self.currentSize): 
            mc = A.ret(self.minChild(i,A))

            # Swaping the minimum element
            if A.comparegt(self.heapList[i],self.heapList[mc]):

                self.heapList[i],self.heapList[mc] = A.swap(self.heapList[i],self.heapList[mc])

            i = A.ret(mc)

    # Finds the minimum child
    def minChild(self,i,A: Analyse): 
        if A.comparegt(A.add(A.mul(i,2)),self.currentSize):
            return A.ret(A.mul(i,2))
        else:
            if A.comparelt(self.heapList[A.mul(i,2)],self.heapList[A.add(A.mul(i,2))]):
                return A.ret(A.mul(i,2))
            else:
                return A.ret(A.add(A.mul(i,2)))

    # Deletes the minimum element from the root node appends into resultant list
    def delMin(self,A: Analyse): 
        retval = A.ret(self.heapList[1])
        A.mem(retval)
        self.heapList[1] = A.ret(self.heapList[self.currentSize])
        self.currentSize = A.sub(self.currentSize)
        self.heapList.pop()
        self.downheap(1,A)
        return A.ret(retval)
    
    # Heapify's the heap
    def buildHeap(self,alist,A: Analyse): 
        i = A.divf(len(alist),2)
        self.currentSize = A.ret(len(alist))
        self.heapList = A.ret([0] + alist[:])
        while A.comparegt(i,0):  
            self.downheap(i,A)
            i = A.sub(i)

# Heap Sort Function
def HeapSort(arr: list, A: Analyse) -> list: 
    heap = Heap()
    arraySize = len(arr)

    A.mem(arraySize)
    A.mem(arr)
    
    # Heapify's the given array
    heap.buildHeap(arr,A) 
    A.mem(heap)
    
    # Final list to store ordered elements
    res = A.ret(list())
    A.mem(res)

    for _ in range(0,arraySize): 
        
        # Deleting the min element and appending into new list
        res.append(heap.delMin(A))


    return res

