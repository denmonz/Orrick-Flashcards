## Environment Setup:
## pip install spacy==2.1.0
## pip install neuralcoref
## python -m spacy download en


def fix_pronouns(text):

    import pip
    import spacy
    import neuralcoref
    
##   Doesn't work, need to install specific version of spacy
##   def import_or_install(package):
##        try:
##            __import__(package)
##        except ImportError:
##            pip.main(['install', package]) 
##
##    
##    import_or_install('neuralcoref')
##    import_or_install('spacy')


    #print(spacy.__version__)
    nlp = spacy.load('en')
    neuralcoref.add_to_pipe(nlp,greedyness=0.5,max_dist=100,blacklist=False)

    doc = nlp(text)
    clusters = doc._.coref_clusters
    resolved_coref = doc._.coref_resolved

    return resolved_coref

if __name__ == "__main__":
    fixed = fix_pronouns('The dog came back home for dinner. It was happy.')
    print(fixed)
## Paramaters for neuralcoref: (keyword arguments)
##greedyness	float	A number between 0 and 1 determining how greedy the model is about making coreference decisions (more greedy means more coreference links). The default value is 0.5.
##max_dist	int	How many mentions back to look when considering possible antecedents of the current mention. Decreasing the value will cause the system to run faster but less accurately. The default value is 50.
##max_dist_match	int	The system will consider linking the current mention to a preceding one further than max_dist away if they share a noun or proper noun. In this case, it looks max_dist_match away instead. The default value is 500.
##blacklist	boolean	Should the system resolve coreferences for pronouns in the following list: ["i", "me", "my", "you", "your"]. The default value is True (coreference resolved).
##store_scores	boolean	Should the system store the scores for the coreferences in annotations. The default value is True.
##conv_dict	dict(str, list(str))	A conversion dictionary that you can use to replace the embeddings of rare words (keys) by an average of the embeddings of a list of common words (values). Ex: conv_dict={"Angela": ["woman", "girl"]} will help resolving coreferences for Angela by using the embeddings for the more common woman and girl instead of the embedding of Angela. This currently only works for single words (not for words groups).
