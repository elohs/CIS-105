# Ethan Lohs
# 4/18/2021
# Week12-Assignment2

# This program reads a file in two different ways. First, it reads
# the entire file. It then reads the first three lines of the file.

# Here the function is created that reads the entire file.
def read_whole_file():
    # Here the file is opened in read mode.
    input_file = open('names.txt' , 'r')

    # Here a variable is assigned to represent the content of the file.
    names_content = input_file.read()

    # The file is closed here.
    input_file.close()

    # The entire content of the file is displayed.
    print(names_content)

# Function that reads only the first three lines of the file.
def read_lines():
    # Here the file is opened in read mode.
    input_file = open('names.txt' , 'r')

    # This is where the three variables are created and assigned to
    # represent the first three lines in the file.
    line1 = input_file.readline()
    line2 = input_file.readline()
    line3 = input_file.readline()

    # Here the file is closed.
    input_file.close()

    # This is where the data from the first three lines is displayed using
    # the variables that represent them. end='' is used to suppress new 
    # lines being displayed.
    print(line1 , end='')
    print(line2 , end='')
    print(line3 , end='')

# This is where the main body of the program begins.

# The function that reads the entire file is called.
read_whole_file()  

# The function that reads the first three lines in the file is called.
read_lines()
