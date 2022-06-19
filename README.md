# AC5-Z_PAC_explorer
 # A search tool for AC5/Z .PAC files
 
 This tool was made to facilitate the researching and modding process for Ace Combat 5\Z. It can look up on most of the game's files, mainly .PAC files (DATA.PAC, BGM.PAC, RADIOUSA.PAC, etc), extracted .dat files (from death_the_d0g's tool at https://www.moddb.com/games/ace-combat-zero-the-belkan-war/tutorials/ace-combat-zero-the-belkan-war-importing-aircraft-from-ac5-the-unsung-war) and find all instances of a chosen list of keywords. All occurrences wil be saved to a .txt file where the filename, search terms, number of occurrences and offsets of such will be displayed.
 
# Mode of usage:
1- Insert all files to be searched in 'search_folder'. Multiple files can be searched at the same time.

2- Input all search terms in 'search_terms.txt', each per line and their prefixes to indicate which type of search will take place.

SUPPORTED SEARCH TYPES AND PREFIXES:
- "string\" - Looks for a pure text string. If there is no prefix in a search term, it will also default to 'string'
- "hex\" - Looks for a hex value. Useful for raw searching of values of other files.
- "int\" - Looks for a int value.


3- After the search, all results will be saved on 'result.txt'. Data includes the files where the terms were found on and the offsets for each instance.

 # Example:
FILES @ 'search_folder'
0000.dat
0001.dat
0002.dat
0003.dat
0004.dat
0005.dat

SEARCH TERMS @ 'search_terms.txt':
string\F-14D
string\GRIPEN
int\5115
int\317
hex\54414E4B

RESULTS AT 'result.txt'

&&&
0000.dat
317:6 @ 0x119f0,0x13792,0x13852,0x2216a,0x22423,0x24169


&&&
0001.dat
F-14D:6 @ 0x1a1470,0x1a1490,0x1a14b0,0x1a14d0,0x1a14f0,0x1a1510

GRIPEN:6 @ 0x1a1d70,0x1a1d90,0x1a1db0,0x1a1dd0,0x1a1df0,0x1a1e10

5115:2 @ 0x70,0x5060

317:2 @ 0x19038f,0x19be5f

54414E4B:24 @ 0x1a40b0,0x1a40d0,0x1a40f0,0x1a4110,0x1a4130,0x1a4150,0x1a42f4,0x1a4314,0x1a4334,0x1a4354,0x1a4374,0x1a4394,0x1a5d35,0x1a5d55,0x1a5d75,0x1a5d95,0x1a5db5,0x1a5dd5,0x1a60f4,0x1a6114,0x1a6134,0x1a6154,0x1a6174,0x1a6194

&&&
0003.dat
317:4 @ 0x5824bb,0x58254b,0x8e6573,0x8e6603


&&&
0004.dat
317:4 @ 0x53e6cb,0x53e75b,0x8c9d93,0x8c9e23


&&&
0005.dat
317:5 @ 0x58b53b,0x58b5cb,0x5c035f,0x5c09ff,0x5c109f