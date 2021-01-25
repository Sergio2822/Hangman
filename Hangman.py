##Codigo creado por: SSH
##Para entender la OOP en Python


import random
from country_list import countries_for_language
lifes = 4

class word:
    def __init__ (self):
        self.word_list=[]
    
    def select_word (self,array_number):
        if array_number == 1:
            countries = dict(countries_for_language('en'))
            for i in countries.values():
                self.word_list.append(i)
            random_number = random.randint(0 , len(self.word_list))
            random_word = self.word_list[random_number]
            return random_word.lower() 
    
    def split(self,word):
        return [char for char in word]  

    def compare (self, letter, word):
        word_split = self.split(word)
        position = 0
        position_array = []
        for i in word_split:
            if i == letter:
                position_array.append(position)
            position +=1
        return letter, position_array



class lines_array:
    def __init__(self):
        self.lines_word= []
    
    def create(self, letter_array):
        for i in range (0, len(letter_array)):
            if letter_array[i] == " ":
                self.lines_word.append(" ")
            else:
                self.lines_word.append("_")
        return self.lines_word

    def update (self, letter, position_array, times):
        for i in range (0,times):
            self.lines_word[position_array[i]] = letter
        return self.lines_word



if __name__ == '__main__':
    word = word()
    random_word = word.select_word(1) # Choose a random word
    split_word = word.split (random_word)
    print(random_word)
    lines_array = lines_array()
    lines_created = lines_array.create(random_word)# Creates the lines according to the word spaces
    print(lines_created)
    while lifes > 0:

        player_guess = input ("Elige una letra: ") # Player letter input
        letter, position_array = word.compare(player_guess,random_word) #Compare letter with word
        if len(position_array) == 0: 
            lifes -= 1
        lines_updated = lines_array.update(player_guess,position_array,len(position_array))
        if split_word == lines_updated:
            print("Congrats, you won!")
            break
        print(lines_updated)
        print(lifes)
    if lifes == 0:
        print ("Sorry, Game over :(")


   




