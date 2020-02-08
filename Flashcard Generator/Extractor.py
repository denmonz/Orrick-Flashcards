import sys

import lexnlp.nlp.en.segments.sentences as lex_sentences
import lexnlp.nlp.en.segments.sections as lex_sections
import lexnlp.nlp.en.segments.paragraphs as lex_paragraphs
import lexnlp.extract.en.dates as lex_dates
import lexnlp.extract.en.courts as lex_courts
import lexnlp.extract.en.definitions as lex_definitions
import lexnlp.extract.en.regulations as lex_regulations
import lexnlp.extract.en.trademarks as lex_trademarks
import lexnlp.extract.en.entities.nltk_maxent as lex_entities


class Extractor:
    
    def __init__(self, text):
        self.text = self.init_preprocess(text)
        self.sections = None
        self.paragraphs = None
        self.sentences = None
        return



    '''
    Functions: Prep the Document
    '''
    # Pre-process Document
    def init_preprocess(self, text = None):
        return lex_sentences.pre_process_document(text)

    
    # Tokenize the Document
    def init_tokenize(self, text = None):
        if not text:
            text = self.text           
        self.sections = self.tokenize_to_sentences(text)
        self.paragraphs = self.tokenize_to_paragraphs(text)
        self.sentences = self.tokenize_to_sentences(text)
        return

        
    # Give Extractor new document
    def update_text(self, text = None):
        if not text:
            text = self.text
        self.text = self.init_preprocess(text)
        return 



    '''
    Functions: Tokenize The Document
    '''
    # Returns list of sections
    def get_sections(self, text = None):
        if not text:
            text = self.text 
        return list(lex_sections.get_sections(text))


    # Returns list of paragraphs
    def get_paragraphs(self, text = None):
        if not text:
            text = self.text 
        return list(lex_paragraphs.get_paragraphs(text))

        
    # Returns list of sentences
    def get_sentences(self, text = None):
        if not text:
            text = self.text 
        return list(lex_sentences.get_sentence_list(text))



    '''
    Functions: Extract Entities
    '''
    # Returns list of dates
    def extract_dates(self, text = None):
        if not text:
            text = self.text
        return list(lex_dates.get_dates(text))


    # Returns list of companies
    def extract_companies(self, text = None):
        if not text:
            text = self.text
        return list(lex_entities.get_companies(text))


    # Returns list of geopolitical entities
    def extract_geopolitical(self, text = None):
        if not text:
            text = self.text
        return list(lex_entities.get_geopolitical(text))


    # Returns list of persons
    def extract_persons(self, text = None):
        if not text:
            text = self.text
        return list(lex_entities.get_persons(text))


    # Returns list of courts
    def extract_courts(self, text = None):
        if not text:
            text = self.text
        return list(lex_courts.get_courts(text))
    

    # Returns list of definitions
    def extract_definitions(self, text = None):
        if not text:
            text = self.text
        return list(lex_definitions.get_definitions(text))


    # Returns list of regulations
    def extract_regulations(self, text = None):
        if not text:
            text = self.text
        return list(lex_definitions.get_regulations(text))


    # Returns list of trademarks
    def extract_regulations(self, text = None):
        if not text:
            text = self.text
        return list(lex_definitions.get_trademarks(text))
    
