#WARNING: UNFINISHED! DO NOT USE!

def class smart_parser():
	def parse_file_to_visual_latex(self, filepath):
		header = '\documentclass[12pt, titlepage]{article}\n\\begin{document}\n\n' #Beginning of the document
		body = '' #This is where the parsed code goes
		end = '\end{document}\n' #End of the document

		input_file = open(filepath, 'r') #Open the .json or .py file

		
