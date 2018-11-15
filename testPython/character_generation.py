import random

gender = ["male", "female"]
race = ["dwarf", "elf", "human", "orc","Undead"]
char_class = ["paladin", "warrior", "cleric", "mage","Death Knight"]

#def rand_char_gen():
#    player_gender = gender[random.randint(0,len(gender)-1)]
#    player_race = race[random.randint(0,len(race)-1)]
#    player_char_class = char_class[random.randint(0,len(char_class)-1)]
#    result = "you are a "+player_gender+" "+player_race+" "+player_char_class
#    return result

def rand_player_gender():
    player_gender = gender[random.randint(0,len(gender)-1)]
    return player_gender

def rand_player_race():
   player_race = race[random.randint(0,len(race)-1)]
   return player_race

def rand_player_char_class():
    player_char_class = char_class[random.randint(0,len(char_class)-1)]
    return player_char_class

def random_char_gen():
    player_gender = rand_player_gender()
    player_race = rand_player_race()
    player_char_class = rand_player_char_class()
    result = "you are a "+player_gender+" "+player_race+" "+player_char_class
    return result


name = input("please enter your name: ")
print("your name is ", str(name))
print(random_char_gen())
#for x in range (0,10,1):
#    print(random_char_gen())
    
male_count = 0
female_count = 0


for x in range (0, 100, 1):
   # print("Running For loop for " +str( x )+" time")
    result=rand_player_gender()
    if (result == gender[0]):
       male_count= male_count+1
    elif (result == gender[1]):
       female_count=female_count+1
     

#print ("A male character was created "+ str(male_count))
#print ("A female character was created "+str(female_count))


   



