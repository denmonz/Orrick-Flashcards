import sys

import lexnlp.nlp.en.segments.sentences as lex_sentences
import lexnlp.nlp.en.segments.sections as lex_sections
import lexnlp.nlp.en.segments.paragraphs as lex_paragraphs
import lexnlp.nlp.en.segments.pages as lex_pages
import lexnlp.extract.en.dates as lex_dates
import lexnlp.extract.en.courts as lex_courts
import lexnlp.extract.en.definitions as lex_definitions
import lexnlp.extract.en.regulations as lex_regulations
import lexnlp.extract.en.trademarks as lex_trademarks
import lexnlp.extract.en.entities.nltk_maxent as lex_entities



class Extractor:
    
    def __init__(self, text):
        self.text = self.init_preprocess(text)
        self.init_tokenize()
        self.sections = None
        self.pages = None
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
        self.sections = self.get_sections(text)
        self.paragraphs = self.get_paragraphs(text)
        self.sentences = self.get_sentences(text)
        self.pages = self.get_pages(text)
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

    # Returns list of pages
    def get_pages(self, text = None):
        if not text:
            text = self.text 
        return list(lex_pages.get_pages(text))

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



    '''
    Functions: Locate Entities
    '''
    # Returns page locations for entity
    def locate_pages(self, entity):
        if not self.pages:
            self.init_preprocess()
            self.init_tokenize()
        if len(entity)>1:
            entity = " ".join(entity)           
        result = []
        for page_index, page_content in enumerate(self.pages):
            count = page_content.count(entity)
            for x in range(count):
                # TODO: Needs adjusting for Roman Numeral pages (i, ii, ...) before page 1
                result.append((page_index, entity))

        return result


    # Returns page locations for entity
    def locate_sections(self, entity):
        if not self.sections:
            self.init_preprocess()
            self.init_tokenize()
        if len(entity)>1:
            entity = " ".join(entity)
        result = []
        for section_index, section_content in enumerate(self.sections):
            count = section_content.count(entity)
            for x in range(count):
                # TODO: Need to get section heading for the sections
                result.append((section_index, entity))

        return result
    
