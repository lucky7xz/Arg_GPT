def maybe():
    return 1



import math
import random
import glob

def split_text(text, max_length):
    # Calculate the number of splits needed to create strings of roughly equal length
    num_splits = math.ceil(len(text) / max_length)

    # Calculate the length of each split
    split_length = len(text) / (num_splits)

    # Initialize variables to keep track of the current string and its length
    current_str = ""
    current_length = 0

    # Initialize an empty list to store the resulting strings
    result = []

    # Loop through each character in the text
    for i in range(len(text)):
        # Add the current character to the current string
        current_str += text[i]
        current_length += 1

        
        if current_length >= split_length:
            # check if space
            if text[i] == " ":
                # Add the current string to the result
                result.append(current_str)
                # Reset the current string and its length
                current_str = ""
                current_length = 0
            
            else:
                # keep going
                continue

    return result            
            




# read the file

def read_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return text



text = read_file('data_in/small.en/borrowed_future_wav_text/RM3387691770.txt')
splitz = split_text(text, 7000)

#for result in splitz:
   # print(result, "\n\n\n")

#for result in splitz:
 #   print(len(result))