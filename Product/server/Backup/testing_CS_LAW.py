import sys
import lexnlp.nlp.en.segments.sentences as lex_sentences
import lexnlp.extract.en.dates as lex_dates

# path as command line argument
# path = sys.argv[1]

# copy&paste brief pdf into .txt file. 
direct_path = "/Users/brandon/Documents/Northwestern Courses/Winter 2019/CS+Law Innovation Lab/Orrick, Harrington, & Sutcliffe/Documents/Dish_Sample.txt"

with open(direct_path, 'r') as file:
    brief = file.read()

processed_brief = lex_sentences.pre_process_document(brief)
sentences_brief = lex_sentences.get_sentence_list(processed_brief)

#print(sentences_brief)

facts = []
for sentence in sentences_brief:
    dates = lex_dates.get_dates(sentence)
    for date in dates:
        facts.append((date,sentence))

for fact in facts:
    print("Question:\nWhy is {} significant?\n\nAnswer:\n{}".format(str(fact[0]), fact[1]))
    print("\n---------------\n")
