import os
import shutil
from setuptools import setup, find_packages

temp_dir = os.path.expanduser("~")+"/Templates/gtree-templates"
if not os.path.isdir(temp_dir):
	os.makedirs(tmp_dir)
	shutil.copytree("sample-templates/", temp_dir)


setup(
	name = "gtree",
	version = "0.1dev",
	description = "Gtree is an simple script which can be used to create directory-structure as defined in an text-based file.",
	author = "a5hish",
	packages = ["gtree"],
	entry_points={
          'console_scripts': ['gtree = gtree.__main__:main'],
      }
)
