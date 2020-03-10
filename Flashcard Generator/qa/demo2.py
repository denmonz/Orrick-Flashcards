from xl_dict import xl2dict
from q_filter import *

def demo2():
	dict = xl2dict(231)
	rm_2_short(dict)
	rm_not_quote(dict)
	rm_bad_question(dict)

	# this returns {heading:{q:a}}
	# return dict
	# this returns {q:a}
	# return dict['heading']
	# this returns 2 lists: [question] and [answers]
	return dict_zip(dict["heading"])[0], dict_zip(dict["heading"])[1]
