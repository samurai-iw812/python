import pathlib

x=pathlib.Path.cwd() #gets the current working directory
print(x)

y=pathlib.Path.home() #gets the home directory
print(y)

x= x/ "test.txt" #adds the file name to the path
print(x)

print(x.resolve()) #resolves the path to an absolute path

print(x.parent) #gets the parent directory of the path

print(x.name) #gets the name of the file    

print(x.parts) #gets the parts of the path

print(x.anchor) #gets the anchor of the path

print(x.parent.parent) #gets the parent of the parent directory

print(str(x)) #converts the path to a string

file_path=pathlib.Path("/python/sec573/defense/fileoperations/test.txt")
file_path.write_text("this is test file") #writes the text to the file
print(file_path.read_text()) #reads the text from the file

file_path.write_bytes(b"this is test file") #writes the bytes to the file
print(file_path.read_bytes()) #reads the bytes from the file



