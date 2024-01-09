import numpy as np
class Node:
    
    def __init__(self, value=None, parent=None, delimited=False, children=np.empty((0,), object), is_root=False):
        self.value = value if not is_root else ''
        self.is_word = delimited
        self.children = children
        self.is_root = is_root
        self.parent = parent
        if not is_root and self.value == None: raise ValueError
    
    def exist_by_value(self, value):
        try:
            return True if self.index_by_value(value) > -1 else False
        except ValueError:
            return False
            
    def append_child(self, value):
        self.children = np.append(self.children, value)

    def index_by_value(self, value):
        try:
            for i in range(len(self.children)):
                if self.children[i].value == value:
                    return i
            return -1
        except ValueError:
            return -1
        
    def remove_child(self, child):
        self.remove_child_by_value(child.value)

    def remove_child_by_value(self, value):
        child_index = self.index_by_value(value)
        if child_index < 0 : return
        self.children = np.delete(self.children, child_index)
        return

    @property
    def has_any_child(self):
        return self.children.size > 0

    @property
    def is_leaf(self):
        return not self.has_any_child and not self.is_root
    

    def __str__(self):
        return f"{self.value}, {self.children}, {self.is_leaf}"
    
    def __repr__(self) -> str:
        return self.__str__()