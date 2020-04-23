#Speedup: bash runStanfordParserServer.sh, bash runSSTServer.sh

import sys
import pip
import spacy
import neuralcoref
import lexnlp.nlp.en.segments.sentences as lex_sentences
import question_generator as gen
import csv
import time


#Load
start_time = time.time()
direct_path = '/Users/brandon/Documents/Northwestern Courses/Winter 2019/CS+Law Innovation Lab/Orrick, Harrington, & Sutcliffe/Documents/Apple Answering Brief - Word Version/ARGUMENT III.txt'

with open(direct_path, 'r') as file:
    brief = file.read()
print("--- %s seconds to Load ---" % (time.time() - start_time))


#Preprocess
##start_time = time.time()
##brief = lex_sentences.pre_process_document(brief)
##print("--- %s seconds to LexNLP Preprocess---" % (time.time() - start_time))


start_time = time.time()
pronouns = spacy.load('en')
neuralcoref.add_to_pipe(pronouns,greedyness=0.5,max_dist=100,blacklist=False)
neural = pronouns(brief)
brief = neural._.coref_resolved
print("--- %s seconds to Pronoun Fix ---" % (time.time() - start_time))

#Tokenize
start_time = time.time()
sentences = list(lex_sentences.get_sentence_list(brief))
questions = gen.QuestionGenerator()
print("--- %s seconds to Tokenize ---" % (time.time() - start_time))

#Print
start_time = time.time()
with open('/Users/brandon/Documents/Northwestern Courses/Winter 2019/CS+Law Innovation Lab/Orrick, Harrington, & Sutcliffe/Documents/ex.csv', 'w') as csvfile:
    qawriter = csv.writer(csvfile)
    qawriter.writerow(["Q", "A"])
    for sentence in sentences:
            flashcard = questions.generate_question(sentence)
            if flashcard:
                qawriter.writerow([flashcard[0]['Q'], flashcard[0]['A']])
print("--- %s seconds to Generate csv ---" % (time.time() - start_time))
