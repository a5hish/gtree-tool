# gtree
gtree is a simple program which automatically create directory-templates on your system as per defined in an text file.

# Requirements
- python-2.7.*
- linux based OS

# Installation
These instructions will get you a copy of the ***gtree*** up and running on your local machine.


```sh
# getting the source files from the git:
$ git clone https://github.com/a5hish/gtree-tool.git

$ cd gtree-tool/

# to install it on your system use the following command
$ pip install --user .

# it can also be used directly from the source file like
$ bin/gtree --help
```
## Quick Example:
For this example we will define a simple python project directory-structure in an file "sample1-ds.txt" and pass this file to the "gtree" program with the location of were to create it.

*File : sample1-ds.txt*
```
# sample-1 directory-structure
project/
    bin/
        project
    project/
        __init__.py
        module1.py
        main.py
    setup.py    
```

we will pass the above file to the ***gtree*** program and give destination location as "/tmp" to create the defined directories.

```sh
$ gtree sample1-ds.txt /tmp
Done
```
gtree creates the defined directories and files.
```
$ ls /tmp/project
bin/  project/  setup.py
```

# Usage :

#### How to define directory-structure in an file :

**Comments** :
To write comments in the file use "#", sentence written after this character will be ignore by gtree.
```
# This is an comment
# which will be ignored
app/
    setup.py    # this is also a comment
    run.py      # and this too.
```
(and exception to this is the @include tag).

_______
**Indentation** :
Only whitespaces or taps should be used for indentation's and defining hierarchy between inner directories and files.
```
# example
app/
    bin/
        script
    setup.py
```
______
**Directory** :
Directory is only noticed when their name ends with a "/".
```
app/        # this will interpreted as directory by gtree
app         # this will interpreted as file by gtree
```
____
**Tags** :

By default files created using gtree are empty but if you want to include some pre-defined template-text in them, then ***@include*** tag can be used, the ***@include***  tag is used in the comments after the file name in which you want to include template-text.
Syntax : @include="file-name"
file-name is the name of the file in which the template-text is defined, This file should be stored at location ***"~/Templates/gtree-templates/"***, hence this is the default location were gtree search for templates-files with @include tag.
```
# example usecase
website/
    index.html          # @include="html_file"
    img/
    js/
    css/
```
(****-t**** option can be used to tell gtree to use a different location when searching for templates).
____
### Placeholders :
This are special string which are used in template-text file that are changed dynamically at runtime by gtree.
| PlaceHolders | Function |
|---|----|
|[@file_name]|This will be changed to the name of the file into which it is copied|
|[@date]| This will be changed to the date on which the file was created.|

( Used on files which are stored in ***“~/Templates/gtree-templates/”***)
### Example using @include and placeholer:
we will create an html template file with placeholder's
*File : ~/Templates/html_file*
```
 <!DOCTYPE html>
<html>
<head>
<title> [@file_name] </title>
</head>
<body></body>
</html>
```

*File : sample3-ds.txt*
```
website/
    homepage.html   # @include="html_file"
    css/
    img/
```

```sh
# execute gtree
$ gtree sample3-ds.txt /tmp/
```

Now when the directory-structure is created by gtree the contains on *"html_file"* will be copied to homepage.html with **[@file_name]** replaced with the name of that file (i.e Homepage)

```sh
# homepage file containts would look like this now
$ cat /tmp/website/homepage.html
<html>
<head>
<title> homepage </title>
</head>
<body></body>
</html>
```
