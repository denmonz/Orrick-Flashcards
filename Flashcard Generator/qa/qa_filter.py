### Potential Rule-based Question Filters ###
# Created by Zhili Wang
# Gathering rule-based filtering functions
# Potentially implement these in main.py
# all inputs and outputs are in forms of a q:a dictinary:
# {heading: {q1:a1, q2:a2, ..., q230:a230}}
# might need to be careful with heading data type
import nltk
import lexnlp
import lexnlp.nlp.en.tokens
from get_dict import get_dict


def dict_zip(dict, sections):
    dict = dict[sections][0]
    ls_keys = [k for k in dict]
    ls_values = [v for v in dict.values()]
    # ls_ls = [[k,v] for k, v in dict.items()]
    # ls_tup = [(k,v) for k, v in dict.items()]
    return ls_keys, ls_values


# I am taking a different approach to keep every filter short
# and deal with the difficult structure of our json in 'assemble' function
def if_2_short(question):
    # purpose:
    # remove questions that are too short (likely to be bad):
    # remove ones consisted of 2 terms (e.g. "What 345?")
    # remove ones shorter than a length of 8 (worst case: "Who is ?")

    ## c++ way:
    ## return (len(ques) <= 8 or len(ques.split()) <= 2) ? True : False
    # if it is not a bad question --> True --> we take further actions
    return True if len(question) > 8 or len(question.split()) > 3 else False


# isolating this function for now
def rm_not_quote(qna, heading):
    # if "`" exists once, it usually is accompanied by other weird quote marks
    # rid all of them:
    # heading = dict_zip(dict)[0][0]
    # qna = dict[heading]
    questions = dict_zip(qna, heading)[0]

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

    questions = dict_zip(qna, heading)[0]
    for ques in questions:
        newques = ques.split("?", 1)[0] + "?"
        qna[newques] = qna.pop(ques)
    return qna


def if_bad_question(question):  # (qna, heading):
    # get rid of the "What-is-[bad-word]" type of questions
    # Pronoun + be + [bad word]
    # heading = dict_zip(dict)[0][0]
    # qna = dict[heading]
    nouns = list(lexnlp.nlp.en.tokens.get_nouns(question))
    verbs = list(lexnlp.nlp.en.tokens.get_nouns(question))
    # if it is a bad question --> True --> we take further actions
    if len(question.split()) == 3:
        if (question.split()[1] in verbs) and (question.split()[2] not in nouns):
            return True
    return False


def get_sections(dict_json):
    # purpose:
    # pass in our structure of q&a data and get a list of sections
    sections = []
    for section in dict_json.keys():
        sections.append(section)
    return sections


def assemble(dict1):  # we can add the json file of qa here as input later
    # get list of sections
    dict1 = get_dict()
    sections = get_sections(dict1)
    print("Here are the sections: {}".format(sections))

    # traverse the list of sections to access to every section of data
    for sec in sections:
        # get each section's
        if len(dict1[sec]) == 0:
            # if nothing in this section, do nothing
            pass
        else:
            for pairs in dict1[sec]:
                temp_new_ls = list()
                if if_2_short(pairs["question"]):
                    temp_new_ls.append(pairs)
                elif if_bad_question(pairs["question"]):
                    temp_new_ls.append(pairs)
                dict1[sec] = temp_new_ls
    return dict1


if __name__ == "__main__":
    print(assemble())
