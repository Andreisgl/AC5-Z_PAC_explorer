# AC File Searcher
# By Andrei_sgl @ Github

# This tool eases the researching process of AC5 and ACZ's .PAC files by
# allowing the search for specific terms and values within the files.

# For use with DATA.PAC, use death_the_d0g's ACZ_PAC_TOOLS to unpack it.

# TODO: 
# 1 - Finish the supported term formats
# 2 - Make a proper term input system, you lazy coder!


from json import encoder
import math
# from imp import SEARCH_ERROR
import os
from os import listdir
from os.path import isfile, join
import re

import textwrap

BASE_FOLDER = "./"
SEARCH_FOLDER = BASE_FOLDER + "search_folder"

search_term_file = "search_terms.txt"
search_result_file = "result.txt"

in_file_list = [] # Filenames to be searched
search_term_list = [] # List of terms to be searched
term_type_list = [] # List of type of search type for each term (string, hex, int...)

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
    
    if not os.path.exists(search_term_file):
        with open(search_term_file, 'w'):
            errormsg = "No search term file present!"

    # If any error was accused, exit program.
    if not errormsg == "":
        exit(errormsg)

def get_search_terms():
    with open(search_term_file, 'r') as STF:
        num_lines = 0
        # num_lines = sum(1 for line in STF if line.rstrip())
        for line in STF:
            if line.rstrip():
                search_term_list.append(line.rstrip("\n"))
                num_lines += 1
        print('Number of search terms:', num_lines)

# Gets and saves the files in the search folder.
def get_files_in_search():
    global in_file_list
    in_file_list = listdir(SEARCH_FOLDER)

    #for i in range(len(in_file_list)):
        
    print("Number of files: " + str(len(in_file_list)))

# Search for a term list in the file located in the chosen index.
def search_in_file(index, search_term):
    match_list = []
    with open(SEARCH_FOLDER + "/" + in_file_list[index], 'rb') as dat_file:
        dat_file_s = os.path.getsize(SEARCH_FOLDER + "/" + in_file_list[index])

        # number_of_bytes = math.floor(dat_file_s/4)

        data = dat_file.read() 
        term_type = term_type_list[index]
        search_term = search_term_list[index]
        encoded_term = term_encoder(search_term, term_type)
        occurrence_count = 0

        
        

        for match in re.finditer(encoded_term, data):
            occurrence_count += 1
            s = match.start()
            e = match.end()

            match_list.append(s)

        # Print search results in a string
        # Should this be a separate function?
        
        # If there are any occurrences of this term, record it.
        search_result_str = ""
        
        # search_result_str = in_file_list[index] + ">"
        search_result_str += search_term
        search_result_str += ":" + str(occurrence_count) + " @ "
        
        counter = 0
        for occurr in match_list:
            search_result_str += str(hex(occurr))
            counter += 1
            if counter < occurrence_count:
                search_result_str += ","

        if occurrence_count == 0:
            return -1
        return search_result_str
                
def search_term_list_in_file(index, term_list):
    # Start string for each file
    search_result_str = "\n" + "&&&" + "\n"
    search_result_str += in_file_list[index] + "\n"
    counter = 0
    empty_counter = 0
    for term in term_list:
        counter += 1
        aux = search_in_file(index, term)
        if aux == -1:
            empty_counter += 1
            if empty_counter == len(term_list):
                return -1
        else:
            search_result_str += aux + "\n"
            if counter < len(term_list):
                search_result_str += "\n"

    
    # End string for each file
    # search_result_str += "\n|||"
    return search_result_str
    
def search_term_list_in_all_files(term_list):
    
    with open(search_result_file, 'w') as result_file:
        for file in range(len(in_file_list)):
            aux = search_term_list_in_file(file, term_list)
            if aux != -1:
                result_file.write(aux)
            
# Returns term type to aid search. If not present, defaults to 'string'
def get_search_type(term):
    # Term types:
    # index- | special char | name of type
    # 0- | string\ | string
    # 1- | hex\ | hex
    # 2- | int\ | int

    encode_type = -1
    default_type = "string"

    try:
        prefix = term.split('\\', 1)[0]
        suffix = term.split('\\', 1)[1]
    except IndexError:
        prefix = "string"
        suffix = term
    if prefix == 'string':
        print('Is string!')
        encode_type = 0
    elif prefix == 'hex':
        print("Is hex!")
        encode_type = 1
    elif prefix == "int":
        print("Is int!")
        encode_type = 2

    return encode_type, suffix

def get_search_type_list():
    for index in range(len(search_term_list)):
        search_type, search_term_list[index] = get_search_type(search_term_list[index])
        term_type_list.append(search_type)

# Encodes a term based on it's type
def term_encoder(term, type):
    # Only string for now...
    if type == 0:
        return bytes(term, 'UTF-8')
    if type == 1:
        hex_size = int(len(term)/2)
        term = int(term, 16)
        #term = hex(term)
        term = int(term).to_bytes(hex_size, 'big')

        print(term)
        return term
    if type == 2:
        aux = int(term).to_bytes(4, 'little')
        
        return aux
    else:
        return bytes(term, 'UTF-8')


show_welcome_msg_instructions()
check_folders()
get_search_terms()
get_search_type_list()
get_files_in_search()

# search_in_file(0, "jooj")
# search_term_list_in_file(0, search_list)
search_term_list_in_all_files(search_term_list)

print("END!!")
