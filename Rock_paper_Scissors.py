import random
print('🪨📄✂️' + '='*15 + ' WELCOME TO ROCK PAPER SCISSORS ' + '='*15 + '🪨📄✂️\n')
user_wins=0
computer_wins=0
options=['rock','paper','scissors']
emoji_map = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
while True:
    user_input=input('Type Rock/Paper/Scissors or Q to quit: ').lower().strip()
    if user_input=='q':
        print('👋 Quitting the game. See your results below!')
        break
    if user_input not in options:
        print("❌ Invalid input. Please type Rock, Paper, or Scissors.\n")
        continue
    random_num=random.randint(0,2)

    computer_pic=options[random_num]

    print(f'🤖 Computer Pick: {computer_pic.capitalize()} {emoji_map[computer_pic]}')

    if user_input==computer_pic:
        print("😐 It's a tie!")
    elif user_input=='rock' and computer_pic=='scissors':
        print('🎉 You Won!')
        user_wins+=1
    elif user_input=='paper' and computer_pic=='rock':
        print('🎉 You Won!')
        user_wins+=1
    elif user_input=='scissors' and computer_pic=='paper':
        print('🎉 You Won!')
        user_wins+=1
    else:
        print('💔 You Lost!')
        computer_wins+=1
print('\n','🏆'*2,'YOU WON:',user_wins,'TIMES','🏆'*2)
print('\n','🤖'*2,'COMPUTER WON:',computer_wins,'TIMES','🤖'*2)
print('\n','='*15,'🙏 THANK YOU FOR PLAYING!','='*15)