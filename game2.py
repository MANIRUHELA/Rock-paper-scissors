
import random

def win(comp,you):

    if comp==you:
        return None

    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False

    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True

    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False

print("COMPUTER'S TURN:rock(r),paper(p) or scissor(s)? ")

rand_no=random.randint(1,3)

if rand_no==1:
    comp='r'

elif rand_no==2:
    comp='p'

elif rand_no==3:
    comp='s'

you=input("YOUR TURN:rock(r),paper(p) or scissor? ")

print(f"computer chose {comp}")
print(f"you chose {you}")

a=win(comp,you)

if a==None:
    print("IT'S A TIE")

elif a:
    print("HURRAY!YOU WON!!!!")
    
else:
    print("OOPSS!!YOU LOSE:(")