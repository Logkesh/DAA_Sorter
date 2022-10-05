import matplotlib.pyplot as plt
import numpy as np
from Analyser import Analyse
from bucketsort import BucketSort
from quicksort import QuickSort


def CreateAr():
    for size in range(100,100001,100):
        with open("inputs/input_"+str(size)+".txt","w+") as f:
            array = [str(np.random.randint(1,size)) for i in range(size)]
            data = "\n".join(array)
            f.write(data)


def GenerateAr(size = 10):
    with open("inputs/input_"+str(size)+".txt","r") as f:
        array = [int(i.split("\n")[0]) for i in f.readlines()]
        return array

def DoAnalyse(name,func,array):
    A = Analyse()
    print("Sorting Array...")
    A.Timer(func,array)
    print("Array Sorted...")
    A.StoreData(name)

def PlotAnalysis(sorts,group):
    for i in sorts:
        for j in group:
            with open("Analysis/"+i+j+".txt","r") as f:
                data = [float(i) for i in f.read().split(" ")[1:]]
                size = [i for i in range(len(data))]
                plt.ylabel(j.upper())
                plt.xlabel("SIZE (10^2)")
                plt.title(j.upper() + " - " + i)
                plt.plot(size,data)
                plt.show()

def Print_Sorting(array):
    func = {"BucketSort":BucketSort,"QuickSort":QuickSort}
    for i in func.keys():
        print(i," with ",len(array))
        DoAnalyse(i,func[i],array)

def ReadyStorage(sorts, group):
    for i in sorts:
        for j in group:
            with open("Analysis/"+i+j+".txt","w+") as f:
                data = ""
                f.write(data)

def main():
    
    sorts = ["BucketSort","QuickSort"]
    group = ["time","swap","compare","basicop","mem"]
    
    ReadyStorage(sorts,group)
    
    for n in range(100,100001,100):
        array = GenerateAr(n)
        Print_Sorting(array)
    
    PlotAnalysis(sorts,group)
    
if __name__ == "__main__":
    main()