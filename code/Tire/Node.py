class Node:
    def __init__(self, value=None, delimited=False, children=[], is_leaf=True):
        self.value = value
        self.is_delimited = delimited
        self.children = children
        self.is_leaf = is_leaf
    
    
    def have_child(self, value):
        try:
            return True if self.children.index(value) else False
        except ValueError:
            return False
            
            

    def child_index(self, value):
        try:
            return self.children.index(value)
        except ValueError:
            return -1