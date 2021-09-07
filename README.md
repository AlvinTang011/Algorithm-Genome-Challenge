# Algorithm-Genome-Challenge
Team Challenge to Resolve a Genome Sequence Search as efficiently as possible

readme file for Genome Sequence Search.
Project created by Team SSP1-2 - Alvin, Jing Hong, Nasran, Aaron, and Ashwin.


# PREREQUISITES

Python version 3.7


# INTRODUCTION

The program intends to return all the positions (indexes) of exact occurrences
of the query in the genome sequence via 2 search algorithms - Brute force
method and First-Last Pattern Matching. If there is no any exact match, the
program will return "No Occurrence". This information includes the time taken
for the algorithm to run the two searching algorithms. The user can select 5
options after selecting the file and query sequence they want to analyze - 
the 2 searching methods, change their query sequence, change the file that
the user wants to analyze or quit the program.


##LAUNCH##

Language used: Python version 3.7
Module used: time

Main file to run program: genome_sequence_search

NOTE: Double clicking to run the file will work.

**Ensure that the genome files are in fna type. The genome files are to be
placed in the same folder, as per your genome search program for the program
to work**


# DETAILED DESCRIPTION

Main Menu message prompts user to input 1 to select the file the user wants 
to analyze or input 2 to quit the program.

In case the user inputs an invalid option, the user will be prompt to 
reinput their choice.

After entering 1 as the input, the user will be prompt to type the file's
name that the user wants to analyze.

In the event that the file does not exist, the program will prompt the user
that the file does not exist and asks for the user input again.

If the user selects 2, the program will terminate.

Another message will prompt user to input the desired query sequence that
they want to search for.

Upon entering the query sequence, the user will have 5 options for choose:
the Brute Force method, the First-Last Pattern Matching algorithm, changing
their query sequence, going back to the main menu to change the genome file
or quit the program.

By entering 1, the program will print out the exact occurrence of the query
sequence in the file as well as the time taken for the algorithm to run
under the Brute Force method.

Upon entering 2, the program will print out the exact occurrence of the
query sequence in the file as well as the time taken for the algorithm to
run under the First-Last Pattern Matching algorithm.

Inputting 3 will bring the user back to where the user can re-input their 
desired query sequence.

Option 4 will bring the user back to the main menu so that the user can
select a different genome file to analyze.

If the user is done with what they want to do, the user can select option 5
to terminate the program.

However, if the user does not input any of the above options, the program
will ask for the user input again between the option 1 to 5.


# ACKNOWLEDGEMENTS
The Python Standard Documentation and
Google.
