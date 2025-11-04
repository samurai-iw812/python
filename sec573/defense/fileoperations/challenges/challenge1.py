#wite code print all the files in dir just the files and thier sizes
import pathlib

x = pathlib.Path(__file__).resolve().parents[1] #get the parent directory of the current file

for eachfile in x.iterdir():
    if eachfile.is_file():
        print(eachfile.name, eachfile.stat().st_size)

    else:
        continue