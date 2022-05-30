# AC File Searcher
# By Andrei_sgl @ Github

# This tool eases the researching process of AC5 and ACZ's .PAC files by
# allowing the search for specific terms and values within the files.

# For use with DATA.PAC, use death_the_d0g's ACZ_PAC_TOOLS to unpack it.

import math
from imp import SEARCH_ERROR
import os
from os import listdir
from os.path import isfile, join

import textwrap

BASE_FOLDER = "./"
SEARCH_FOLDER = BASE_FOLDER + "search_folder"

in_file_list = []
#file_content_list = []

term_list = ["version"] #[b'0\x00\x00\x00'] #"F-14D",

def show_welcome_msg_instructions():
    print(textwrap.fill("Ace Combat 5/Zero .PAC searcher by Andrei Segal (Andrei_sgl@ Github)", width=80))
    print("INSTRUCTIONS:")
    print(textwrap.fill("Run the program once to generate necessary folders.", width=80))
    print(textwrap.fill("Put all the files to be searched in " + SEARCH_FOLDER + ".", width=80))
    
# Checks if all necessary folders for startup exist
def check_folders():
    errormsg = ""
    # If necessary folders do not exist, create them.
    if not os.path.exists(BASE_FOLDER):
        os.mkdir(BASE_FOLDER)
    if not os.path.exists(SEARCH_FOLDER):
        os.mkdir(SEARCH_FOLDER)
    # If search directory is empty, accuse an error.
    if len(listdir(SEARCH_FOLDER)) <= 0:
        errormsg = "Search directory is empty!"
    # If any error was accused, exit program.
    if not errormsg == "":
        exit(errormsg)

# Gets and saves the files in the search folder.
def get_files_in_search():
    global in_file_list
    in_file_list = listdir(SEARCH_FOLDER)

    #for i in range(len(in_file_list)):
        
    print(in_file_list)

# Search for a term in the file contained in the chosen index.
def search_in_file(index, termlist):
    with open(SEARCH_FOLDER + "/" + in_file_list[index], 'rb') as dat_file:
        dat_file_s = os.path.getsize(SEARCH_FOLDER + "/" + in_file_list[index])

        if not dat_file_s % 4 == 0:
            input("Number of bytes not divisible by 4!")
        number_of_bytes = math.floor(dat_file_s/4)

        data = dat_file.read()
        #print(data)
        

        for term in termlist:
            
            encoded_term = bytes(term, 'UTF-8')

            first_find_index = data.find(encoded_term)
            last_find_index = data.rfind(encoded_term)
            found_ocurrences = data.count(encoded_term)
            
            if data.find(bytes(term, 'UTF-8')) != -1:
                print("!")
                #found_ocurrences += 1

    print("Searches for a list of terms in a single file")


show_welcome_msg_instructions()
check_folders()
get_files_in_search()

search_in_file(0, term_list)

print("END!!")
