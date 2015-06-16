#!/usr/bin/python3

from db import Db
from mode import Mode
from words import list_to_dict
from words import text_to_list
import sys


class Learn:
	def initialize(self, args):
		self.doc_type = args[2]
		self.doc_file = args[3]

	def validate(self, args):
		# valid_args = False
		# usage = 'Usage: %s learn <doc type> <file>' % args[0]

		if len(args) == 4:

			initialize(args)

		else:

			self.doc_type = input("Enter doc_type: ")
			self.doc_file = input("Enter doc/file path: ")

		self.file_contents = None
		
		try:
			self.file_contents = open(self.doc_file, 'r').read()
			
		except Exception as e:
			raise ValueError(usage + '\nUnable to read specified file "%s", the error message was: %s' % (self.doc_file, e))

		self.count = len(self.file_contents)

	def execute(self):
		db = Db()
		l = text_to_list(self.file_contents)
		d = list_to_dict(l)
		db.update_word_counts(d, self.doc_type)
		db.update_doctype_count(self.count, self.doc_type)
		return self.count

	def output(self, _):
		print "Processed %s documents of type '%s'" % (self.count, self.doc_type)
