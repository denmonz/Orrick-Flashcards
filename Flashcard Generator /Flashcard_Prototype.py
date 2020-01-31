import sys
import lexnlp.nlp.en.segments.sentences as lex_sentences
import lexnlp.extract.en.dates as lex_dates

# path as command line argument
# path = sys.argv[1]

# copy & paste brief pdf into .txt file
direct_path = ""

with open(direct_path, 'r') as file:
    brief = file.read()

processed_brief = lex_sentences.pre_process_document(brief)
sentences_brief = lex_sentences.get_sentence_list(processed_brief)

# print(sentences_brief)

facts = []
for sentence in sentences_brief:
    dates = lex_dates.get_dates(sentence)
    for date in dates:
        facts.append((date, sentence))

for fact in facts:
    print("Question:\nWhy is {} significant?\n\nAnswer:\n{}".format(str(fact[0]), fact[1]))
    print("\n---------------\n")


'''
Question:
Why is 2018-11-26 significant?

Answer:
Case: 18-60522 Document: 00514736148 Page: 17 Date Filed: 11/26/2018 
that these employees were constructively discharged because they faced a Hobson’s Choice?

---------------

Question:
Why is 2018-11-26 significant?

Answer:
Case: 18-60522 Document: 00514736148 Page: 18 Date Filed: 11/26/2018 
performed the task) and assigned dollar values.

---------------

Question:
Why is 2018-11-26 significant?

Answer:
Case: 18-60522 Document: 00514736148 Page: 19 Date Filed: 11/26/2018 
wanted to preserve QPC.

---------------

Question:
Why is 2010-07-01 significant?

Answer:
ROA.1083, 2172 (ALJ).1 
Collective bargaining between DISH and the Union began in July 2010, ROA.2168, and during the first years of bargaining, the parties met approximately a dozen times, for a total of 20 to 25 days.

---------------

Question:
Why is 2013-03-22 significant?

Answer:
2 ROA.1083-84, 1089-93; ROA.1410 (Union’s March 22, 2013 proposal, indicating that “[a]ll bargaining unit employees will participate in the same incentive programs as other non-represented DISH network

---------------
'''
