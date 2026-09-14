from typing import Self
import math

class Vec :
    def __init__(self, src = None) -> Self:
        if src is None :
            self.elements = ()
        else :
            elements = tuple(src)
            for x in elements :
                if not isinstance(x,(int, float)):
                    print(f"THE INPUT MUST BE A SCALAR")
            self.elements = elements
    
    def __repr__(self):
        return repr(self.elements)
    
    def __len__(self):
        return len(self.elements)
    def mean(self) :
        return (sum(self.elements) / len(self.elements))
    
    def demean(self) :
        m = self.mean()
        return Vec(x - m for x in self.elements )
    
    def std(self) :
        dm = self.demean()
        # print(f"VECTOR INSIDE STD : ",self)
        # print(f"DEMEAN INSIDE STD : ",dm)
        return math.sqrt(sum(x * x for x in dm.elements)/len(dm))
    
