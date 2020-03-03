### Potential Rule-based Question Filters ###
# Gathering rule-based filtering functions

def rm_2_short(ques_ls):
'''
# input string[]: a python list of questions 
# output string[]: a list of filtered questions 
# purpose: remove questions that only consist of 2 terms 
	- questions that short are most likely to be bad
	- e.g. remove non-sense questions such as e.g. "What 345?" genearted from our system
'''
	for ques in ques_ls:
		if len(question.split()) <= 2:
			question_list.remove(question1)
	return ques_ls

def rm_ques_mark(ques_ls)
'''
# input string[]: a python list of questions 
# output string[]: a list of filtered questions 
# purpose: remove all question marks of every single question from the input list
	- complements the "rm_2_short" function: in rare cases there are question marks 
	  in front of the spaces, which lead to inaccurate lengths of sentences
	- Zhili has an alternate/improved version of Question-Answering system, which 
	  performs better if question marks are stripped (we can always add them back
	  whenever we print the questions) 
'''
	for question in question_list:
		question = question.strip('?')
	return ques_ls