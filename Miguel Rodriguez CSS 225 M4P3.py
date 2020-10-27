#Miguel Rodriguez
#October 24,2020
#Lab Activity 4

#This code can return the mad libs text based on the user input.
#Is the code always returning the correct input?
#What do you think I did to write this code that I shouldn't done it.

def change_name(adjective):
    if adjective == 'green':
        return "The baby climbed over the green chair ."
    elif adjective == 'mysterious':
        return "The baby climbed over the mysterious chair."
    elif adjective =='narrow':
        return "The baby climbed over the narrow chair."
    elif adjective =='broken':
        return "The baby climbed over the broken chair."
    elif adjective == 'fresh':
        return "The baby climbed over the fresh chair."
    else:
        return "No adjective case found!"
#I added an  input that it can ask the user the missing adjectives.
#I fixed the sentence on the that was repeating at the top on the second problem.
 user_input = input("What is the adjective:")
 print (change_name(user_input))
 

        
