#Miguel Rodriguez
#October 24,2020
#CSS 225
#Lab

#This program will take a user's password and print it as an apporpiate message.
#The 'in' keyword will check to see if a value exists somewhere in any other string that is given.

#I removed the 'in' code because it was telling me there was an issue.
#The issue was that it would give me a response when given a wrong password.
greeting =input("Hello,pirate! What is the password?")
if greeting == ("Arrr!"):
    print ("Go away, you pirate.")

    else:
        print("Greetings, pirate hater!")
        
