#!/usr/bin/python3

from db import Db
from words import list_to_dict
from words import text_to_list
import sys
from pdb import set_trace

class Learn:
	def initialize(self, args):
		self.doc_type = args[1]
		self.doc_file = args[2]

	def validate(self, args):
		# valid_args = False
		usage = 'Usage: python3 learn.py <doc type> <file>'

		if len(args) == 3:

			self.initialize(args)

		else:

			self.doc_type = input("Enter doc_type: ")
			self.doc_file = input("Enter doc/file path: ")

		self.file_contents = None
		
		try:
			self.file_contents = open(self.doc_file, 'r').read()
		except Exception as e:
			raise ValueError(usage + '\nUnable to read specified file "{}", the error message was: {}'.format(self.doc_file, e))

		self.count = len(open(self.doc_file, 'r').readlines())


	def execute(self):
		db = Db()
		text_list = text_to_list(self.file_contents)
		text_dict = list_to_dict(text_list)
		db.update_word_counts(text_dict, self.doc_type)
		db.update_doctype_count(self.count, self.doc_type)
		return self.count

	def output(self, _):
		print("Processed {} documents of type '{}'".format(self.count, self.doc_type))

learn = Learn()
learn.validate(sys.argv)
learn.output(learn.execute())