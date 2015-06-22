#!/usr/bin/python3

import sys
from pdb import set_trace

if __name__ == '__main__':
	try:

		args = sys.argv
		usage = 'Usage: python3 learn.py <file> <doc_type> \n python3 bayes.py classify <file> <doc_type1> <doc_type2>'

		if (len(args) < 2):
			raise ValueError(usage)

		modes = ['learn', 'classify']
		mode_name = args[1].lower()

		if mode_name not in modes:
			raise ValueError(usage + '\nUnrecognised mode: ' + mode_name)
		
		print(mode_name)
		if mode_name == 'learn':
			print("learn")
			from learn import Learn as M
		else:
			print("Classify")
			from classify import Classify as M
		
		mode = M()
		mode.validate(args)
		mode.output(mode.execute())

		
	except Exception as ex:
		print(ex)
