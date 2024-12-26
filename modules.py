import random

# extract a random number based on the number of digits we want
def random_number(num_digits):
    #Create a list of number which will be part of the extracted number
    list_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #Create a null string
    string_extracted_number=""
    #Append random number in string
    for index in range(num_digits):
        string_extracted_number = string_extracted_number + str(random.choice(list_number))
    #return the random number
    return string_extracted_number

# return
# Pico    One digit is correct but in the wrong position.
# Fermi   One digit is correct and in the right position.
# Bagels  No digit is correct.
winning_output = "Congratulations! You found the number"
def output(number, rand_number):
    #if we found the rand_number return winning_output
    if number == rand_number:
        return winning_output
    #create a null list. We will put pico/fermi/bagels for each digit of number
    clues = []
    #loop to fill the list clues
    for i in range(len(number)):
        # One digit is correct but in the wrong position.
        if  number[i] == rand_number[i]:
            clues.append('Fermi')
        # One digit is correct but in the wrong position.
        elif number[i] in rand_number:
            clues.append('Pico')
    #No digit is correct.
    if len(clues) ==0:
        return 'Bagels'
    else:
        #shuffle so we don't give away information away
        clues.sort()
        #return a single string
        return ''.join(clues)


if __name__ == '__main__':
    print(random_number(4))
    print(output("123", "345"))
    print(output("515", "345"))
