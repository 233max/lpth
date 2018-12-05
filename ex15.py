# from sys module (system-specific parameters and functions), import argv
from sys import argv

# setup variables to instore argv in command line
script, filename = argv

# open dominated txt file
txt = open(filename)

# print format string with variable filename
print(f"Here's your file {filename}:")
# readin the content in variable txt
print(txt.read())

txt.close()

# ask user type in file name again, with > prompt
print("Type the filename again:")
file_again = input("> ")

# open file 
txt_again = open(file_again)

# printout the txt been read in 
print(txt_again.read())
txt_again.close()