# Ethan Lohs
# 4/18/21
# Week12-Assignment1

# This program that does two things. First it creates a file containing a list of names.
# Later it reopens this file and appends additional names to this list.

# Function that creates and adds the initial content of the file.
def file_creation():

    # Here the file is opened
    name_file = open("names.txt" , "w")

    # Here the names are added to the file.
    name_file.write('Shaggy\n')
    name_file.write('Scooby-Doo\n')
    name_file.write('Daphne\n')
    name_file.write('Velma\n')
    
    # File is closed here.
    name_file.close()

# This is the function that edits the file adding two additional names.
def file_edit():
    # Here the file is opened.
    name_file = open('names.txt' , 'a')

    # The additional names are appended to the file.
    name_file.write('Fred\n')
    name_file.write('Scrappy\n')

    # The file is closed.
    name_file.close

# This is where the main body of the program begins.

# Here the function that creates the file is called.
file_creation()

# Here the function that edits the file is called.
file_edit()


