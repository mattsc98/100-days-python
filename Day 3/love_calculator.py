name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

total_score = ''

true_ = 0
love = 0

name1 = name1.lower()
name2 = name2.lower()

combined_names = name1 + name2

for letter in 'true':
    true_ += combined_names.count(letter)

for letter in 'love':
    love += combined_names.count(letter)

total_score = str(true_) + str(love)
total_score = int(total_score)

if(total_score < 10 or total_score > 90):
    print(f'Your score is {total_score}, coke and mentos')

elif(40 < total_score < 50):
    print(f'Your score is {total_score}, iz good')        

else:
    print(f'Your score is {total_score}')    
