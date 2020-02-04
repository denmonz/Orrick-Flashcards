import sys
import lexnlp.nlp.en.segments.sentences as lex_sentences
import lexnlp.extract.en.dates as lex_dates
import lexnlp.extract.en.entities.nltk_maxent as lex_entities

direct_path = ""

with open(direct_path, 'r') as file:
    brief = file.read()

processed_brief = lex_sentences.pre_process_document(brief)
sentences_brief = lex_sentences.get_sentence_list(processed_brief)


facts = []

for sentence in sentences_brief:
    entities = lex_entities.get_persons(sentence)
    for entity in entities:
        facts.append((entity,sentence))


for fact in facts:
    print("Question:\nWhy is {} relevant?\n\nAnswer:\n{}".format(fact[0], fact[1]))
    print("\n---------------\n")

    
'''
Question:
Why is Farmers Branch relevant?

Answer:
In 2009, DISH began a pilot program to test QPC, a new incentive-based system at several locations, including two of its eight offices in the North Texas region: Farmers Branch and North Richland Hills.

---------------

Question:
Why is Hills relevant?

Answer:
The technicians in Farmers Branch and North Richland Hills fervently opposed QPC because it decreased their hourly base wage.

---------------
'''

