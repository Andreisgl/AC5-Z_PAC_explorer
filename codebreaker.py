# Programa rápido para descoberta de padrão


# List of characters in hex
# buddy = 0x42 0x55 0x44 0x44 0x59



term_character_list = [0x42, 0x55, 0x44, 0x44, 0x59]
offset_values_list = []
#character_test_range = [0x41, 0x5A]
character_test_range = [0x1, 0x7F]
all_searches_list = []

output_file = './search_terms.txt'

def find_smallest_number():
    return min(term_character_list)

def add_number_to_whole_list(number, list):
    aux_list = []
    for index in range(len(list)):
        aux_list.append(list[index] + number)
    return aux_list


min_term = find_smallest_number()

for index in range(len(term_character_list)):
    offset_values_list.append(term_character_list[index] - min_term)

#
#


for number in range(character_test_range[0], character_test_range[1]):
    aux_list = add_number_to_whole_list(number, offset_values_list)
    
    all_searches_list.append(aux_list)


search_type_hex = [0x73, 0x74, 0x72, 0x69, 0x6E, 0x67, 0x5C]
newline_list = [0x0A]

with open(output_file, 'wb') as OTPF:
    for index in range(len(all_searches_list)):
        see = all_searches_list[index]
        #see2 = search_type_hex + see + newline_list
        see2 = see + newline_list
        OTPF.write( bytearray(see2) )


print(term_character_list)
print(min_term)
print(character_test_range)
print(offset_values_list)


