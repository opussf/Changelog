#!/usr/bin/env python3

class ChangeLog( object ):
	""" Things to do:
	[ ] Assign classes that import dictionary info
	[ ] gather a dictionary
	[ ] set a template path
	[ ] set an output path
	[ ] process templates to output path
	"""
	def __init__( self ):
		pass

if __name__ == "__main__":
	import os, sys
	import argparse

	cwd = os.path.dirname( sys.argv[0] )

	parser = argparse.ArgumentParser(
        description="Change logs based on templates.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

