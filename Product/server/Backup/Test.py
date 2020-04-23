import Extractor as ex
import question_generator as gen

# To speed up script, start servers:
##bash runStanfordParserServer.sh
##bash runSSTServer.sh



#Dish sample
#direct_path = "/Users/brandon/Documents/Northwestern Courses/Winter 2019/CS+Law Innovation Lab/Orrick, Harrington, & Sutcliffe/Documents/Dish_Sample.txt"

#Apple Brief
direct_path = '/Users/brandon/Documents/Northwestern Courses/Winter 2019/CS+Law Innovation Lab/Orrick, Harrington, & Sutcliffe/Documents/Test_Text.txt'

with open(direct_path, 'r') as file:
    brief = file.read()

test = ex.Extractor(brief)
qGen = gen.QuestionGenerator()
test.fix_pronouns(silence=1)
sentences = test.get_sentences()
print(sentences)

for sentence in sentences:
    flashcard = qGen.generate_question(sentence)
    if flashcard:
        #print(type(flashcard), type(flashcard[0]))
        print("Question: {}\n\nAnswer: {}'\n-------------".format(flashcard[0]['Q'], flashcard[0]['A']))


