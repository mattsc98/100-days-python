
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
NATO_PATH = 'Day 26\\NATO-alphabet-start\\NATO-alphabet-start\\nato_phonetic_alphabet.csv'
nato_data_frame = pandas.read_csv(NATO_PATH)

nato_data_dict = {row.letter : row.code for (index, row) in nato_data_frame.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

word_split = [nato_data_dict[letter] for letter in user_word]

print(word_split)