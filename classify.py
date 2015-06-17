#!/usr/bin/python3

from db import Db
from words import text_to_list
from pdb import set_trace

class Classify():
	MIN_WORD_COUNT = 5
	RARE_WORD_PROB = 0.5
	EXCLUSIVE_WORD_PROB = 0.99

	def set_text(self, text):
		words = text_to_list(text)

		if not len(words):
			raise ValueError('Text did not contain any valid words')

		self.words = words
		return self

	def set_file_name(self, file_name):
		try:
			file_contents = open(file_name, 'r').read()
			return self.set_text(file_contents)

		except Exception as e:
			raise ValueError('Unable to read specified file "%s", the error message was: %s' % (file_name, e))

	def set_doc_types(self, doc_type1, doc_type2):
		if doc_type1 == doc_type2:
			raise ValueError('Please enter two different doc_types')

		d = Db().get_doc_type_counts()
		
		if doc_type1 and doc_type2 not in d.keys():
			raise ValueError('Unknown doc_type: ' + doc_type2)

		self.doc_type1 = doc_type1
		self.doc_type2 = doc_type2

	def validate(self, args):

		if len(args) == 5:

			self.set_file_name(args[2])
			self.set_doc_types(args[3], args[4])

		else:

			doc_type1 = input("Enter doc_type1: ")
			doc_type2 = input("Enter doc_type2: ")
			self.set_file_name(input("Enter doc/file path: "))
			self.set_doc_types(doc_type1, doc_type2)


	def prob_4_word(self, db, word):
		total_word_count = self.doc_type1_word_count + self.doc_type2_word_count

		word_count_doc_type1 = db.get_word_count(self.doc_type1, word)
		word_count_doc_type2 = db.get_word_count(self.doc_type2, word)
		
		if word_count_doc_type1 + word_count_doc_type2 < self.MIN_WORD_COUNT:
			return self.RARE_WORD_PROB

		if word_count_doc_type1 == 0:
				return 1 - self.EXCLUSIVE_WORD_PROB
		elif word_count_doc_type2 == 0:
				return self.EXCLUSIVE_WORD_PROB

		# P(S|W) = P(W|S) / ( P(W|S) + P(W|H) )

		p_ws = word_count_doc_type1 / self.doc_type1_word_count
		p_wh = word_count_doc_type2 / self.doc_type2_word_count

		return p_ws / (p_ws + p_wh)


	def prob_4_list(self, prob_list):
		# PROB_LIST = 0

		prob_product = 1
		for each in prob_list:
			prob_product *= each

		for i in range(len(prob_list)):
			prob_list[i] = 1 - prob_list[i]

		prob_inverse_product = 1
		for each in prob_list:
			prob_inverse_product *= each

		return float(prob_product)/(float(prob_product) + float(prob_inverse_product))

	def execute(self):
		pl = []
		db = Db()

		d = db.get_doc_type_counts()
		self.doc_type1_count = d.get(self.doc_type1)
		self.doc_type2_count = d.get(self.doc_type2)

		self.doc_type1_word_count = db.get_words_count(self.doc_type1)
		self.doc_type2_word_count = db.get_words_count(self.doc_type2)

		for word in self.words:
			p = self.prob_4_word(db, word)
			pl.append(p)

		result = self.prob_4_list(pl)

		return result

	def output(self, result):
		print ('Probability that document is {} rather than {} is {}'.format(self.doc_type1, self.doc_type2, result))