import sys;
import json;
import time;
import requests;



def addnote(arg):
	print("add note {}".format(arg[1:]));
	description = ""
	for i in range(len(arg) -1):
		description += arg[i+1] + " "

	print(description)	
	data = {		
		"Notess":{
			"Time": time.asctime(),
			"Description": description
		}
	}

	with open("data.json","a", encoding='utf-8') as write_note:

		json.dump(data,write_note, indent=2)



def listnotes():
	with open("data.json", "r", encoding='utf-8') as read_notes:
		data = json.load(read_notes);
		print(data);


if __name__ == '__main__':
	
	print(sys.argv[1])

	if sys.argv[1] == "-a":	
		addnote(sys.argv[1:]); 
	if sys.argv[1] == "-l":	
		listnotes(); 
