#!/usr/bin/python3

import re
from pdb import set_trace

commonWords = ('the','be','to','of','and','a','in','that','have','it','is','im','are','was','for','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when','make','can','like','time','just','him','know','take','person','into','year','your','some','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','way','even','because','any','these','us')

def list_to_dict(word_list):
	text_dict = {}
	add_list_to_dict(word_list, text_dict)
	return text_dict

def add_list_to_dict(word_list, text_dict):
	for word in word_list:
		try:
			text_dict[word] += 1
		except:
			text_dict[word] = 1

def text_to_list(text):
	# cleaned_words = map(cleanUpWord, re.split('\W+', text.strip()))
	# print(list(cleaned_words))
	# return filter(lambda word : word and (len(word) > 0), cleaned_words)

	text = re.split('\W+', text.strip())
	for word in text:
		if (len(word) < 2 or word.isdigit()):
			continue
		elif word in commonWords:
			text.remove(word)

	return text

	# "my name is amit joshi."
