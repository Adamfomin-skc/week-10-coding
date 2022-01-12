import random
number = random.randint(1,10)
print(number)


while True:   
    
    
    
    guess = int(input('Enter a number between 1 and 10: '))

    if guess == number:
        print('your guess was correct')
        print('Well done!')
        break
    else:
        print('hard luck try again')
        
print('goodbye')
