### Potential Rule-based Question Filters ###
# Gathering rule-based filtering functions
# Potentially implement these in main.py
# all inputs and outputs are in forms of a q:a dictinary: 
# {heading: {q1:a1, q2:a2, ..., q230:a230}}
# might need to be careful with heading data type
import nltk
import lexnlp
import lexnlp.nlp.en.tokens

def dict_zip(dict):
	ls_keys = [k for k in dict]
	ls_values = [v for v in dict.values()]
	#ls_ls = [[k,v] for k, v in dict.items()]
	#ls_tup = [(k,v) for k, v in dict.items()]
	return ls_keys, ls_values

def rm_2_short(dict):
# purpose: remove questions that are too short (likely to be bad):
#	- remove ones consisted of 2 terms
#	- remove ones shorter than a length of 8 (worst case: "Who is ?")
#	- remove non-sense questions generated from our system (e.g. "What 345?")
	# get the only key(heading) of original dict
	heading = dict_zip(dict)[0][0]
	# get the only value (q&a dictionary) of original dict
	#qna = dict_zip(dict)[1]
	qna = dict[heading]
	# get a list of questions
	questions = dict_zip(qna)[0] 
	bad_questions = []
	for ques in questions:
		if len(ques) <= 8 or len(ques.split()) <= 2:
			bad_questions.append(ques)
	
	for key in bad_questions:
		qna.pop(key)
	filtered_dict = {}
	filtered_dict[heading] = qna
	return filtered_dict

def rm_not_quote(dict):
# if "`" exists once, it usually is accompanied by other weird quote marks
# rid all of them:
	heading = dict_zip(dict)[0][0]
	qna = dict[heading]
	questions = dict_zip(qna)[0] 

	for ques in questions:
		if "``" in ques:
			newq = ques.replace("``", '"')
			qna[newq] = qna.pop(ques)
		'''
		elif "`" in ques:
			newq = ques.replace("`", "")
			#newq = ques.strip('"')
			#newq = ques.strip("'")
			qna[newq] = qna.pop(ques)
		'''

	questions = dict_zip(qna)[0] 
	for ques in questions:
		newques = ques.split("?", 1)[0] + "?"
		qna[newques] = qna.pop(ques)
	return qna

	filtered_dict = {}
	filtered_dict[heading] = qna
	return filtered_dict

def rm_bad_question(dict):
# get rid of the "What-is-[bad-word]" type of questions
# Pronoun + be + [bad word]
	heading = dict_zip(dict)[0][0]
	qna = dict[heading]
	questions = dict_zip(qna)[0] 

	bad_questions = []
	for ques in questions:
		nouns = list(lexnlp.nlp.en.tokens.get_nouns(ques))
		verbs = list(lexnlp.nlp.en.tokens.get_nouns(ques))
		if len(ques.split()) != 3:
			if (ques.split()[1] in verbs) and (ques.split()[2] not in nouns):
				bad_questions.append(ques)
	
	for key in bad_questions:
		qna.pop(key)
	filtered_dict = {}
	filtered_dict[heading] = qna
	return filtered_dict




