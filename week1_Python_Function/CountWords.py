# Count words from file

def count_words(file_path):
    '''This function counts the words from a file'''
    word_count = {}  # Create an empty dictionary to store word counts
    with open(file_path, "r") as file:  # Open file in read mode and automatically close it after use
        for line in file:  # Iterate through each line in the file
            words = line.split()  # Split the line into words using whitespace as delimiter
            for word in words:  # Loop through each word in the current line
                word = word.lower().strip('.,!?\':;')  # Convert to lowercase and remove punctuation marks
                word_count[word] = word_count.get(word, 0)+1  # Increment word count (add 1 if exists, else start at 0)

    return word_count  # Return the dictionary containing all words and their frequencies


# Calling function
filepath = "Sample.txt"  # Specify the file path to read
word_frequency = count_words(filepath)  # Call the function and store the result
print(word_frequency)  # Print the word frequency dictionary