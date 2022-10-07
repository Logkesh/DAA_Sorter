import matplotlib.pyplot as plt         # For Displaying results in graphs
import numpy as np                      # To Generate Random Inputs 

from Analyser import Analyse            # User Defined Class to Analyse the Sorting Algorithm 

from updatedquicksort import Updated_QuickSort         # Updated Quick Sort Function
from timsort import TimSort                   # Tim Sort Function

# Creates an array with shuffeled random numbers
# Used to create input files
def CreateAr():

    # Generating random arrays from size 100 to size 75000 with the interval value of 100 
    for size in range(100,20001,100):
        
        # Opening the file in write mode
        with open("../inputs/input_"+str(size)+".txt","w+") as f:
            
            # Generating the random data and storing into array
            array = [str(np.random.randint(1,size)) for i in range(size)]
            
            # Converting into string
            data = "\n".join(array)
            
            # Storing into file
            f.write(data)

# Fetches input data from stored files
def GenerateAr(size = 10):
    
    # Opening the file in read mode
    with open("../inputs/input_"+str(size)+".txt","r") as f:  

        # Fetching the data from the file and storing into array
        array = [int(i.split("\n")[0]) for i in f.readlines()] 

        return array

# Executes and Anylse the sorting program 
# and stores the analysed information into the specified files
def DoAnalyse(name,func,array):
    
    # Creating the object of the class Analyse
    A = Analyse()

    print("Sorting Array...")
    
    # Executing the function and invoking the timer
    A.Timer(func,array)
    
    print("Array Sorted...")
    
    # Storing the data into file
    A.StoreData(name)

# Plots and Display the Analysed info as a graph
def PlotAnalysis(sorts,group):
    # Ploting for different combinations of Analysed features and Sorts
    for i in sorts:
        for j in group:

            # Opening a file in read mode
            with open("Analysis/"+i+j+".txt","r") as f:

                # Fetching the data  from the file and measuring the size
                data = [float(i) for i in f.read().split(" ")[1:]]
                size = range(len(data))
                
                # Naming the label and title for the plots
                plt.ylabel(j.upper())
                plt.xlabel("SIZE (10^2)")
                
                plt.title(j.upper() + " - " + i)
                
                # Ploting and displaying the data as graph 
                plt.plot(size,data)
                plt.show()

# Executes the sorting Algos and Prints the status of the sorting
def Print_Sorting(array,func: dict):
    # Analysing the different Algorithms
    for i in func.keys():
        print(i," with ",len(array))
        DoAnalyse(i,func[i],array)

# Makes the files ready before the program executes
def ReadyStorage(sorts, groups):
    for sort in sorts:
        for group in groups:
            # Opening the file in write mode
            with open("Analysis/" + sort + group + ".txt","w+") as f:
                
                data = ""
                f.write(data)

# Tests the performance of the sorting Algorithms by using plots
def Sort_Testing(func,sort,size = 200):
    arr = GenerateAr(size)
    for i in sort:
        
        print(i)
        # Array Before Sorting
        plt.title(i + "Before Sorting")
        print("Array Before Sorting:",arr)
        plt.xlabel("INDEX")
        plt.ylabel("Elements")
        plt.plot(range(size), arr)
        plt.show()
        
        # Sorting the array
        res = func[i](arr.copy(),Analyse())
        
        # Array After Sorting 
        plt.title(i + "After Sorting")
        print("Sorted Array:",res)
        plt.xlabel("INDEX")
        plt.ylabel("Elements")
        plt.plot(range(size), res)
        plt.show()
    
# The Main Driver Function
def main():
    
    # Sorting functions and analysed features
    func = {"QuickSort":Updated_QuickSort,"TimSort":TimSort}
    group = ["time","swap","compare","basicop","mem"]
    sort = list(func.keys())
    
    # Testing the Algorithms using sample data before execution
    Sort_Testing(func,sort)
    
    
    # invoking all funtions
    ReadyStorage(sort,group)
    
    for n in range(100,20001,100):
        array = GenerateAr(n)
        Print_Sorting(array,func)
    
    PlotAnalysis(sort,group)

    
if __name__ == "__main__":
    main()