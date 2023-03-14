
import random
import glob

from preprocess import split_text, read_file

def test_text_split(max_length, ): 

    print("--- Testing text split function ---")

    bf_samples = glob.glob('data_in/small.en/borrowed_future_wav_text/*.txt')
    lex_samples = glob.glob('data_in/small.en/lex_fridman_podcast_text/*.txt')
    SW_samples = glob.glob('data_in/small.en/science_weekly_text/*.txt')

    # pick 5 random samples from each and add them to a list test_texts

    test_texts = []

    for i in range(5):
        bf = random.choice(bf_samples)
        lex = random.choice(lex_samples)
        sw = random.choice(SW_samples)

        test_texts.append(bf)
        test_texts.append(lex)
        test_texts.append(sw)

    # read the text from each file and split it into strings of length max_length
    # add the resulting strings to a list test_texts

    splitz_to_test = []

    for file in test_texts:

        text = read_file(file)
        splitz = split_text(text, max_length)

        for result in splitz:
            splitz_to_test.append(result)
        
    
    # now we test

    # a list comprehension to get the length of each string in splitz_to_test
    lengths = [len(splitz_to_test[i]) for i in range(len(splitz_to_test))]

    # list comprehension to check if each string in splitz_to_test is less than or equal to max_length
    less_than_max = [len(splitz_to_test[i]) <= max_length for i in range(len(splitz_to_test))]

    # list comprehension to check if each string is at least 75% of max_length
    at_least_half = [len(splitz_to_test[i]) >= (max_length * 0.5) for i in range(len(splitz_to_test))]

    
    if all(less_than_max):
        print("All strings are less than or equal to max_length")
    
    else:
        print("Some strings are greater than max_length")



    if all(at_least_half):
        print("All strings are at least 50% of max_length")

    else:
        print("Some strings are less than 50% of max_length")


    print("\n\nThe lengths of the strings are: ")
    print(lengths)
    print("\n\n")



def test_text_split_visual(max_len):


    pass


########## Main ##########

test_text_split(7000)