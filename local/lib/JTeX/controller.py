import os
import sys
from simple_parser import *
import smart_parser

filepaths = [] #Holds filepaths that were specified at the command line

#Stores the filepath for all files either listed at the command line or the files listed inside of directories specified at the command line.
def expand_file_dir(file_or_dir):
    if os.path.isdir(file_or_dir): #If file_or_dir is a directory:
        dir_children = os.listdir(file_or_dir) #Get all directory children (files or more directories)
        for item in dir_children: #Loop through children
            expand_file_dir(os.path.join(file_or_dir, item)) #Append child's name to current path and recurse until a file is found
			
    else: #if the parameter is a file (base case)
	length = len(file_or_dir) #Fetch the length of the filepath (represented as a string)
	if length > 5 and file_or_dir[length-5:length] == '.json': #Check if the file ends in .json
	    filepaths.append(file_or_dir) #Store the filepath
	elif len(file_or_dir) > 3 and file_or_dir[length-3:length] == '.py': #Check if the file ends in .py. Warning: only parses Python lists and dicts!
	    filepaths.append(file_or_dir) #Store the filepath

#Takes in filepaths and directories from the command line
def handle_cmdline():
    for item in sys.argv[1:]: #Loop through command line arguments (files or directories)
	expand_file_dir(item) #Record all files to be parsed

#Takes care of the parsing by using the parser class
def parse():
    #json_parser = simple_parser()
    for filepath in filepaths: #Loop through the text from each file
	smart_parser.scan(filepath)
	#json_parser.parse_file_to_latex(filepath) #Parses the .json or .py file into a .tex file

handle_cmdline()
parse()
