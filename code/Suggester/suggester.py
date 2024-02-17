from statics.paths import *
from Trie.TrieTree import TrieTree as TTree
from distance.Levenshtein import LevenshteinDistance as LD
import pickle


class Suggester:
    
    SUGGESTION_MODES = ('ALPHA', 'BETA', 'ALL')
    NEIGHBOR_PATHS = {SUGGESTION_MODES[0] : ALPHA_NEIGHBORS_PATH, SUGGESTION_MODES[1] : BETA_NEIGHBORS_PATH, SUGGESTION_MODES[2] : ALL_NEIGHBORS_PATH}

    DATASET_MODES = ('ALL', "ALPHA")
    DATASET_PATHS = {DATASET_MODES[0] : ALL_WORD_SET_PATH, DATASET_MODES[1] : ALPHA_WORD_SET_PATH}
    PICKLE_PATHS = {DATASET_MODES[0] : PICKLED_WORD_SET_PATH, DATASET_MODES[1] : PICKLED_ALPHA_WORD_SET_PATH}

    MAX_SUGGESTION_COUNT = 8

    def __init__(self, mode:str, dataset_mode:str) -> None:
        self.mode = mode

        if mode not in Suggester.SUGGESTION_MODES:
            raise ValueError(f'mode must be one of the modes specified in the MODES list Options are: {Suggester.SUGGESTION_MODES}')
        self._neighbors = None
        
        self.load_raw_neighbors()

        self._dataset_mode = dataset_mode
        if self._dataset_mode not in Suggester.DATASET_MODES:
            raise ValueError(f'dataset mode must be one of the modes specified in the DATASET_MODES list, Options are: {Suggester.DATASET_MODES}')
        self.tt = None # Trie Tree of words in dataset

        self.load_pickled_dataset()


    def load_raw_neighbors(self):
        self._neighbors = dict()
        with open(Suggester.NEIGHBOR_PATHS[self.mode], 'r') as file:
            for line in file:
                separated = line.strip().split(' ')
                main_char = separated[0]
                separated.remove(main_char)
                self._neighbors[main_char] = separated
    
    def load_raw_dataset(self):
        self.tt = TTree()
        with open(Suggester.DATASET_PATHS[self._dataset_mode], 'r') as file:
            for line in file:
                self.tt.append_word(line.strip())


    def save_pickled_dataset(self):
        with open(Suggester.PICKLE_PATHS[self._dataset_mode], 'wb') as file:
            pickle.dump(self.tt, file, 4)
    
    def load_pickled_dataset(self):
        with open(Suggester.PICKLE_PATHS[self._dataset_mode], 'rb') as file:
            self.tt = pickle.load(file)


    def make_suggestion(self, word:str):
        if len(word) < 2: raise ValueError

        if self.tt.search(word).exists:
            return self.tt.search_conditional(word, max_length=len(word)+1, max_count=Suggester.MAX_SUGGESTION_COUNT)
        
        #check variations
        suggestions = []
        tmp_word = word
        for character in self._neighbors[word[-1]]:
            tmp_word = tmp_word[:-1] + character
            if self.tt.search(tmp_word).exists:
                suggestions.append((tmp_word, LD.calculateDistance(word, tmp_word)[0]))

        if len(suggestions) > 0 : 
            suggestions = sorted(suggestions, key=lambda x: x[1])[:Suggester.MAX_SUGGESTION_COUNT]
            return suggestions
        
        tmp_sug = self.tt.search_conditional(word[:-1], min_length= len(word)-1, max_length= len(word) + 1)
        for sug in tmp_sug:
            suggestions.append((sug, LD.calculateDistance(sug, word)[0]))
        suggestions = sorted(suggestions, key=lambda x: x[1])[:Suggester.MAX_SUGGESTION_COUNT]
        return suggestions