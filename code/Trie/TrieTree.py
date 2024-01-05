from .Node import Node

class TrieTree:
    
    def __init__(self):
        self.word_count = 0
        self.root = Node(is_root=True)
    


    def append_word(self, value):
        search_res = self.search(value)
        if search_res.exists : return
        elif search_res.processed_chars == value : 
            search_res.last_node.is_delimited = True
            return
        current_node = search_res.last_node
        index = len(search_res.processed_chars)
        while index < len(value):
            new_node = Node(value[index],current_node, len(value) == index + 1)
            current_node.append_child(new_node)
            current_node = new_node
            index += 1



    def search(self, value):
        current_node = self.root
        index = 0
        while not current_node.is_leaf and index < len(value):
            child_index = current_node.child_index(value[index])
            if child_index == -1: return TrieTree.SearchResult(False, value[0:index], current_node)
            current_node = current_node.children[child_index]
            if index == len(value) - 1 and current_node.is_delimited:
                return TrieTree.SearchResult(True, value[0:index+1], current_node)
            index += 1
        return TrieTree.SearchResult(False, value[0:index], current_node)



    class SearchResult:
        def __init__(self, exists, processed_chars, last_node) -> None:
            self.exists = exists
            self.processed_chars = processed_chars
            self.last_node = last_node
            