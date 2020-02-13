import sys;
import json;
import time;
import requests;

class Pynote:
	def __init__(self, datafile = "data.json",website = None,username = "mattiwos"):
		self.datafile = datafile
		self.website = website
		self.username = username
	def addnote(self,arg):
		self.arg = arg
		print("add note {}".format(self.arg[1:]));
		self.description = ""
		for i in range(len(self.arg) -1):
			self.description += self.arg[i+1] + " "

		print(self.description)	
		
		
		with open(self.datafile, "r", encoding='utf-8') as read_notes:
			self.data = json.load(read_notes);

			with open(self.datafile,"w",encoding='utf-8') as write_notes:	
				print(len(self.data))	
				self.data[len(self.data)] = {
					"user": self.username,
					"Time": time.asctime(),
					"Description": self.description
				}
				json.dump(self.data,write_notes,indent=2)
				
	def listnotes(self):
		with open(self.datafile, "r") as self.read_notes:
			self.data = json.load(self.read_notes);
			for i in range(len(self.data)-2):
			 	print( "List: {}".format(self.data[i:i+1]) )

	def deletenote(self):
		pass

if __name__ == '__main__':
	foo = Pynote()
	print(sys.argv[1])

	if sys.argv[1] == "-a":	
		foo.addnote(sys.argv[1:]); 
	if sys.argv[1] == "-l":	
		foo.listnotes(); 
	if sys.argv[1] == "-d":	
		foo.listnotes(); 
