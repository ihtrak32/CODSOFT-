def add():
    a=eval(input("Enter the Frist Number: "))
    b=eval(input("Ente the Second Number: "))
    print("\nThe Addtion of the numbers",a,"and",b,"is",a+b,'\n')

def sub():
    a=eval(input("Enter the Frist Number: "))
    b=eval(input("Ente the Second Number: "))
    print("\nThe Subtraction of the numbers",a,"and",b,"is",a-b,'\n')

def mult():
    a=eval(input("Enter the Frist Number: "))
    b=eval(input("Ente the Second Number: "))
    print("\nThe Multiplication of the numbers",a,"and",b,"is",a*b,'\n')

def div():
    a=eval(input("Enter the Frist Number: "))
    b=eval(input("Ente the Second Number: "))
    if b==0:
        print("\nNumber Cannot be divisible by 0 !!!!!!")
    else:
        print("\nThe Division of the numbers",a,"and",b,"is",a/b,'\n')

a=0
while a==0:
    print("                CALCULATOR\n1. ADD                            2. SUBTRACT\n3. MULTIPLY                       4. DIVISION\n5. EXIT")
    k=eval(input("Enter the number 1/2/3/4/5 to Continue your operation: "))
    if k==1:
        add()
    elif k==2:
        sub()
    elif k==3:
        mult()
    elif k==4:
        div()
    elif k==5:
        print("\nTHANK YOU for your response")
        a=1
    else:
        print("\nGiven option is not in the list !!!!!!\n")
        
        

