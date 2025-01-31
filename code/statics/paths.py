from pathlib import Path
#================================================================================================

_BETA_NEIGHBORS_STR_PATH = 'code/statics/neighbors_beta.txt'
_ALPHA_NEIGHBORS_STR_PATH = 'code/statics/neighbors_alpha.txt'
_ALL_NEIGHBORS_STR_PATH = 'code/statics/neighbors_all.txt'
_ALL_WORD_SET_STR_PATH = 'dataset/words.txt'
_ALPHA_WORD_SET_STR_PATH = 'dataset/words_alpha.txt'

_PICKLED_ALPHA_WORD_SET_STR_PATH =  'dataset/pickled_alpha_words'
_PICKLED_WORD_SET_STR_PATH =  'dataset/pickled_words'
#================================================================================================

BETA_NEIGHBORS_PATH = Path(_BETA_NEIGHBORS_STR_PATH)
ALPHA_NEIGHBORS_PATH = Path(_ALPHA_NEIGHBORS_STR_PATH)
ALL_NEIGHBORS_PATH = Path(_ALL_NEIGHBORS_STR_PATH)
ALL_WORD_SET_PATH = Path(_ALL_WORD_SET_STR_PATH)
ALPHA_WORD_SET_PATH = Path(_ALPHA_WORD_SET_STR_PATH)

PICKLED_ALPHA_WORD_SET_PATH = Path(_PICKLED_ALPHA_WORD_SET_STR_PATH)
PICKLED_WORD_SET_PATH = Path(_PICKLED_WORD_SET_STR_PATH)