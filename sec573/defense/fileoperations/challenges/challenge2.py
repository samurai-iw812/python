#write code to print the number of lines in each log file
import pathlib

x=pathlib.Path("/var/log").rglob("*.log")

for eachfile in x:
    with open(eachfile, "r") as file:
        lines=file.readlines()
    print(f"{eachfile} -> {len(lines)} lines")