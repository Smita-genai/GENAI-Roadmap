## Find the Longest Word from User Input

# Get user input and convert it into a list of words
# The input should be comma-separated words
words = list(map(str, input("Enter list of words: ").split(",")))
length = len(words)  # Store the total number of words in the list


def longest_word():
    """This function finds and returns the longest word from the list"""
    max = words[0]  # Initialize max with the first word
    for i in range(0, length):  # Iterate through each word in the list
        if len(words[i]) > len(max):  # Compare length of current word with max word
            max = words[i]  # Update max if current word is longer
    return max  # Return the longest word found
          

# Call the function and print the result
print(longest_word())


