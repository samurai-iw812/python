import pathlib
import os

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

#########################################
#cheack if the file exists it checks the permissions of the file
xpath=pathlib.Path("/python/sec573/defense/fileoperations/test.txt")
xpath.exists() #checks if the path exists
xpath.is_file() #checks if the path is a file
xpath.is_dir() #checks if the path is a directory

#check with os
os.path.exits(xpath) #do it any way 

##########################################
#obtain a listing of a dir with pathlib.Path.glob()
print(list(pathlib.Path.glob("/python/sec573/defense/fileoperations")))

[str(eachpath) for eachpath in pathlib.Path.glob(xpath) if eachpath.is_file()] #to see only the files in the directory

#with os.listdir()
os.listdir(xpath) #to see the files in the directory

##########################################
#supporting wildcards with glob
import glob
glob.glob("/python/sec573/defense/*/*.txt") #to see the files in the directory

##########################################
#finding files with os.walk()
drv = list(os.walk("/python/sec573/defense/fileoperations"))
for root, dirs, files in drv:
    print(root)
    print(dirs)
    print(files)

##########################################
#finding files with pathlib.Path.walk()
for root, dirs, files in pathlib.Path.walk(xpath):
    print(root)
    print(dirs)
    print(files)

##########################################
#reading gzip compressed files
import gzip 

gz = gzip.open(xpath, "rt"
)
for line in gz:
    print(line)
gz.close()
for eachfile in pathlib.Path.glob(xpath).glob("*.gz"):
    fc=gzip.open(readfile).read()
    print(eachfile.name,"-",fc[:40])
    
