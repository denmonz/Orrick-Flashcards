### Potential Rule-based Question Filters ###
# Gathering rule-based filtering functions

def rm_2_short(ques_ls):
'''
# input string[]: a python list of questions 
# output string[]: a list of filtered questions 
# purpose: remove questions that are too short (likely to be bad):
	- remove ones consisted of 2 terms
	- remove ones shorter than a length of 8 (worst case: "Who is ?")
	- remove non-sense questions generated from our system (e.g. "What 345?")
'''
	for ques in ques_ls:
		if len(questions) <= 8:
			ques_ls.remove(ques)
		if len(question.split()) <= 2:
			ques_ls.remove(ques)
	return ques_ls

def rm_ques_mark(ques_ls)
'''
# input string[]: a python list of questions 
# output string[]: a list of filtered questions 
# purpose: remove all question marks of every individual question 
	 	- complements the "rm_2_short" function: in rare cases there are 
	 	question marks in front of the spaces, which lead to inaccurate 
	 	lengths of sentences
		- our alternate/improved version of Question-Answering 
		system performs better if question marks are stripped 
		(we can easily add '?' back whenever we print out the questions) 
'''
	for question in question_list:
		question = question.strip('?')
	return ques_ls