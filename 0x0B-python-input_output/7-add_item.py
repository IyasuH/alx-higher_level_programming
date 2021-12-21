#!/usr/bin/python3
"""import modules"""
import sys
import os.path

"""adds all arguments to a python list and then save them to afile"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file0 = "add_item.json"
if os.path.isfil(file0):
    json_file0 = load_from_json_file(file0)
    json_file0 += sys.argv[1:]
    save_to_json_file(json_file0, file0)
else:
    save_to_json_file(sys.argv[1:], file0)
