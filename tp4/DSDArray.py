import math
import DSD
class DSDArray (DSD.DSD):
    def __init__(self,graph,start):
        self.__array=dict()
        super().__init__(graph,start) 

        
        
    def insert(self, node, distance):
        self.__array[node]=distance
        
    def extract_min(self):
        print(self.__array)
        assert (len(self.__array)>0)
        minimum =math.inf
        res=0
        for key in self.__array:
            if( self.__array[key] < minimum):
                minimum=self.__array[key]
                res=key
        resf =(res,minimum)
        del(self.__array[res])
        return resf

        


        
    def decrease(self, node, distance):

        if  node in self.__array and distance<self.__array[node] :
            self.__array[node]=distance
            
    def is_empty(self):
        return len(self.__array)==0
    
    def __str__(self):
        return ""