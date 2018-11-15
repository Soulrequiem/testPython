#x = 1.50
#y = 2.67
#Result = x + y
#print (Result)
#print ("hello world")

#FirstArrays = [1, 2, 3]
#for FirstArray in FirstArrays:
#    print (FirstArray)

#for i in range (0, 10):
#    result = random.randint(1,20)
#   print(result)

import random
base_hit = 5
base_attack = 10
base_crit = 2

hit_to_roll = 10

def dice_roll():
    dice_roll = random.randint(1,20)
    return dice_roll

def attack_roll(base_hit, hit_to_roll,base_attack, base_crit):
    hit_roll = base_hit+dice_roll()
    if (hit_roll > hit_to_roll):
        print("You have hit the target with a roll of "+ str(hit_roll))
        print("Rolling for attack damage")
        attack_damage(base_attack,base_crit )
    else:
        print("you have missed the target with a roll of " + str(hit_roll)) 

def attack_damage(base_attack, base_crit):
    crit_bonus = base_crit+dice_roll()
    print("Rolling for bonus damage")
    print("Critical damage bonus rolled was " + str(crit_bonus))
    if (crit_bonus >= 15 and crit_bonus <=20):
        print("you have scored a crit!")
        print("you have dealt "+str(base_attack*2)+" damage to the target")
    else:
        attack = base_attack
        print("you did not score a crit")
        print("you have dealt "+str(base_attack)+" damage to the target")

print ("I'm rolling to hit")
attack_roll(base_hit, hit_to_roll, base_attack, base_crit)

