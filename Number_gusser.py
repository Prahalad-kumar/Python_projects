import random

print('🔢' + '='*10 + ' WELCOME TO NUMBER GUESS GAME ' + '='*10 + '🔢')

top_num=input("🎯 Enter the Max Range (0-Number) you want to guess: ")

if top_num.isdigit():
    top_num=int(top_num)

    if top_num <=0:
        print('⚠️ Please enter a number larger than 0 next time.')
        quit()
else:
    print('⚠️ Please type a valid number next time!')
    quit()

random_num=random.randint(0,top_num)
guess=0

while True:
    guess+=1
    user_guess=input("🔢 Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('⚠️ Please enter a number next time!')
        continue
    
    if user_guess==random_num:
        print('🎉 You got it!')
        break
    elif user_guess>random_num:
        print('⬇️ Too high! Try a smaller number.')
    else:
        print('⬆️ Too low! Try a bigger number.')
print(f'🏅 You got it in {guess} guesses.')
print('='*10,'🙏 THANK YOU, COME AGAIN!','='*10)