print('🧠' + '='*10 + ' Welcome to Computer Quiz ' + '='*10 + '🧠')

play=input("Do you want to play? (yes/no): ")

if play.lower() != 'yes':
    print('👋 Goodbye!')
    quit()
print('Okay! Let\'s Play! 😃')
score=0
ans=input("❓ What does CPU stand for? : ")

if ans.lower()=='central processing unit':
    print('✅ Correct!')
    score+=1
else:
    print('❌ Incorrect!')

ans=input("❓ What does GPU stand for? : ")

if ans.lower()=='graphics processing unit':
    print('✅ Correct!')
    score+=1
else:
    print('❌ Incorrect!')

ans=input("❓ What does RAM stand for? : ")

if ans.lower()=='random access memory':
    print('✅ Correct!')
    score+=1
else:
    print('❌ Incorrect!')

ans=input("❓ What does ROM stand for? : ")

if ans.lower()=='read only memory':
    print('✅ Correct!')
    score+=1
else:
    print('❌ Incorrect!')

ans=input("❓ What does PSU stand for? : ")

if ans.lower()=='power supply unit':
    print('✅ Correct!')
    score+=1
else:
    print('❌ Incorrect!')

print(f'🏅 Your score is {score} / 5.')
print('='*10,'🙏 Thank you for playing!','='*10)