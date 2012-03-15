# Please note the use of with-as to open the file.
# It forms another block of code, where we use 
# our file and the file is automatically closed 
# once the block ends.
# For example the file f is closed after executing 
# the print statement here.

try:
	with open('filename', 'r') as f:
		print f.read()

except IOError:
	print "no such file exists"