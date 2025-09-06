import random
import string

def genPass(length=12):
    #step 1: make a pool of characters
    characters = string.ascii_letters + string.digits + string.punctuation
    #step 2: pick out length of random characters and join into a string
    password = ''.join(random.choice(characters) for _ in range(length))
    # return it
    return password

while True:
    #ask how long password should be
    length = input('enter password length (or "q" to quit):')

    if length.lower() == 'q':
        print('Goodbye!')
        break # end loop

    if length.isdigit():
        length = int(length) #convert into number
        print('Generated password is:', genPass(length))

    else:
        print('please enter a valid number or "q" to quit.')
    
