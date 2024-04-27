#a program that reads in a text file and outputs
# the number of e's in it contains
#Author : Andre Machado


from genericpath import isfile


FILENAME = "moby-dick.txt"

if not isfile(FILENAME): #cheking if the file not exist
    print("File does not exist")
    exit(1) #helps to terminate the code and avoid futher execution
else:
    print("File exists")
    def read_number(letter): #using letter as a parameter
        #encoding="utf-8" ensures that python will correctly decode, avoiding the UnicodeDecodeError
        with open(FILENAME, "r", encoding="utf-8") as f: 
            number = f.read()
            return number.count(letter) #counts how many times the variable appears
    num = read_number("e") #call the function to count the letter 'e'
    
    def read_title(): #function to read the title from the file
        with open(FILENAME) as f:
            title = f.readline().strip() #read the first line of file and remove the whitespaces
            return title
    title = read_title() #call the function to read it

    print(title)
    print(num)