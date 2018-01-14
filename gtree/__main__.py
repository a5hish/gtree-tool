import os
import argparse

from path_maker import path_maker

DESCRIPTION = """
gtree is an simple program which create directory-structure as defined in an text-based file.

	Example 1: Simple-usecase
			when an directory-structure is defined in a text-based file (ds1.txt) as:

				my_website/
					index.html 				# This is the homepage
					form.html
					css/
						header.css
						footer.css
					js/
						form_action.js
					config

			When this file (ds1.txt) is passed as an argument to this program it will create
			the directories and files to a perticular location as defined in the file (ds1.txt).

			# this will create directories and files as defined in the "ds1.txt" file at "/tmp" location
			$ gtree ds1.txt /tmp


	Rules while defining directory structure in an file :
		[-] Syntax
			- Only whitespaces or taps are allowed while defining the directory-structure
			- Directory/folders is only noticed when it ends with a "/" symbol.

				Correct Method :
					app/
						file1
						app1/
							file3
						app2

				In-Correct Method and will cause and error :
					app
						file1
						inner_app
							file3
						app3

		[-] Comments
			"#" are use to write comments
			eg:
				index.html 			# This is an comment
			In the above case the sentence after # will be ignored or commented unless there @include option used.

		[-] @include Option
			By default files created using this program are empty but if you want to include some pre-defined template-text in it
			the @include  option is used in the comments after the file name in which you want to include template-text from an
			predified file.
			syntex : # @include="html_template.html"

"""
SRC_FILE_DESCRIPTION = """
path of the file to be used to
"""
DES_PATH_DESCRIPTION = """
Destination to which the files will be genrated.
"""
INCLUDE_DESCRIPTION = """
Turn off @include= option
"""
PH_DESCRIPTION = """
Turn off place_holder option
"""
#FILTERS_DESCRIPTION = """
#specify character filters to be used here.
#(the script uses space to get the relation between parent and child folders/file this option changes ani specified filter character to space)
#"""
TPATH_DESCRIPTION = """
specify path to be the folder to be used to search for include file.
"""

PROGRAM_NAME = "gtree"

def check_required_dir( dir_name ):
	"""
	check for the required directories if not present creates them.
	"""

	if not os.path.isdir(dir_name):
		os.makedirs(dir_name)


def main():
	parser = argparse.ArgumentParser( prog = PROGRAM_NAME, description = DESCRIPTION )
	parser.add_argument("input_file", help = SRC_FILE_DESCRIPTION)
	parser.add_argument("des", help = DES_PATH_DESCRIPTION)
	parser.add_argument("-i", "--include_ignore", help = INCLUDE_DESCRIPTION, action = "store_false")
	parser.add_argument("-p", "--ph_ignore", help = PH_DESCRIPTION, action = "store_false")
	parser.add_argument("-t", "--tpath", help = TPATH_DESCRIPTION)


	args = parser.parse_args()

	src = os.path.realpath(args.input_file)
	des = os.path.realpath(args.des)+"/"
	i_option = args.include_ignore
	ph_option = args.ph_ignore
	tpath = args.tpath

	if tpath == None:
		tpath = os.path.expanduser("~")+"/Templates/gtree-templates/"
		if not os.path.isdir(tpath):
			tpath = "sample-templates/"

	else :
		tpath = os.path.realpath(args.tpath)+"/"

	with open(src, "rb") as f:
		s = f.read()
		path_maker(s,  des, "", tpath, i_option, ph_option)


if __name__ == "__main__":
	try:
		main()
	except Exception, e:
		print str(e)
