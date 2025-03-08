print('WELCOME TO TWO PLAYER TIC TAC TOE')
print()
print('''RULES FOR PLAYING THE GAME :\n--> EACH PLAYER HAS ONLY ONE CHANCE AT A TIME
--> IF THE PLAYER TYPES A WRONG MOVE THEN HIS / HER CHANCE WILL BE LOST
--> THERE IS NO TIME LIMIT IN THIS GAME\n\nALL THE BEST ''')
print()
cnt=0
def user():
    global cnt
    try:
        c=int(input('Enter a box player 1:'))
        if c in l:
            for i in range(len(l)):
                if c==l[i]:
                    l[i]=player1
                    cnt+=1
                    break
        else:
            print()
            print('CHANCE LOST')
    except:
        print()
        print('CHANCE LOST')
def user2():
    global cnt
    try:
        d=int(input('Enter a box player 2:'))
        if d in l:
            for a in range(len(l)):
                if d==l[a]:
                    l[a]=player2
                    cnt+=1
                    break
        else:
            print()
            print('CHANCE LOST')   
    except:
        print()
        print('CHANCE LOST')
def box():
    print('     |','  |',sep='   ',end='')
    print()
    print('  ',l[0],'  |','  ',l[1],'  |','  ',l[2],'  ',sep='',end='')
    print()
    print('_____',sep='',end='');print('|',sep='',end='');print('_____',sep='',end='')
    print('|',sep='',end='');print('_____',sep='',end='')
    print()
    print('     |','  |',sep='   ',end='')
    print()
    print('  ',l[3],'  |','  ',l[4],'  |','  ',l[5],'  ',sep='',end='')
    print()
    print('_____',sep='',end='');print('|',sep='',end='');print('_____',sep='',end='')
    print('|',sep='',end='');print('_____',sep='',end='')
    print()
    print('     |','  |',sep='   ',end='')
    print()
    print('  ',l[6],'  |','  ',l[7],'  |','  ',l[8],'  ',sep='',end='')
    print()
    print('     |','  |',sep='   ',end='')
    print()

def check():
    if l[0]==l[1]==l[2]==player1:
        return 1
    elif l[3]==l[4]==l[5]==player1:
        return 1
    elif l[6]==l[7]==l[8]==player1:
        return 1
    elif l[0]==l[3]==l[6]==player1:
        return 1
    elif l[1]==l[4]==l[7]==player1:
        return 1
    elif l[2]==l[5]==l[8]==player1:
        return 1
    elif l[0]==l[4]==l[8]==player1:
        return 1
    elif l[2]==l[4]==l[6]==player1:
        return 1
def check2():
    if l[0]==l[1]==l[2]==player2:
        return 1
    elif l[3]==l[4]==l[5]==player2:
        return 1
    elif l[6]==l[7]==l[8]==player2:
        return 1
    elif l[0]==l[3]==l[6]==player2:
        return 1
    elif l[1]==l[4]==l[7]==player2:
        return 1
    elif l[2]==l[5]==l[8]==player2:
        return 1
    elif l[0]==l[4]==l[8]==player2:
        return 1
    elif l[2]==l[4]==l[6]==player2:
        return 1
while True:
    l=[1,2,3,4,5,6,7,8,9]
    import random
    r=random.randint(0,1)
    if r==0:
        player1='X';player2='O'
    else:
        player1='O';player2='X'
    print('Player 1 is',player1);print('Player 2 is',player2)
    print()
    box()
    while cnt<10:
        print()
        user()
        print()
        box()
        a=check()
        if a==1:
            print()    
            print('Player 1 is the WINNER !!!')
            print()
            print('CONGRATULATIONS !!')
            break
        if cnt==9:
            break
        print()
        user2()
        print()
        b=check2()
        box()
        if b==1:
            print()
            print('Player 2 is the WINNER !!!')
            print()
            print('CONGRATULATIONS !!')
            break
        if cnt==9:
            break
    if a==b:
        print()
        print('It Is A Tie!!')
    print()
    ch=input('Do you wish to continue to a new game (yes/no):')
    print()
    cnt=0
    if ch[0]!='Y' and ch[0]!='y':
        print('EXITING THE PROGRAM')
        print()
        print('THANK YOU FOR PLAYING :)')
        break
