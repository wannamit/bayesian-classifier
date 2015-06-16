#!/usr/bin/python3

import sys

if __name__ == '__main__':
	try:

		args = sys.argv
		usage = 'Usage: python3 bayes.py learn <file> <doc_type> \n python3 bayes.py classify <file> <doc_type1> <doc_type2>' % (args[0], '|'.join(modes.keys()))

		if (len(args) < 2):
			raise ValueError(usage)

		modes = ['learn', 'classify']
		mode_name = args[1].lower()

		if lower(mode_name) not in modes:
			raise ValueError(usage + '\nUnrecognised mode: ' + mode_name)
		
		if mode_name is 'learn':
			from learn import Learn as modes
		else:
			from classify import Classify as modes
		
		mode = modes()
		mode.validate(args)
		mode.output(mode.execute())
		
	except Exception as ex:
		print ex
