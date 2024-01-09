from .Node import Node

class TrieTree:
    
    def __init__(self):
        self.word_count = 0
        self.root = Node(is_root=True)
    


    def append_word(self, value):
        search_res = self.search(value)

        if search_res.exists : return
        elif search_res.processed_chars == value : 
            search_res.last_node.is_word = True
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
            child_index = current_node.index_by_value(value[index])

            if child_index == -1: return TrieTree.SearchResult(False, value[0:index], current_node)

            current_node = current_node.children[child_index]
            if index == len(value) - 1 and current_node.is_word:
                return TrieTree.SearchResult(True, value[0:index+1], current_node)
            index += 1

        return TrieTree.SearchResult(False, value[0:index], current_node)


    def remove_word(self, value):
        search_res = self.search(value)
        if not search_res.exists : return
        rev_val = value[::-1]
        current_node = search_res.last_node
        current_node.is_word = False
        while not (current_node.is_word or current_node.has_any_child or current_node.is_root) :
            current_node.parent.remove_child_by_value(rev_val[0])
            current_node = current_node.parent
            rev_val = rev_val[1:]
            
            
    def search_starts_with(self, value:str):
        search_res = self.search(value)
        results = []
        if value != search_res.processed_chars : return results
        stack = []
        # (node, str_until_node)
        stack.append((search_res.last_node, value[:-1]))
        while len(stack) > 0:
            popped = stack.pop()
            current_str = popped[1] + popped[0].value
            if popped[0].is_word : results.append(current_str)
            for child in popped[0].children:
                stack.append((child, current_str))
        return results


    class SearchResult:
        def __init__(self, exists:bool, processed_chars:str, last_node:Node) -> None:
            self.exists = exists
            self.processed_chars = processed_chars
            self.last_node = last_node
            