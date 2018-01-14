import os
import argparse

from path_maker import path_maker

DESCRIPTION = "gtree is a simple program which automatically create directory-templates \
on your system as per defined in an text file."

SRC_FILE_DESCRIPTION = "file in which directory-structure is defined"
DES_PATH_DESCRIPTION = "path to were the directory-structure should be created"
INCLUDE_DESCRIPTION = "Turn off @include tag"
PH_DESCRIPTION = "Turn off placeholder option's"

TPATH_DESCRIPTION = "specify path to were templates should be searched for when used @include tag"

PROGRAM_NAME = "gtree"


def main():
	parser = argparse.ArgumentParser( prog = PROGRAM_NAME, description = DESCRIPTION, epilog = "Documentation can be found at : https://github.com/a5hish/gtree-tool/blob/master/README.md" )
	parser.add_argument("input_file", help = SRC_FILE_DESCRIPTION)
	parser.add_argument("des_path", help = DES_PATH_DESCRIPTION)
	parser.add_argument("-i", "--include_ignore", help = INCLUDE_DESCRIPTION, action = "store_false")
	parser.add_argument("-p", "--ph_ignore", help = PH_DESCRIPTION, action = "store_false")
	parser.add_argument("-t", "--tpath", help = TPATH_DESCRIPTION)


	args = parser.parse_args()

	src = os.path.realpath(args.input_file)
	des = os.path.realpath(args.des_path)+"/"
	i_option = args.include_ignore
	ph_option = args.ph_ignore
	tpath = args.tpath

	if tpath == None:
		tpath = os.path.expanduser("~")+"/Templates/gtree-templates/"
		if os.path.isdir(tpath) == False:
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
