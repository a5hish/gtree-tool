import re, os, datetime

def getFiltered(text, filters):
	""" returns a string with replaced char in the filters with a spaces """
	# if more filters need's to be added.
	filters = "[\t" + filters + "]"

	# replace the given char in the filters list with a spaces
	text = re.sub(filters, "  ", text)

	return text


def getToIncludes(line):
	"""
	Return's the file_names found in the comment section with @include= format
	If not found return's None
	"""

	tmp_s = re.findall('@include="(.*)"', line)

	if len(tmp_s) <= 0:
		return None

	fnames = []
	for fn in tmp_s[0].split(","):
		fnames.append(fn.strip())
	return fnames

def extractByLines(text, include_option):
	"""
	input(text) 	: Output of getFiltered() function.
	include_option 	: toggle TO_INCLUDE option
						True = Enabled; Flase = Disabled

	Returns a list of tuples containing
	(SPACES_VALUE, FILE_NAME, TO_INCLUDE, FILE_TYPE)
	Values:
		SPACE_VALUE = number of spaces on left-side
		FILE_NAME = file/folder name
		TO_INCLUDE = contained to be copied into the FILE_NAME file from the given file_names.
		FILE_TYPE = type of file
					"D" = directory
					"F" = file

	"""

	data=[]


	# adding a pre-end line to the text to make it ez to apply regex on it
	text="\n"+text

	# creating a list of only the valied lines.
	filtered_text=re.findall("\n(\s*\w+.*)", text)

	if len(filtered_text) > 0 :
		for l in filtered_text:
			if len(l)<=0:
				continue

			tmp_line = l[1:]
			tmp_line = l.split("#")
			file_name = tmp_line[0].rstrip()

			# remove tailling "\n"
			if file_name.find("\n")!=-1:
				file_name = file_name[ file_name.rindex("\n") + 1 : ]

			space_value = len(file_name) - len(file_name.lstrip())
			file_name = file_name.lstrip()

			file_type = "F"

			if file_name[-1] == "/":
				file_type = "D"

			to_includes=None
			if len(tmp_line) == 2 and file_type == "F" and include_option:
				to_includes = getToIncludes(tmp_line[1])

			data.append((space_value, file_name, to_includes, file_type))

	return data


def tupleStrCat(tuple_list, index):
	"""

	tuple_list = list of tuples
	index = index of string in the individual tuples

	return an Concated strings in the given list of tuple with an given index to it.
	"""


	string = ""
	for l in tuple_list:
		string += l[index]

	return string

def genratePaths(data):
	"""
	input : output of extractByLines() function.

	Returns a list of (paths, to_includes, type) tuples.
	"""

	stack_l=[]
	stack_l.append((-1, "", None, "D"))
	paths=[]
	for l in data:
		while len(stack_l)>1 and stack_l[-1][0]>=l[0]:
			stack_l.pop()

		paths.append( ( tupleStrCat( stack_l, 1) + l[1], ) + l[2:] )
		if l[3] == "D":
			stack_l.append(l)

	return paths


def setPlaceHolders(text, file_path):
	"""
	Returns the altered-text with replaced placeholder string with their appropriate dynamic-values.
	"""
	# genrate only the name of the file
	file_name = os.path.basename(file_path)
	file_name = file_name[:file_name.index('.')]
	text = text.replace("[@file_name]", file_name)

	# genrate only date.
	text = text.replace("[@date]", str(datetime.datetime.now().date()))

	return text

def createFromPaths(paths, tailing_path, templates_path, ph_option):
	"""
	input(path)		: output of genratePaths
	tailing_path 	: path of parent directory in which to create this files/folders
	ph_option		: place-holder option to toggle
						True = Enabled; False = Disabled

	Create's directories and file accoring to the defined paths.
	"""


	for path in paths:

		new_path = tailing_path + path[0]

		if path[-1] == "D":
			os.mkdir( new_path )
		else:

			new_file = open( new_path, "wb")

			if path[1] != None:
				for s in path[1]:
					if len(s) == 0:
						continue

					temp_f = open( templates_path + s, "rb" )
					tmp = temp_f.read()

					if ph_option:
						tmp = setPlaceHolders(tmp, new_file.name)

					new_file.write(tmp)
					temp_f.close()

			new_file.close()



def path_maker(text,  destination_path, filter_str,  templates_path, include_option, placeholder_option):
	"""
	creates files/folder form a text-based template.
	"""

	text = getFiltered(text, filter_str)
	data = extractByLines(text, include_option)
	paths = genratePaths(data)

	createFromPaths(paths, destination_path, templates_path, placeholder_option)

	print "Done"
