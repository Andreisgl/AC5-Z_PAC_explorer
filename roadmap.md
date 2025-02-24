# ROADMAP

# Planned features
1. Add support for Little Endian and Big Endian discrimination on search terms
1. Allow for file-based search instead of only string-based
    1. Enable using files as search terms alongside the regular list by putting them into an input folder
    1. Add the prefix for the filename to indicate the type of search (binary, string, etc). The rest of the filename is just an identifier

# Intended changes
1. Rewrite code with better standards
1. Rewrite the 'results' file structure
    1. consider using JSON
    1. but an easily-readable format is necessary. Maybe it's better to write a custom format again.
        1. It has to be easy to read and easy to parse.
