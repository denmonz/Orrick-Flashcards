import language_check
import os
import getpass


def question_filter(questions_ls):
	
	# sudo_password = input('Input password for a sudo command: ')
	
	#os.system('if which jenv > /dev/null; then eval "$(jenv init -)"; fi')
	#sudo_password = getpass.getpass()
	#command = 'sudo jenv global 1.8.0.242'
	#os.system('echo %s|sudo -S %s' % (sudo_password, command))
	
	tool = language_check.LanguageTool('en-US')
	for q in questions_ls: 
		matches = tool.check(q)
		if matches != []:
			questions_ls.remove(q)

	return questions_ls

def main():
	
	qls = ['What is H20?', 
		'Can this Java-program be written better?',
		'Who teaches Java at teamtreehouse?',
		'Which Countries share a border with Switzerland?',
		'What is our group name?',
		'Who was the 3rd president of the United States?',
		'Which law school?',
		'Which law school do you attend?']
	
	q1 = ['What could not support class certification even if they were implemented?', 
		'Moreover, Plaintiffs injury theories could not support class certification even if they were implemented.', 
		'What was thus appropriately denied?', 
		'Class certification was thus appropriately denied.', 
		'Who has provided Plaintiffs ample opportunity to establish their case?', 
		'Since inheriting this and related cases in 2012 (when Judge James Ware retired), Judge Gonzalez Rogers has been impartial, patient and provided Plaintiffs ample opportunity to establish their case.', 
		'What are suspect?', "Plaintiffs' motivations in even raising the issue are suspect.", 'What did Rail Freight F.3d at?', 'Rail Freight, 725 F.3d at 253.', 'What 459?']

	print(question_filter(q1))
	print(question_filter(qls))

if __name__ == '__main__':
    main()