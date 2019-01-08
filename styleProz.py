import sys

def main(files):
	for x in files:
		with open(x) as file: # Use file to refer to the file object
			print("processing file: ", x);
			i = 1
			for line in file:
				indentation = len(line) - len(line.lstrip(' '))
				if(indentation % 4 != 0) :
					print("{0} line: {1} wrong indentation by {2} spaces".format(x, i, indentation))
				
				j = 0
				for char in line:
					if(char == "\t"):
						print("{0} line: {1} tabulator used on col {2}".format(x, i, j))
					if(ord(char) > 127):
						print("{0} line: {1} forbidden character used on col {2} - {3}".format(x, i, j, char))
					j = j + 1
				
				
				
				i = i + 1
	 
if __name__ == '__main__' :
	if(len(sys.argv) < 2):
		print("no files given - exiting")
	else :
		main(sys.argv[1:])