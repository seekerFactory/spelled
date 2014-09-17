#! /usr/bin/env python3

import argparse
from testCases.tests import tested



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Chek mi spel', add_help=True)
	parser.add_argument('-v', '--verbose',dest='verbose', action='store_true', help='verbose mode processing shown')
	parser.add_argument('-t', '--test',dest='testcase', action='store', choices={'test1', 'test2', 'basic', 'filetest'}, default='test1',help='testcase name')
	parser.add_argument('-q', '--quit', dest='quit', action='store_true', help='quit now')
	args=parser.parse_args()


	if not args.quit:
		tested(testcase=args.testcase, verbose=args.verbose)
