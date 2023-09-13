#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
LETTER_PATH = 'Day 24\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt'
NAMES_PATH = 'Day 24\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Names\\invited_names.txt'
OUTPUT_FOLDER = 'Day 24\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Output'
PLACEHOLDER = "[name]"


with open(NAMES_PATH, "r") as data:
    names = [name.strip() for name in data.readlines()]

with open(LETTER_PATH) as data:
    letter_conents = data.read()
    for name in names:
        new_letter = letter_conents.replace(PLACEHOLDER, name)
        output_file = OUTPUT_FOLDER + f"letter_for_{name}"
        with open(output_file, "w") as ltr_send:
            ltr_send.write(new_letter)



