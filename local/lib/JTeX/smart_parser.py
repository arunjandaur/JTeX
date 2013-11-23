#WARNING: UNFINISHED! DO NOT USE!
import json

class JsonTerminus(object):
	def __init__(self, value):
		self.value = value

	def get_value(self):
		return self.value

	def __str__(self):
		return "(Terminus {0})".format(self.value)

class JsonKey(object):
	def __init__(self, key):
		self.key = key

	def get_value(self):
		return self.key

	def __str__(self):
		return "(JsonKey {0})".format(self.key)

class JsonObject(object):
	def __init__(self):
		self.attributes = {}

	def add(self, key, value):
		self.attributes[key] = value

	def __str__(self):
		result = "(JsonObject\n"
		for attr in self.attributes:
			result += "\t{0} {1}\n".format(str(attr), str(self.attributes[attr]))
		result += ")\n"
		return result

class JsonList(object):
	def __init__(self):
		self.json_objects = []

	def add(self, json_obj):
		self.json_objects.append(json_obj)
	
	def __str__(self):
		result = "(JsonList\n"
		for obj in self.json_objects:
			result += "{0}\n".format(str(obj))
		result += ")\n"
		return result

def parse(json_token):
	#Todo

def tokenize(py_obj):
	if type(py_obj) == list:
		json_list = JsonList()
		for elem in py_obj:
			json_list.add(tokenize(elem))
		return json_list
	if type(py_obj) == dict:
		json_object = JsonObject()
		for key in py_obj:
			json_object.add(JsonKey(key), tokenize(py_obj[key]))
		return json_object
	else:
		return JsonTerminus(py_obj)

def scan(filepath):
	json_file = open(filepath, 'r')
	json_text = json_file.read()
	py_obj = json.loads(json_text)
	return tokenize(py_obj)
