
"""
Created on Fri Mar 01 13:35:34 2016

@author: Sarthak Ghosh
"""

import re

def getLex(post, liwc_lexicons):
	liwc_lexicon_to_count = {}
	for liwc_lexicon_name in set(liwc_lexicons.keys()):
		liwc_lexicon_to_count[liwc_lexicon_name] = 0	
	for name, items in liwc_lexicons.iteritems():
		for item in items:
			pattern = re.compile(item)
			count = len(pattern.findall(post))
			liwc_lexicon_to_count[name] += count
		liwc_lexicon_to_count[name] /= float(len(post.split(' ')))
		if liwc_lexicon_to_count[name]< 0.0:
			print "negative :", post
		if name=="positive_affect" and liwc_lexicon_to_count[name] == 1.0:
			print "hi: ", post
	return liwc_lexicon_to_count

def get_liwc_dictionary():
	
	liwc_lex_dict = {}
	liwc_lex_dict["positive_affect"] = get_liwc_lexicons("positive_affect")
	liwc_lex_dict["negative_affect"] = get_liwc_lexicons("negative_affect")
	liwc_lex_dict["anger"] = get_liwc_lexicons("anger")
	liwc_lex_dict["anxiety"] = get_liwc_lexicons("anxiety")	
	liwc_lex_dict["sadness"] = get_liwc_lexicons("sadness")
	liwc_lex_dict["swear"] = get_liwc_lexicons("swear")
	return liwc_lex_dict



def get_liwc_lexicons(category):
	liwc_lexicons_directory = "LIWC_lexicons"
	lexicon = []
	lexicon_str = "("
	with open("{0}/{1}".format(liwc_lexicons_directory, category), "r") as file_handle:
		for line in file_handle:
			item = line.strip()
			if "*" in item:
				item = r"\b{0}\b".format(item.replace("*", ".*?"))
			else:
				item = r"\b{0}\b".format(item)
			lexicon_str += item + "|"
	lexicon_str = lexicon_str[:-1] + ")"
	lexicon.append(lexicon_str)
	return lexicon

