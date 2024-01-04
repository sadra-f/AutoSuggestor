import numpy as np
class Node:
    
    def __init__(self, value=None, delimited=False, children=np.empty((0,), object), is_root=False):
        self.value = value
        self.is_delimited = delimited
        self.children = children
        self.is_root = is_root
        if not is_root and self.value == None: raise ValueError
    
    def have_child(self, value):
        try:
            return True if self.child_index(value) > -1 else False
        except ValueError:
            return False
            
    def append_child(self, value):
        self.children = np.append(self.children, value)

    def child_index(self, value):
        try:
            for i in range(len(self.children)):
                if self.children[i].value == value:
                    return i
            return -1
        except ValueError:
            return -1
        
    @property
    def is_leaf(self):
        return self.children.size == 0 and not self.is_root
    

    def __str__(self):
        return f"{self.value}, {self.children}, {self.is_leaf}"
    
    def __repr__(self) -> str:
        return self.__str__()