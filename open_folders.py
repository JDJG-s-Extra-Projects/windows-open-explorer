import subprocess
import os
import time
import pathlib

txt = ""
# put your txt's name with the information in there.

file_path = os.path.realpath(__file__)
current_path = pathlib.PurePath(file_path)
current = current_path.parent
with open(f"{current}/{txt}") as file:
	directories = file.readlines() 

for dir in directories:
	if dir == "\n" or not dir:
		print("Found New line skipping also possible empty str")
		print(dir)
		continue

	Path = pathlib.PurePath(dir)
	os.system(f"explorer {Path}")
	time.sleep(2)
	print(f"opened {Path}")
	

input("please enter to exit")
print("done")
