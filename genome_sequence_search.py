import time

# Bruteforce Algorithm
def bruteforce(t, p):
    a = []  # declare empty array
    n = len(t)  # set length of text to n
    m = len(p)  # set length of pattern to m
    for i in range(n - m + 1):
        j = 0
        while j < m and p[j] == t[i + j]:
            j += 1
        if j == m:
            a.append(i + 1)  # add the position of a matched sequence to the array(position = index + 1
    return a


# FLPM Method
def flpm(text, pattern):
    n = len(text)
    m = len(pattern)
    window = []
    result = []
    # pre-processing phase
    for i in range(n - m + 1):
        # if first and last char of pattern matches with ith and (i+m-1)th char of text
        if text[i] == pattern[0] and text[i + m - 1] == pattern[m - 1]:
            # record the index in array
            window.append(i)

    # matching phase
    for i in range(len(window)):
        # x = first match of first char in the text
        x = window[i]
        for y in range(1, m - 1):
            # start matching from the 2nd index of the pattern to the next char of the text
            # match until the 2nd last char of pattern == 2nd char of the pattern
            if pattern[y] != text[x + y]:
                break
            
        if y == m - 2:
            result.append(x + 1) # Align the index accordingly

    return result


# Occurrence Printing
def printOcc(arr):
    if len(arr) > 0:
        newstr = ""
        for x in arr:
            newstr += str(x)
            newstr += ", "
        newstr = newstr[:-2]  # removes the ", " at the back
        print("Occurrence found in position(s): %s\n" % newstr)
    else:
        print("No Occurrence.\n")


# Data extraction from file
def fileExtract(fileName):
    f = open(fileName + ".fna", "r")  # Allows user to open file where the genome sequence is in the same folder as the code
    fileStr = f.read()  # read file and assign data to String
    f.close()  # close file

    # Data Cleaning
    fileStr = fileStr.split('\n', 1)[-1]  # remove the first line from String
    fileStr = fileStr.replace("\n", "")  # remove linebreaks from String
    return fileStr


# Main Menu
control = 0  # Control Value for the menu to go back and forth without using 2 while loops
marker = 0   # Marker Value for file error handling
while True:
    if control == 1:  # Ignores the lines below so that user can access the other methods straight away
        pass
    else:
        if marker == 1:  # Make it more user-friendly with the file error handling as well as presentation of main menu
            pass
        else:
            print("Welcome to the Genome Sequence Search!\n")
            print("1) Select genome file to analyze")
            print("2) Quit")
            choice = input("Select option:\n")
            print("")

            if choice == 1 or choice == "1":
                pass # Move user to input the file type
            elif choice == 2 or choice == "2":
                print("Terminating Program...\n")
                time.sleep(1) # Lets user know they closed the program with the above print message
                break
            else:
                print("Invalid input. Please choose between option 1 or 2.\n") #Lets user retry their input
                continue # Bring back the main menu

        try:
            # File To use
            fName = input("Input file name(must be fna type):\n")
            print("")

            txt = fileExtract(fName)
            print(">>File loaded!\n")

        except:
            print("File does not exist. Please retype input file name.\n")
            marker = 1
            continue
        
        pat = input("Input Query Sequence:\n")
        print("")
        print(">>Query loaded!\n")


    # Allows user to select their searching method and more options to improve user-friendliness
    if control == 0 or control == 1:
        print("Select your choice of searching method:")
        print("1) Bruteforce")
        print("2) First-Last Pattern Matching")
        print("3) Return to change choice of DNA sequence")
        print("4) Return to Main Menu")
        print("5) Quit")
        choice = input("Select option:\n")
        print("")

        # Search Options
        # Brute Force Method
        if choice == 1 or choice == "1":
            startTime = time.time()  # Log time before execution of algorithm
            occArray = bruteforce(txt, pat)  # Run Search Algorithm
            endTime = time.time()  # Log time after execution of algorithm
            print("Search Algorithm(Bruteforce) was executed within %.9f seconds\n" % (endTime - startTime))

            printOcc(occArray)
            control = 1


        # FLPM Method
        elif choice == 2 or choice == "2":
            startTime = time.time()  # Log time before execution of algorithm
            occArray = flpm(txt, pat)  # Run Search Algorithm
            endTime = time.time()  # Log time after execution of algorithm
            print("Search Algorithm(FLPM) was executed within %.9f seconds\n" % (endTime - startTime))

            printOcc(occArray)
            control = 1


        # Return to change choice of Genome Sequnce to search but under same file
        elif choice == 3 or choice == "3":
            pat = input("Input New Query Sequence:\n")
            print("")
            control = 1


        # Return to Main Menu
        elif choice == 4 or choice == "4":
            control = 0 # Reprints the Menu Message
            marker = 0  # Prints the Menu Message


        # Quit Program
        elif choice == 5 or choice == "5":
            print("Terminating Program...\n")
            time.sleep(1) # Lets user know they closed the program with the above print message
            break


        # Error Handling
        else:
            print("Invalid input. Please choose between option 1 to 5.\n") #Lets user retry their input
            control = 1