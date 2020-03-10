### Potential Rule-based Question Filters ###
# Gathering rule-based filtering functions
# Potentially implement these in main.py
import nltk
import lexnlp
import lexnlp.nlp.en.tokens

def rm_2_short(questions):
'''
# input string[]: a python list of questions 
# output string[]: a list of filtered questions 
# purpose: remove questions that are too short (likely to be bad):
	- remove ones consisted of 2 terms
	- remove ones shorter than a length of 8 (worst case: "Who is ?")
	- remove non-sense questions generated from our system (e.g. "What 345?")
''' 
	filtered_questions = []
	for ques in questions:
		if len(ques) > 8 or len(ques.split()) > 2:
			filtered_ls.append(ques)
	return filtered_questions

def rm_not_quote(questions):
# if "`" exists once, it usually is accompanied by other weird quote marks
# rid all of them:
	for ques in questions:
		if "`" in ques:
			ques.strip("`")
			ques.strip('"')
			ques.strip("'")
	return questions


def rm_bad_question(questions):
# get rid of the "What-is-[bad-word]" type of questions
	filtered_questions = []
	for ques in questions:
		nouns = list(lexnlp.nlp.en.tokens.get_nouns(ques))
		verbs = list(lexnlp.nlp.en.tokens.get_nouns(ques))
		if len(ques.split()) != 3:
			if (ques.split()[1] not in verbs) and (ques.split()[2] in nouns):
				filtered_questions.append(ques)
	return filtered_questions




