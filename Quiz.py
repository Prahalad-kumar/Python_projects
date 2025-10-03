print('='*10 ,'Welcome to Computer Quiz','='*10)

play=input("Do you want to play? :")

if play.lower() != 'yes':
    quit()
print('Okay ! lets Play ::)')
score=0
ans=input("What does CPU stands for? : ")

if ans.lower()=='central processing unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

ans=input("What does GPU stands for? : ")

if ans.lower()=='graphics processing unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

ans=input("What does RAM stands for? : ")

if ans.lower()=='random access memory':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

ans=input("What does ROM stands for? : ")

if ans.lower()=='read only memory':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

ans=input("What does PSU stands for? : ")

if ans.lower()=='power supply unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

print(f'Your score is {score} /5.')
print('='*10,'Thank you','='*10)