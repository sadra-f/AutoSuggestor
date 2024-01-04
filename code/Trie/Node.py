class Node:
    
    def __init__(self, value=None, delimited=False, children=[], is_root=False):
        self.value = value
        self.is_delimited = delimited
        self.children = children
        self.is_root = is_root
    
    def have_child(self, value):
        try:
            return True if self.children.index(value) > -1 else False
        except ValueError:
            return False
            
            

    def child_index(self, value):
        try:
            for i in range(len(self.children)):
                if self.children[i] == value:
                    return i
            return -1
        except ValueError:
            return -1
        
    @property
    def is_leaf(self):
        return len(self.children) == 0 and not self.is_root