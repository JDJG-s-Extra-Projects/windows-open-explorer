import subprocess
import os
import sys
import time
import pathlib

txt = ""
# put your txt's name with the information in there.

current = pathlib.Path(__file__).absolute().parent
file_location = f"{current}/{txt}"

if not Pathlib.Path(file_location).exists():
	sys.exit(1)
	# Best solution I found was closing the file before stuff is used

with open(file_location) as file:
	directories = file.readlines() 

for dir in directories:
	if dir == "\n" or not dir:
		print("Found New line skipping also possible empty str")
		print(dir)
		continue

	Path = pathlib.PurePath(dir)

	if not path.exists():
		continue

	# possibly not needed?
	os.system(f"explorer {Path}")
	time.sleep(2)
	print(f"opened {Path}")
	

input("please enter to exit")
print("done")
