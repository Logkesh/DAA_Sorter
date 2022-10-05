import time                         # For Calculating time
from sys import getsizeof           # For Calculating size of the objects
import matplotlib.pyplot as plt     # For Displaying Analysis in graphs

# Class to Analyse the following parameters of the sorting algorithms 
# Time Taken
# Space occupied
# Number of Swaps
# Number of Comparisons
# Number of Basic Operations
class Analyse:

    # Initializing the Parameters
    def __init__(self):
        self.Ctime = 0
        self.Cswaps = 0
        self.Ccompare = 0
        self.Cbasicop = 0
        self.Cmemory = 0
    
    # Calcualtes the Time Taken of the Algorithm
    def Timer(self,func,array):
        # Start time
        a = time.time()
        func(array,A = self)
        # End time
        b = time.time()
        # Time Taken
        self.Ctime = b - a
    
    # Calculates the Space consumed
    def mem(self,obj):
        self.Cmemory += getsizeof(obj)

    # Calcutes Number of '>' comparisons
    def comparegt(self,a,b):
        self.Ccompare += 1
        return a > b
    
    # Calcutes Number of '<' comparisons
    def comparelt(self,a,b):
        self.Ccompare += 1
        return a < b
    
    # Calcutes Number of equality comparisons
    def equate(self,a,b):
        self.Ccompare += 1
        return a == b
    
    # Calcutes Number of Swaps
    def swap(self,a,b):
        self.Cswaps += 1
        return b,a
    
    # Calcutes Number of addition Operations (Basic)
    def add(self,a,b=1):
        self.Cbasicop += 1
        return a + b
    
    # Calcutes Number of subraction Operations (Basic)
    def sub(self,a,b=1):
        self.Cbasicop += 1
        return a - b
    
    # Calcutes Number of multiplication Operations (Basic)
    def mul(self,a,b=1):
        self.Cbasicop += 1
        return a * b
    
    # Calcutes Number of division Operations (Basic)
    def div(self,a,b = 1):
        self.Cbasicop += 1
        return a / b
    
    # Calcutes Number of return or assignment Operations (Basic)
    def ret(self,a):
        self.Cbasicop += 1
        return a
    
    # Stores the data in file
    def StoreData(self,sort):
        def HelpToStore(sort,group,attr):
            
            # Reads the data
            with open("Analysis/"+sort+group+".txt","r+") as f:
                data = f.read()
            
            # Writes the data
            with open("Analysis/"+sort+group+".txt","w+") as f:
                data += " " + str(attr)
                f.write(data)
        
        # List of parameters and respective attributes
        group = [("time",self.Ctime),
                 ("swap",self.Cswaps),
                 ("compare",self.Ccompare),
                 ("basicop",self.Cbasicop),
                 ("mem",self.Cmemory)]
        for g,a in group:
            HelpToStore(sort, g, a)
            
    # Ploting Graph
    def PlotGraph(self,array,title):
        plt.xlabel("Index")
        plt.ylabel("Elements")
        plt.title(title)
        plt.plot(range(len(array)),array)
        plt.show()
    

    
        
    
