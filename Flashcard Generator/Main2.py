# you may need to pip install python-docx
import ParseDocx
import os
import sys
def Main():
    # Put direct path to word doc here, or pass as command line argument
    word_doc = ''
    if len(sys.argv)>1:
        word_doc = sys.argv[1]

    #Flashcard Generation
    def process(section_text, section_name):
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
        brief = section_text
        print("--- %s seconds to Load ---" % (time.time() - start_time))

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

        for sentence in sentences:
                flashcard = questions.generate_question(sentence)
                if flashcard:
                    partial = {"question":flashcard[0]['Q'], "answer": flashcard[0]['A']}
                    result[section_name].append(partial)
                    
        print("--- %s seconds to Generate Questions ---" % (time.time() - start_time))


    #Parse and Process
    #ParseDocx returns dictionary {section: 'section text', section:''}
    parsed = ParseDocx.ParseDocx(word_doc)

    result = {}

    for section, text in parsed.items():
        result[section] = []
        process(text, section)

    print(result)
    return result


if __name__ == "__main__":
    Main()
