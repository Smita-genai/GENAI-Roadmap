"""
File Operations Learning Module

This module demonstrates various file handling operations in Python including:
- Reading files (whole file, line by line)
- Writing files (overwriting, appending)
- Binary file operations
- File copying
- Text analysis (line, word, character counting)
- File reading and writing simultaneously using 'w+' mode
"""

import os


# ============================================================================
# LEARNING EXAMPLES (Uncomment to run individual examples)
# ============================================================================

'''
## 1. Read a whole file
with open("StoryFile.txt", "r") as file:
    content = file.read()
    print(content)


## 2. Read a file line by line
with open("StoryFile.txt", "r") as file:
    for line in file:
        print(line.strip())

## Write a file (overwriting)
with open("StoryFile.txt", 'w') as file:
    file.write("Welcome to Wonderland!.\nHope you enjoy the provided features.\nThanks for visiting!")
   
## Write a file without overwriting
with open("StoryFile.txt", "a") as file:
    file.write("\nWe hope you will visit next time for extra adventure!") 

## Writing list of lines 
lines = ["\nFirst line\n", "Second Line\n", "Third Line"]
with open("StoryFile.txt", "a") as file:
    file.writelines(lines)       


## Operations on Binary File
data = b'\x00\x01\x02\x03\x04'

with open("example.bin", "wb") as file:
    file.write(data) 

# Reading Binary File
with open("example.bin", "rb") as file:
    content = file.read()
    print(content)    

## Read from a source text file and write content to destination file
## copying a text file
with open("StoryFile.txt", "r") as file:
    content = file.read()

with open("DestinationFile.txt", "w") as file:
    file.write(content)                        


## Read a text file and count number of lines, words and characters

# 1. Count number of lines from text file
LineCount = 0
with open("StoryFile.txt", "r") as file:
    for line in file:
        LineCount += 1

print(LineCount)

# 2. Count number of words from a file
WordsCount = {}
with open("StoryFile.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower().strip('!.')
            WordsCount[word] = WordsCount.get(word, 0) + 1

print(WordsCount)

# Count characters from a file
CharCount = {}
with open("StoryFile.txt", "r") as file:
    for char in file.read():
        CharCount[char] = CharCount.get(char, 0) + 1

print(CharCount) 

'''

# ============================================================================
# MAIN EXAMPLE: File Reading and Writing with 'w+' Mode
# ============================================================================

def demonstrate_file_operations():
    """Demonstrates reading and writing to a file simultaneously using 'w+' mode."""
    
    # Open file for both Writing and reading using 'w+' mode
    with open("DestinationFile.txt", "w+") as file:
        # Write content to file
        file.write("Hello User 1\n")
        file.write("Welcome to Python Programming!\n")
        
        # Move the cursor to beginning of the file
        file.seek(0)
        
        # Read and display content
        content = file.read()
        print(content)


if __name__ == "__main__":
    demonstrate_file_operations() 
