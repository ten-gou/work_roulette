import string

#creates a multiple choice input and verifies if input is accounted for
def verify(num):
    value = input().casefold()
    
    letterSelect = []
    i = 0
    while i < num:
        letterSelect.append(string.ascii_lowercase[i])
        i+=1

    if value in letterSelect:
        return value
    else:
        print("Please make a valid input!")
        verify(num) #loops the program if incorrect input


#converts letter input into number input
def numConvert(value):
    if value.isdigit() or len(value) > 1:
        print("Please make a valid input!")
        numConvert(input()) #loops the program if incorrect input
    else:
        number = string.ascii_lowercase.index(value)
        print(number)
        return number
