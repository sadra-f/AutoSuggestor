An attempt to create an english word suggestion model that takes closeness of keys on the keyboard into consideration while suggesting words.

The model uses the levenshtein algorithm and a set of neighboring characters.

dataset source: [https://github.com/dwyl/english-words](https://github.com/dwyl/english-words)

The main idea is that when trying to write a word such as "he" and you mistakenly type "h3", considering the fact that on the keyboard, the key for 'e' and the key for '3' are close. the program will try to suggest correct words for such mistakes.