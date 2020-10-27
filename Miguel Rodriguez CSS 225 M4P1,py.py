#Miguel Rodriguez
#CSS 225
#October 24,2020
#Lab Activity 4

#This program will take the hours in time between 0-23.
#This will also tell you how many hours the user will have to wait.
#It will also print what the time between 0-23 hours after the user has finished waiting.
currentTimeStr = input("What the current time is in 0-23 hours?")
waitTimeStr = input("How many hours would the user decide to wait?")

currentTimeInt = int(currentTimeStr)
waitTimeInt =int(waitTimeStr)
#The issue that this had was that this did not had the modulo which was needed.
#This helped restart after the final 24th hour which didn't go past the last hour.
finalTimeInt= (currentTimeInt + waitTimeInt) /24
print(finalTimeInt)
