#WARNING: UNFINISHED! DO NOT USE!
import json
import re

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
        type_str = self.attributes[JsonKey("type")].get_value().split(".")[-1]
        ps_type = lookup(ps_obj_str)
            
        x = self.attributes[JsonKey("x")].get_value()
        y = self.attributes[JsonKey("y")].get_value()
            
        latex_str = "\\begin{{0}}\n STUFF \\end{{0}}\n".format(ps_type)

    def __str_(self):
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

def parse(json_obj):
    return str(json_obj)

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

def preprocess(json_text):
    return json.loads(json_text)

def scan(filepath):
    json_file = open(filepath, 'r')
    return json_file.read()

def main(filepath):
    json_text = scan(filepath)
    py_obj = preprocess(json_text)
    json_obj = tokenize(py_obj)
    pstricks = parse(json_obj)
