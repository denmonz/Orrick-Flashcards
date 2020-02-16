import Extractor as ex
import question_generator as gen

#Dish sample
#direct_path = ""

#Apple Brief
direct_path = ''

with open(direct_path, 'r') as file:
    brief = file.read()


test = ex.Extractor(brief)
qGen = gen.QuestionGenerator()

sentences = test.get_sentences()

for sentence in sentences:
    flashcard = qGen.generate_question(sentence)
    if flashcard:
        #print(type(flashcard), type(flashcard[0]))
        print("Question: {}\n\nAnswer: {}'\n-------------".format(flashcard[0]['Q'], flashcard[0]['A']))


