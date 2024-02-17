from Suggester.suggester import Suggester


suggester = Suggester(Suggester.SUGGESTION_MODES[0], Suggester.DATASET_MODES[1])

while True:
    inp = input("word: ")
    print(suggester.make_suggestions(inp))