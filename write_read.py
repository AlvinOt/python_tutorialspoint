#!/usr/bin/python3
import sys

# Define file_finish variable as an empty string
file_finish = "DONE"

try:
    # open file stream
    file_name = input("Enter filename: ")
    if len(file_name) == 0:
        print("Next time please enter something")
        sys.exit()
    file = open(file_name, "w")
except IOError:
    print("There was an error writing to", file_name)
    sys.exit()

print("Enter '{}' When finished".format(file_finish))

# Initialize file_text variable
file_text = ""

while file_text != file_finish:
    file_text = input("Enter text: ")
    if file_text == file_finish:
        # close the file
        file.close()
        break
    file.write(file_text)
    file.write("\n")

file.close()

try:
    file = open(file_name, "r")
except IOError:
    print("There was an error reading file")
    sys.exit()

file_text = file.read()
file.close()

print(file_text)
