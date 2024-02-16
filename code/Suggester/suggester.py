from statics.paths import *
from Trie.TrieTree import TrieTree as TTree
 
class Suggester:
    MODES = ('ALPHA', 'BETA', 'ALL')
    PATHS = {MODES[0] : ALPHA_NEIGHBORS_PATH, MODES[1] : BETA_NEIGHBORS_PATH, MODES[2] : ALL_NEIGHBORS_PATH}
    def __init__(self, mode) -> None:
        self.mode = mode
        if mode not in Suggester.MODES:
            raise ValueError(f'mode must be one of the modes specified in the MODES list Options are : {Suggester.MODES}')
        self._neighbors_path = Suggester.PATHS[self.mode]
        self._neighbors = None
        self.load_raw_neighbors()
        self.word_set = None
        self.load_raw_dataset()
        print()


    def load_raw_neighbors(self):
        self._neighbors = dict()
        with open(self._neighbors_path.absolute(), 'r') as file:
            for line in file:
                separated = line.strip().split(' ')
                main_char = separated[0]
                separated.remove(main_char)
                self._neighbors[main_char] = separated
    
    def load_raw_dataset(self):
        self.word_set = TTree()
        with open(WORD_SET_PATH, 'r') as file:
            for line in file:
                self.word_set.append_word(line.strip())