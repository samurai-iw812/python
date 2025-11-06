import re

print(re.findall(rb"\w",b"abc")) #regular expression for raw bytes

print(re.findall(".","a 1b 2c3")) #match any character

print(re.findall("\\d","a1b2c3")) #match any digit

print(re.findall("\\D","a1b2c3")) #match any non-digit

print(re.findall("\\d.","a1b2c3d")) #match any digit followed by anything

print(re.findall("\\w","a1 ! 2w b3-")) #match any word character

print(re.findall("\\w \\w","a1b2c3d")) #match two word character

print(re.findall("^ \\w \\w","a 1 b2 c3d")) #match two character at the beginning of string

print(re.findall("\\w \\w$","a1 b2c3 d")) #match two character at the end of string

print(re.findall("\\b\\w\\w\\b","a1b 2c 3d")) #match two word chars at the word boundary

print(re.findall(r"\b\w\w\b","a1 b2c 3d")) #the same but with raw string

print(re.findall(r"\w\s","a 1b 2c3")) #match a word character followed by space

print("#################################################")
#################################################
#logical or statement
x=re.findall(r"(0[1-9]|1[0-2])", "12/25/00 13/09/99") #months between 01 and 12
print(x)

y=re.findall(r"(0[1-9]|[1-2][0-9]|3[0-1])", "12/25/00 13/09/99") # and days from 01 to 31
print(y)

print(re.findall("(?:0[1-9]|1[0-2])/(?:0[1-9]|[1-2][0-9]|3[0-1])/\d\d", "12/25/00 13/09/99")) #lets put them togther

