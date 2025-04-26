import random
a='y'
print("Rock !!! Paper !!!! Scissor !!!!")
while(a=='y'):
    h=int(input("\nHow many times wanted to play -"))
    U=0
    C=0
    for i in range(h):
        r=random.randint(1,3)
        u=int(input("1. Rock      2. Paper       3.Scissor\n\nChoose the number--> ")) 
        if (r==1 and u==1 or r==2 and u==2 or r==3 and u==3):
            print("\nYour Score -->",U," Computer Score -->",C,"\n")
            continue        
        elif(r==1 and u==3 or r==2 and u==1 or r==3 and u==2):
            C+=1
            print("\nYour Score -->",U," Computer Score -->",C,"\n")
        elif(u==1 and r==3 or u==2 and r==1 or u==3 and r==2):
            U+=1
            print("\nYour Score -->",U," Computer Score -->",C,"\n")
        else:
            printf("Sorry you entered wrong option so no points")
    if (U>C):
        print("!!!!! You won !!!!!\nYour Score -->",U," Computer Score -->",C,"\n")
    elif (C>U):
        print("Sorry You lose ! \nYour Score -->",U," Computer Score -->",C,"\n")
    else:
        print("The match is draw !! \nYour Score -->",U," Computer Score -->",C,"\n")
    a=input("Do you want to play again !!(y/n): ")
