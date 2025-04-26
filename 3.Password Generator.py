import random
print("\tPASSWORD GENERATOR\n")
l=int(input("Enter the length of password (max 15): "))
E="abc5def7g8hij3klm190"
M="ab5d@f54hi9L8b7&k54h321#"
H="a@b1&A$7K%s46c*hd!LO09fr3sb6"
p=''
if l<=15:
    print("1.Easy\t2.Moderate\t3.Hard\n")
    c=int(input("Enter the Complexity of password (1/2/3) :"))
    for i in range(l):
        if c==1:
            r=random.randrange(0,l)
            p+=E[r]
        elif c==2:
            r=random.randrange(0,l)
            p+=M[r]
        elif c==3:
            r=random.randrange(0,l)
            p+=H[r]
        else:
            print("Complexity is not there ! ! !")
            break
    print("Your Password is ",p)
else:
    print("Length too large ! ! !")
    
