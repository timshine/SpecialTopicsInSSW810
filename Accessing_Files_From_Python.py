import datetime
import os
from prettytable import PrettyTable
import re

def date_after(num_days,current_date):
    """Returns a new date for the number of days after the current date being looked at.
        Date must be entered in the form mm/dd/yyyy"""
    try:
        cur_date = datetime.datetime.strptime(current_date, '%m/%d/%Y')
    except ValueError:
        return "Please enter date as mm/dd/yyyy"
    later_date = cur_date + datetime.timedelta(days = num_days)
    return later_date.strftime('%m/%d/%Y')

def days_passed(date1, date2):
    """Returns the number of days in between two dates (date1 and date2). 
        The dates must be entered in the format mm/dd/yyyy"""
    try:
        dt1 = datetime.datetime.strptime(date1, '%m/%d/%Y')
        dt2 = datetime.datetime.strptime(date2, '%m/%d/%Y')
    except ValueError:
        return "Please enter dates as mm/dd/yyyy"
    days_passed = dt2 - dt1
    return days_passed.days

def search_for_python_files(directory):
    """Searchs for python files in a given directory
        Uses the function find_information_in_file to extract information from the python file
        The information extracted is number of classes, functions, lines and characters in the file"""
    try:
        os.listdir(directory)
    except FileNotFoundError:
        return "Invalid directory. Please try again."
    else:
        files = list()
        for file in os.listdir(directory):
            if file.endswith('.py'):
                current_path = os.path.join(directory, file)                            #adds the .py file to the current directory
                files.append((current_path, find_information_in_file(current_path)))    #appends the directory name and information to a list of files
        pt = PrettyTable(field_names = ['Directory', 'Classes', 'Functions', 'Lines', 'Characters'])
        for path, (classes, functions, lines, characters) in files:                     #prints out the list of files and information as a prettytable
            pt.add_row([path, classes, functions, lines, characters])
        return pt

def find_information_in_file(file):
    """Tries to open the file, if not returns that the file cannot be opened
        If the file is open, it returns the number of classes, functions, lines and characters in that file"""
    classes, functions, lines, characters = 0,0,0,0
    try:
        fp = open(file, 'r')                                #already found that file can be opened in search python files, check again so code can be reused elsewhere
    except FileNotFoundError:
        return "Invalid directory. Please try again."
    else:
        with fp:
            for line in fp:
                if re.match(r'^([class]+)\s', line.strip()):    #regex for 'class' followed by a space
                    classes += 1
                elif re.match(r'^[\s{4,}]?([def]+)\s', line.strip()):   #regex for 'def' followed by a space preceeded by option tab (4 spaces) for class methods
                    functions += 1
                lines += 1
                characters += len(line.strip())
        return classes, functions, lines, characters


def main():
    """Prints the prettytable for all the .py files in this folder"""
    print(search_for_python_files(r"\Users\TS\Desktop\Stevens\Work from Semesters\Fourth Semester\SSW 810\PycharmProjects\HW_8_Test"))

if __name__ == '__main__':
    main()
    