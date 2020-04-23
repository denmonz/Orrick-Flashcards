# you may need to pip install python-docx
import ParseDocx
import os
import sys

def main(path):
# Put direct path to word doc here, or pass as command line argument
    word_doc = path
    # if len(sys.argv)>1:
    #     word_doc = sys.argv[1]

    #Flashcard Generation
    def process(input_directory, input_file, section_name):
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
        with open(input_file, 'r') as file:
            brief = file.read()
        print("--- %s seconds to Load ---" % (time.time() - start_time))

        #Preprocess
        ##start_time = time.time()
        ##brief = lex_sentences.pre_process_document(brief)
        ##print("--- %s seconds to LexNLP Preprocess---" % (time.time() - start_time))

        start_time = time.time()
        pronouns = spacy.load('en_core_web_sm')
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
    #    start_time = time.time()
    #    with open(input_directory+"/"+section_name+'.csv', 'w') as csvfile:
    #        qawriter = csv.writer(csvfile)
    #        qawriter.writerow(["Q", "A"])
    #        for sentence in sentences:
    #                flashcard = questions.generate_question(sentence)
    #                if flashcard:
    #                    qawriter.writerow([flashcard[0]['Q'], flashcard[0]['A']])
    #    print("--- %s seconds to Generate Questions ---" % (time.time() - start_time))


    #Parse and Process
    ParseDocx.ParseDocx(word_doc)

    new_folder = os.path.splitext(os.path.basename(word_doc))[0]
    direc =os.path.dirname(word_doc)
    parsed_directory = direc + "/" + new_folder

    file_names = os.listdir(parsed_directory)
    full_paths = []
    for file in file_names:
        full_paths.append((parsed_directory+"/"+file, file[:-4]))

    csv_dir = parsed_directory+"/"
    for file in full_paths:
        process(csv_dir, file[0], file[1])
    
    print_data = {
    "section1": [
        {
            "question": "first q?",
            "answer": "first a."
        },
        {
            "question": "second q?",
            "answer": "second a."
        },
        {
            "question": "third q?",
            "answer": "third a."
        }
    ],
    "section2": [
        {
            "question": "fourth q?",
            "answer": "fourth a."
        },
        {
            "question": "fifth q?",
            "answer": "fifth a."
        },
        {
            "question": "sixth q?",
            "answer": "sixth a."
        }
    ]
    }
    print(print_data)

    return print_data
