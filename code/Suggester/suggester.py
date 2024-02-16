from statics.paths import *
from Trie.TrieTree import TrieTree as TTree
from distance.Levenshtein import LevenshteinDistance as LD
import pickle


class Suggester:
    
    SUGGESTION_MODES = ('ALPHA', 'BETA', 'ALL')
    NEIGHBOR_PATHS = {SUGGESTION_MODES[0] : ALPHA_NEIGHBORS_PATH, SUGGESTION_MODES[1] : BETA_NEIGHBORS_PATH, SUGGESTION_MODES[2] : ALL_NEIGHBORS_PATH}
    DATASET_MODES = ('ALL', "ALPHA")
    DATASET_PATHS = {DATASET_MODES[0] : ALL_WORD_SET_PATH, DATASET_MODES[1] : ALPHA_WORD_SET_PATH}
    PICKLE_PATHS = {DATASET_MODES[0] : PICKLED_ALPHA_WORD_SET_PATH, DATASET_MODES[1] : PICKLED_ALPHA_WORD_SET_PATH}
    
    def __init__(self, mode:str, dataset_mode:str) -> None:
        #TODO : remove load methods and maybe add another method to do that ***
        self.mode = mode
        if mode not in Suggester.SUGGESTION_MODES:
            raise ValueError(f'mode must be one of the modes specified in the MODES list Options are: {Suggester.SUGGESTION_MODES}')
        self._neighbors_path = Suggester.NEIGHBOR_PATHS[self.mode]
        self._neighbors = None
        self.load_raw_neighbors()

        self._dataset_mode = dataset_mode
        if self._dataset_mode not in Suggester.DATASET_MODES:
            raise ValueError(f'dataset mode must be one of the modes specified in the DATASET_MODES list, Options are: {Suggester.DATASET_MODES}')
        self.word_set = None
        self.load_pickled_dataset()
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
        with open(Suggester.DATASET_PATHS[self._dataset_mode], 'r') as file:
            for line in file:
                self.word_set.append_word(line.strip())


    def save_pickled_dataset(self):
        with open(Suggester.PICKLE_PATHS[self.mode], 'wb') as file:
            pickle.dump(self.word_set, file, 4)
    
    def load_pickled_dataset(self):
        with open(Suggester.PICKLE_PATHS[self.mode], 'rb') as file:
            self.word_set = pickle.load(file)


    def make_suggestion(self, word):
        pass