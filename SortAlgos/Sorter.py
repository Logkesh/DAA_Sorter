import matplotlib.pyplot as plt
from bucketsort import BucketSort
from quicksort import QuickSort

def GenerateAr(size = 10):
    with open("inputs/input_"+str(size)+".txt","r") as f:
        array = [int(i.split("\n")[0]) for i in f.readlines()]
        return array

def Print_Sorting(array):
    func = {"BucketSort":BucketSort,"QuickSort":QuickSort}
    for i in func.keys():
        print(i," with ",len(array))
        title = i + " with " + str(len(array)) + " Elements"
        print("Sorting Array...")
        PlotGraph(array,title+" Before Sorting")
        res = func[i](array)
        print("Array Sorted...")
        PlotGraph(res,title+" After Sorting")

def PlotGraph(array,title):
    plt.xlabel("Range")
    plt.ylabel("Elements")
    plt.title(title)
    plt.plot(range(len(array)),array)
    plt.show()

def main():
    for i in range(1,6):
        n = 10**i    
        array = GenerateAr(n)
        Print_Sorting(array)
    
if __name__ == "__main__":
    main()