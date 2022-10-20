import random
user_wins = 0
pc_wins = 0
options = ['paper','rock','scissors']
while True :
    user = input('type paper/rock/scissors or Q to quit : ').lower()
    if user == 'q' :
        break

    if user not in options :
        continue

    random_num=random.randint(0,2)
    #0=paper ,1=rock ,2=scissors
    pc_pick = options[random_num]
    print('the computer picked : ',pc_pick)

    if user == 'rock' and pc_pick == 'scissors' :
        print('you won')
        user_wins += 1

    elif user == 'paper' and pc_pick == 'rock' :
        print('you won')
        user_wins += 1

    elif user == 'scissors' and pc_pick == 'paper' :
        print('you won')
        user_wins += 1

    else :
        print('you lost ')
        pc_wins+=1
print('you won :',user_wins,'times')
print('the computer win :',pc_wins,'times')
print('gg')


