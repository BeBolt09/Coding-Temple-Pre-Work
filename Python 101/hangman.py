from faker import Faker

fake = Faker()
random_word = fake.word()
word_to_guess=str(random_word)
#make a new list to enter letters that were found by user
guessing_list=[]
#now we have a word and we have to convert it to a list of characters
#and add an underscore to the guessing list so the user knows how many letters it is
char_list=[]
for char in word_to_guess:
    char_list.append(char)
    guessing_list.append('_')
#now we have a list of characters that we can use to guess letters
print(guessing_list)

count=0
#make a while loop to keep guesses going until equal
while guessing_list!=char_list:
    guess=input('Guess a letter')
    #now make a if statement to check if the letter is inside the list
    for c in range(len(char_list)):
        if guess==char_list[c]:
            print('You Found a letter !')
            guessing_list[c]=char_list[c]
            print(guessing_list)
    count=count+1

print('Congradulations ! You guessed the word : '+ word_to_guess +' in '+str(count)+' tries')