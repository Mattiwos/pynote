
from pynote import Pynote
if __name__ == '__main__':
	foo = Pynote()
	print(sys.argv[1])

	if sys.argv[1] == "-a":	
		foo.addnote(sys.argv[1:]); 
	if sys.argv[1] == "-l":	
		foo.listnotes(); 