import random

print('='*15,'WELCOME TO NUMBER GUESS GAME.','='*15)

top_num=input("Enter the Max Range(0-Number) You want to Guess:")

if top_num.isdigit():
    top_num=int(top_num)

    if top_num <=0:
        print('Plz Enter the number larger than 0 next time.')
        quit()
else:
    print('plz type a number next time:')
    quit()

random_num=random.randint(0,top_num)
guess=0

while True:
    guess+=1
    user_guess=input("Make a guess:")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('plz Enter Number next time')
        continue
    
    if user_guess==random_num:
        print('You got it!')
        break
    elif user_guess>random_num:
        print('You guess Bigger try smaller!')
    else:
        print('You guess smaller try bigger!')
print(f'You got it in {guess} Gusses.')
print('='*20,'THANK YOU WELCOME AGAIN','='*20)