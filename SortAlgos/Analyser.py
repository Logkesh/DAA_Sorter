import time
from sys import getsizeof 
import matplotlib.pyplot as plt
class Analyse:
    def __init__(self):
        self.Ctime = 0
        self.Cswaps = 0
        self.Ccompare = 0
        self.Cbasicop = 0
        self.Cmemory = 0
    
    def Timer(self,func,array):
        
        a = time.time()
        func(array,A = self)
        b = time.time()
        
        self.Ctime = b - a
    
    def mem(self,obj):
        self.Cmemory += getsizeof(obj)

    def comparegt(self,a,b):
        self.Ccompare += 1
        return a > b
    
    def comparelt(self,a,b):
        self.Ccompare += 1
        return a < b
    
    def equate(self,a,b):
        self.Ccompare += 1
        return a == b
    
    def swap(self,a,b):
        self.Cswaps += 1
        return b,a
    
    def add(self,a,b=1):
        self.Cbasicop += 1
        return a + b
    
    def sub(self,a,b=1):
        self.Cbasicop += 1
        return a - b
    
    def mul(self,a,b=1):
        self.Cbasicop += 1
        return a * b
    
    def div(self,a,b = 1):
        self.Cbasicop += 1
        return a / b
    
    def ret(self,a):
        self.Cbasicop += 1
        return a
    
    def StoreData(self,sort):
        def HelpToStore(sort,group,attr):
            with open("Analysis/"+sort+group+".txt","r+") as f:
                data = f.read()
            with open("Analysis/"+sort+group+".txt","w+") as f:
                data += " " + str(attr)
                f.write(data)
        
        group = [("time",self.Ctime),
                 ("swap",self.Cswaps),
                 ("compare",self.Ccompare),
                 ("basicop",self.Cbasicop),
                 ("mem",self.Cmemory)]
        for g,a in group:
            HelpToStore(sort, g, a)
            
    
    def PlotGraph(self,array,title):
        plt.xlabel("Index")
        plt.ylabel("Elements")
        plt.title(title)
        plt.plot(range(len(array)),array)
        plt.show()
    

    
        
    
