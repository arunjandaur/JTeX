import re

#This class can parse both JSON code as well as Python lists and dicts into LaTeX
class parser():
	#Fetches the file at filepath and parses it to LaTeX
	def parse_file_to_latex(self, filepath):

		header = '\documentclass[12pt, titlepage]{article}\n\\begin{document}\n\n\\begin{itemize}\n' #Beginning of the document
		body = '' #This is where the parsed code goes
		end = '\end{itemize}\n\end{document}\n' #End of the document

		input_file = open(filepath, 'r') #Open the .json or .py file

		for line in input_file: #Loops through each line of the file
			line = line.replace('\t', '').replace('\n', '') #Remove all the tabs and new lines
			if ('[' in line) or ('{' in line): #An open delimiter indicates the start of a bulleted list
				body += '\item ${Item:}$\n' + re.sub(r'[{[]', r'\\begin{itemize}', line) + '\n' #This line substitutes {'s and ['s with \begin{itemize}, which is the beginning of a bulleted LaTeX list. Also, notice that there is a \item called "Item". This is because one can't have two \begin{itemize} in a row. To avoid this, I insert the label "Item" to indicate the start of an inner bulleted list, without causing a LaTeX syntax error.
			elif (']' in line) or ('}' in line): #A closed delimiter indicates the end of a bulleted list. Hence, \end{itemize}
				body += re.sub(r'[}\]]', r'\\end{itemize}', line) + '\n'
			else:
				body += '\item $' + line + '$\n' #This is the typical case, where an item is surrounded by the LaTeX syntax for making a bullet point.
	
		body = re.sub(r'"(.*?)"', r'{\1}', body).replace('#', '\#').replace(',', '') #This is another regex command. LaTeX uses {} to denote strings, while JSON and Python use "". This regex replaces "" with {} by finding all characters (hence, the .*), making sure it's non greedy (hence, the ?), that fit in between two double quotes (hence, the double quotes around the (.*?)). The parentheses allow me to reference the string in between the quotes, which allows me to preserve it and reference it with a '\1' and then surround that \1 with { and }. We also want to get rid of the commas and escape the pound sign.

		#Uncomment the following line to have support for .py files
		#output_filepath = filepath = replace('.py', '.tex')

		output_filepath = filepath.replace('.json', '.tex') #I want the LaTeX file to have the same name as the original file passed in, which is why only the extension is replaced.
		latex_file = open(output_filepath, 'w') #Opens the filepath with .tex ending, which creates a new .tex file.
		latex_file.write(header + body + end) #Concatenates and writes the LaTeX code into the file.
		latex_file.close() #Close the file. We're done!
