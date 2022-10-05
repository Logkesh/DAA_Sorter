#HeapSort
class Heap:
    def __init__(self):
        self.heapList = [] #temporary list to store elements 
        self.currentSize = 0
        self.mini=[] # final list to store ordered elements

    def downheap(self,i):    #moves the new element down the heap
        while (i * 2) <= self.currentSize: 
            mc = self.minChild(i) 
            if self.heapList[i] > self.heapList[mc]: #swap the minimum element
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i): #finds the minimum child
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self): # deletes the minimum element from the root node
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.downheap(1)
        return retval
    
    def buildHeap(self,alist): #Heapify's the heap
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):  
            self.downheap(i)
            i = i - 1
    
    def HeapSort(self,arr): #sorting using heap
        arraySize = len(arr)
        self.buildHeap(arr) #heapify's the given array
        for i in range(0,arraySize): 
            x=self.delMin()
            self.mini.append(x) #deleting the min element and appending into new list       
        return self.mini
    
    def printHeap(self): #prints the elements in the initial heap
        print(self.heapList)

def main():
    heap = Heap()
    arr = list(map(int, input().split()))
    print(heap.HeapSort(arr))
    
if __name__ == '__main__':
    main() 

