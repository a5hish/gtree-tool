import os
import shutil
from setuptools import setup, find_packages

temp_dir = os.path.expanduser("~")+"/Templates/gtree-templates/"
if os.path.isdir(temp_dir) == False:
	os.makedirs(temp_dir)
	shutil.copytree("sample-templates/", temp_dir)
	os.rename()


setup(
	name = "gtree",
	version = "0.1",
	description = "gtree is a simple program which automatically create directory-templates form a text file",
	author = "a5hish",
	packages = ["gtree"],
	license = 'GPLv3',
	entry_points={
          'console_scripts': ['gtree = gtree.__main__:main'],
      }
)
