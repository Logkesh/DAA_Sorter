from bucketsort import BucketSort
from quicksort import QuickSort

def GenerateAr(size = 10):
    with open("inputs/input_"+str(size)+".txt","r") as f:
        array = [int(i.split("\n")[0]) for i in f.readlines()]
        return array

def Print_Sorting(array):
    func = [BucketSort,QuickSort]
    for i in func:
        print("Before Sorting...")
        print(array)
        res = i(array)
        print("After Sorting...")
        print(res)

def main():
    array = GenerateAr()
    Print_Sorting(array)
    
if __name__ == "__main__":
    main()