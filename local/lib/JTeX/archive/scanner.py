#Do not use this code. Refer to archive_info.txt

import os

text = {} #Holds filepaths as keys and the text in those files specified by the paths as the values.

#Removes line formatters
def format_text(text):
	text = text.replace('\n', ' ').replace('\t', '')
	return text

#Extracts text from a file or many files, specified by file_or_dir, which could be a single file, or directory of files and/or subdirectories. Stores the text with its filepath as the key into the dictionary "text".
def extract_text(file_or_dir):
	if os.path.isdir(file_or_dir): #If file_or_dir is a directory:
		dir_children = os.listdir(file_or_dir) #Get all directory children (files or more directories)
		for item in dir_children: #Loop through children
			extract_text(os.path.join(file_or_dir, item)) #Append child's name to current path and recurse until a file is found
	else: #if the parameter is a file (base case)
		file = open(file_or_dir) #open the file
		accum_text = "" #This is the file's text
		for line in file.readlines(): #Loop through file
			accum_text += line #Accumulates text from the file
		accum_text = format_text(accum_text) #Calls this method to remove \t's and \n's
		text[file_or_dir] = accum_text #Store the text with its filepath as the key
