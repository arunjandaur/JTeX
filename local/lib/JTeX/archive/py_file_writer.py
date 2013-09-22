#Do not use this code. Refer to archive_info.txt

JSON_OPEN_DELIMITERS = ["[", "{"]
JSON_CLOSE_DELIMITERS = ["]", "}"]

def write_py_file(filepath, parsed_JSON_list):
        filepath = filepath.replace(".json", ".py")
        f = open(filepath, 'w')
	write_parsed_JSON(parsed_JSON_list, f, "")
	f.close()

def write_proper_type(py_val, file_obj, indent):
	if type(py_val) == unicode or type(py_val) == str:
		file_obj.write(indent + '"' + str(py_val) + '"' + ',' + '\n')
	else:
		file_obj.write(indent + str(py_val) + ',' + '\n')

def write_parsed_JSON(parsed_py_list, file_obj, indent=""):
        if type(parsed_py_list) == list:
                file_obj.write(indent + JSON_OPEN_DELIMITERS[0] + '\n')
                for item in parsed_py_list:
                        write_parsed_JSON(item, file_obj, indent + '\t')
                file_obj.write(indent + JSON_CLOSE_DELIMITERS[0] + ',' + '\n')

        elif type(parsed_py_list) == dict:
                file_obj.write(indent + JSON_OPEN_DELIMITERS[1] + '\n')
                for key in parsed_py_list.keys():
                        str_builder = indent + '\t' + '"' + str(key) + '"' + ":"
			file_obj.write(str_builder)
			
                        if type(parsed_py_list[key]) != dict and type(parsed_py_list[key]) != list:
                                file_obj.write(" ")
				write_parsed_JSON(parsed_py_list[key], file_obj)
                        else:
                                file_obj.write('\n')
                                write_parsed_JSON(parsed_py_list[key], file_obj, indent + '\t')
                file_obj.write(indent + JSON_CLOSE_DELIMITERS[1] + ',' + '\n')

        else:
		write_proper_type(parsed_py_list, file_obj, indent)
