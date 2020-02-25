import language_check
import os
# import getpass

def question_filter(questions_ls):
	# Need to implement this part to do a interactive feature that takes client's password:
	'''
	# sudo_password = input('Input password for a sudo command: ')
	# os.system('if which jenv > /dev/null; then eval "$(jenv init -)"; fi')
	# need to import getpass for the following line
	# sudo_password = getpass.getpass()
	# command = 'sudo jenv global 1.8.0.242'
	# os.system('echo %s|sudo -S %s' % (sudo_password, command))
	'''
	tool = language_check.LanguageTool('en-US')
	for q in questions_ls: 
		matches = tool.check(q)
		if matches != []:
			questions_ls.remove(q)

	return questions_ls
