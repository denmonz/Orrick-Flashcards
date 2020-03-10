### Potential Rule-based Question Filters ###
# Gathering rule-based filtering functions
# Potentially implement these in main.py
import nltk
import lexnlp
import lexnlp.nlp.en.tokens

# all inputs and outputs are in forms of a q:a dictinary: 
# {q1:a1, q2:a2, ..., q230:a230}
def rm_2_short(qna):
# purpose: remove questions that are too short (likely to be bad):
#	- remove ones consisted of 2 terms
#	- remove ones shorter than a length of 8 (worst case: "Who is ?")
#	- remove non-sense questions generated from our system (e.g. "What 345?")
	 
	filtered_questions = 
	for ques in questions:
		if len(ques) > 8 or len(ques.split()) > 2:
			filtered_questions.append(ques)
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
# Pronoun + be + [bad word]
	filtered_questions = []
	for ques in questions:
		nouns = list(lexnlp.nlp.en.tokens.get_nouns(ques))
		verbs = list(lexnlp.nlp.en.tokens.get_nouns(ques))
		if len(ques.split()) != 3:
			if (ques.split()[1] not in verbs) and (ques.split()[2] in nouns):
				filtered_questions.append(ques)
	return filtered_questions




