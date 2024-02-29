# f = open("file handling/file.txt", "r")

# print(f.read())
# f = open("file handling/file.txt", "a")

# print(f.write("Hello! Welcome to file.txt. \n This file is for testing purposes. \n Good Luck!"))

# f.close()

# f = open("myfile.txt", "w")

import os
os.remove("myfile.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder") #only remove empty folders.

#using functions

def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt')
