import random

password = []
# Defining the type pools
symbols = ['§',"'",'"','+','!','%','/','=','(',')','$','?',':','-','_','<','>']
numbers = [0,1,2,3,4,5,6,7,8,9]
lowerCases = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCases = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Define password length by user
print("How long your password should be?")
try:
    passwordLength = int(input())
except ValueError:
    print("Invalid input at password length.")

#Random generators for each type
def randomSymbol():
    return symbols[random.randint(0,len(symbols)-1)]
def randomNumber():
    return numbers[random.randint(0,len(numbers)-1)]
def randomLowerCase():
    return lowerCases[random.randint(0,len(lowerCases)-1)]
def randomUpperCase():
    return upperCases[random.randint(0,len(upperCases)-1)]

#Defining what type of characters the user wants to input

symbolYesNo = None
print("Do you want to include symbols (-,%,!) ? \nyes/no")
try:
    symbolYesNo = str(input())
except ValueError:
    print("Input error at symbolYesNo")
assert symbolYesNo in ('yes','no'),'Input assert error at symbolYesNo'

numberYesNo = None
print("Do you want to include numbers? \nyes/no")
try:
    numberYesNo = str(input())
except ValueError:
    print("Input error at numberYesNo")
assert numberYesNo in ('yes','no'),'Input assert error at numberYesNo'

lowerCaseYesNo = None
print("Do you want to include lower case alphabets? \nyes/no")
try:
    lowerCaseYesNo = str(input())
except ValueError:
    print("Input error at lowerCaseYesNo")
assert lowerCaseYesNo in ('yes','no'),'Input assert error at lowerCaseYesNo'

upperCaseYesNo = None
print("Do you want upper case alphabets? \nyes/no")
try:
    upperCaseYesNo = str(input())
except ValueError:
    print("Input error at upperCaseYesNo")
assert upperCaseYesNo in ('yes','no'),'Input assert error at upperCaseYesNo'

# Determine how many and which types to include
yesNoAnswers = []
yesNoAnswers.extend((symbolYesNo,numberYesNo,lowerCaseYesNo,upperCaseYesNo))

sumOfYesAnswers = yesNoAnswers.count('yes')
if sumOfYesAnswers <= 0 or sumOfYesAnswers > 4:
    print("***Something is fishy with this dude.\n***Invalid number of 'yes' answers.\n***Quitting.")
    raise ValueError
    quit()

#generating random password
for i in range(passwordLength):
    isItGenerated = False
    while isItGenerated == False:
        typeRandom = random.randint(0, 3)
        if yesNoAnswers[typeRandom] == 'yes':
            if typeRandom == 0:
                password.append(randomSymbol())
            elif typeRandom == 1:
                password.append(randomNumber())
            elif typeRandom == 2:
                password.append(randomLowerCase())
            elif typeRandom == 3:
                password.append(randomUpperCase())
            isItGenerated = True

#converting the password to string and the printing out for the user
str(password)
generatedPassword = ''.join(str(e) for e in password)
print("Your random generated password is:",generatedPassword)
