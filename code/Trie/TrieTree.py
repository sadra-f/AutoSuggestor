from .Node import Node

class TrieTree:
    
    def __init__(self):
        self.word_count = 0
        self._abs_word_count = 0
        self.root = Node(is_root=True)
    


    def append_word(self, value):
        """adds a word to the tree if it is not already there

        Args:
            value (str): the word to add if not already there
        """
        search_res = self.search(value)

        if search_res.exists : return
        elif search_res.processed_chars == value : 
            search_res._last_node.is_word = True
            self.word_count += 1
            self._abs_word_count += 1
            return
        
        current_node = search_res._last_node
        index = len(search_res.processed_chars)
        while index < len(value):
            new_node = Node(value[index],current_node, len(value) == index + 1)
            current_node.append_child(new_node)
            current_node = new_node
            index += 1
        self._abs_word_count += 1
        self.word_count += 1



    def search(self, value):
        """searches for the given word in the tree returns a result obj

        Args:
            value (str): the string to search for

        Returns:
            TrieTree.SearchResult: a tuple with the first value being T/F if 
            the string was found/not found and the second value is 
            the portion of the string that was found and the third value is the last node visited.
        """
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
        """removes a word from the tree if it exists. 
           if there are other words that contain given
           word the given word will be set to not be considered as a word

        Args:
            value (str): the string/word that will be removed
        """
        search_res = self.search(value)
        if not search_res.exists : return
        rev_val = value[::-1]
        current_node = search_res._last_node
        current_node.is_word = False
        while not (current_node.is_word or current_node.has_any_child or current_node.is_root) :
            current_node.parent.remove_child_by_value(rev_val[0])
            current_node = current_node.parent
            rev_val = rev_val[1:]
        self.word_count -= 1
            
            
    def search_starts_with(self, value:str):
        """find words in tree that start with the given string

        Args:
            value (str): string to look for in the beginning of the words

        Returns:
            list[str]: returns the list of words that start with the given string
        """
        search_res = self.search(value)
        results = []
        if value != search_res.processed_chars : return results
        stack = []
        # (node, str_until_node)
        stack.append((search_res._last_node, value[:-1]))
        while len(stack) > 0:
            popped = stack.pop()
            current_str = popped[1] + popped[0].value
            if popped[0].is_word : results.append(current_str)
            for child in popped[0].children:
                stack.append((child, current_str))
        return results

    def search_conditional(self, start_With:str, end_With:str=None, min_length:int=None, max_length:int=None):
        if start_With is None: raise ValueError

        search_res = self.search(start_With)
        results = []
        if start_With != search_res.processed_chars : return results
        stack = []
        # (node, str_until_node)
        stack.append((search_res._last_node, start_With[:-1]))
        while len(stack) > 0:
            popped = stack.pop()
            current_str = popped[1] + popped[0].value
            if popped[0].is_word : 
                do_append = True
                if end_With is not None:
                    if current_str[-len(end_With):] != end_With: do_append = False
                if min_length is not None:
                    if len(current_str) < min_length : do_append = False
                if max_length is not None:
                    if len(current_str) > max_length : do_append = False
                if do_append : 
                    results.append(current_str)
            for child in popped[0].children:
                stack.append((child, current_str))
        return results

    class SearchResult:
        """A class to contain the results of a search

            exists: True if the search resulted in finding the exact given word, False otherwise
            processed_chars: the portion of the queried string that was processed/found
            last_node: the last node visited
        """
        def __init__(self, exists:bool, processed_chars:str, last_node:Node) -> None:
            self.exists = exists
            self.processed_chars = processed_chars
            self._last_node = last_node
            