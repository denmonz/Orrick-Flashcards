#Speedup: bash runStanfordParserServer.sh, bash runSSTServer.sh

import sys
import pip
import spacy
import neuralcoref
import lexnlp.nlp.en.segments.sentences as lex_sentences
import question_generator as gen


#Load
direct_path = '/Users/brandon/Documents/Northwestern Courses/Winter 2019/CS+Law Innovation Lab/Orrick, Harrington, & Sutcliffe/Documents/AppleSample.txt'
with open(direct_path, 'r') as file:
    brief = file.read()


#Preprocess
brief = lex_sentences.pre_process_document(brief)
pronouns = spacy.load('en')
neuralcoref.add_to_pipe(pronouns,greedyness=0.5,max_dist=100,blacklist=False)
neural = pronouns(brief)
brief = neural._.coref_resolved


#Tokenize
sentences = list(lex_sentences.get_sentence_list(brief))
questions = gen.QuestionGenerator()


#Print
for sentence in sentences:
        flashcard = questions.generate_question(sentence)
        if flashcard:
            print("Question: {}\n\nAnswer: {}\n-------------\n".format(flashcard[0]['Q'], flashcard[0]['A']))
