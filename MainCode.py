import random
import time

A = 0
B = 0
C = 0
D = 0
A_Check = 0
B_Check = 0
C_Check = 0
D_Check = 0
Player_One = input('What is your name?')
Car_choice_One = input('''What car would you like to choose?
>Car (A)
>Car (B)
>Car (C)
>Car (D)
> ''')
if Car_choice_One.upper() == 'A':
    A_Check = A_Check + 1
elif Car_choice_One.upper() == 'B':
    B_Check = B_Check + 1
elif Car_choice_One.upper() == 'C':
    C_Check = C_Check + 1
elif Car_choice_One.upper() == 'D':
    D_Check = D_Check + 1
print(f'{Player_One} Has Chosen {Car_choice_One} Please Do not choose the same thing!!!!!!!!')
Player_Two = input('What is your name?')
Car_choice_Two = input('''What car would you like to choose?
>Car (A)
>Car (B)
>Car (C)
>Car (D)
> ''')
if Car_choice_Two.upper() == 'A':
    A_Check = A_Check + 1
elif Car_choice_Two.upper() == 'B':
    B_Check = B_Check + 1
elif Car_choice_Two.upper() == 'C':
    C_Check = C_Check + 1
elif Car_choice_Two.upper() == 'D':
    D_Check = D_Check + 1
while A_Check == 2 or B_Check == 2 or C_Check == 2 or D_Check == 2:
    if A_Check == 2:
        A_Check -= 1
    elif B_Check == 2:
        B_Check -= 1
    elif C_Check == 2:
        C_Check -= 1
    elif D_Check == 2:
        D_Check -= 1
    print(Car_choice_Two + ' Has Already Been Chosen. Please Choose A Different One!')
    Car_choice_Two = input('''What car would you like to choose?
    >Car (A)
    >Car (B)
    >Car (C)
    >Car (D)
    > ''')
    if Car_choice_Two.upper() == 'A':
        A_Check = A_Check + 1
    elif Car_choice_Two.upper() == 'B':
        B_Check = B_Check + 1
    elif Car_choice_Two.upper() == 'C':
        C_Check = C_Check + 1
    elif Car_choice_Two.upper() == 'D':
        D_Check = D_Check + 1
print(f'{Player_Two} Has Chosen {Car_choice_Two} Please Do not choose the same thing!!!!!!!!')
Player_Three = input('What is your name?')
Car_choice_Three = input('''What car would you like to choose?
>Car (A)
>Car (B)
>Car (C)
>Car (D)
> ''')
if Car_choice_Three.upper() == 'A':
    A_Check = A_Check + 1
elif Car_choice_Three.upper() == 'B':
    B_Check = B_Check + 1
elif Car_choice_Three.upper() == 'C':
    C_Check = C_Check + 1
elif Car_choice_Three.upper() == 'D':
    D_Check = D_Check + 1
while A_Check == 2 or B_Check == 2 or C_Check == 2 or D_Check == 2:
    if A_Check == 2:
        A_Check -= 1
    elif B_Check == 2:
        B_Check -= 1
    elif C_Check == 2:
        C_Check -= 1
    elif D_Check == 2:
        D_Check -= 1
    print(Car_choice_Three + ' Has Already Been Chosen. Please Choose A Different One!')
    Car_choice_Three = input('''What car would you like to choose?
    >Car (A)
    >Car (B)
    >Car (C)
    >Car (D)
    > ''')
    if Car_choice_Three.upper() == 'A':
        A_Check = A_Check + 1
    elif Car_choice_Three.upper() == 'B':
        B_Check = B_Check + 1
    elif Car_choice_Three.upper() == 'C':
        C_Check = C_Check + 1
    elif Car_choice_Three.upper() == 'D':
        D_Check = D_Check + 1
print(f'{Player_Three} Has Chosen {Car_choice_Three} Please Do not choose the same thing!!!!!!!!')
Player_Four = input('What is your name?')
Car_choice_Four = input('''What car would you like to choose?
>Car (A)
>Car (B)
>Car (C)
>Car (D)
> ''')
if Car_choice_Four.upper() == 'A':
    A_Check = A_Check + 1
elif Car_choice_Four.upper() == 'B':
    B_Check = B_Check + 1
elif Car_choice_Four.upper() == 'C':
    C_Check = C_Check + 1
elif Car_choice_Four.upper() == 'D':
    D_Check = D_Check + 1
while A_Check == 2 or B_Check == 2 or C_Check == 2 or D_Check == 2:
    if A_Check == 2:
        A_Check -= 1
    elif B_Check == 2:
        B_Check -= 1
    elif C_Check == 2:
        C_Check -= 1
    elif D_Check == 2:
        D_Check -= 1
    print(Car_choice_Four + ' Has Already Been Chosen. Please Choose A Different One!')
    Car_choice_Four = input('''What car would you like to choose?
    >Car (A)
    >Car (B)
    >Car (C)
    >Car (D)
    > ''')
    if Car_choice_Four.upper() == 'A':
        A_Check = A_Check + 1
    elif Car_choice_Four.upper() == 'B':
        B_Check = B_Check + 1
    elif Car_choice_Four.upper() == 'C':
        C_Check = C_Check + 1
    elif Car_choice_Four.upper() == 'D':
        D_Check = D_Check + 1

Unlucky = random.randint(1, 4)
Lukcy = random.randint(1, 4)

if Lukcy == 1:
    More = 'A'
    A = A + 2
elif Lukcy == 2:
    More = 'B'
    B = B + 2
elif Lukcy == 3:
    More = 'C'
    C = C + 2
elif Lukcy == 4:
    More = 'D'
    D = D + 2

if Unlucky == 1:
    Less = "A"
    A = A - 2
elif Unlucky == 2:
    Less = 'B'
    B = B - 2
elif Unlucky == 3:
    Less = 'C'
    C = C - 2
elif Unlucky == 4:
    Less = 'D'
    D = D - 2

Ready = input('Users Ready? (Y)es: ')
if Ready.upper() == 'Y':
    print(f'''              {Player_One} your turtle is  {Car_choice_One}
              {Player_Two} your turtle is  {Car_choice_Two}
              {Player_Three} your turtle is  {Car_choice_Three}
              {Player_Four} your turtle is  {Car_choice_Four}''')
    print('3')
    print('2')
    print('1')
    print('Go')

Round = 0
Round_Max = 10

while Round <= Round_Max:
    print('This is Round #' + str(Round))
    print('Round #' + str(Round) + ' will start in 5 seconds!')
    print("5!")
    time.sleep(1)
    print("4!")
    time.sleep(1)
    print("3!")
    time.sleep(1)
    print("2!")
    time.sleep(1)
    print("1!")
    time.sleep(1)
    print("GO!!!!!!")
    if Round == Round_Max:
        print(f'Car A ={A}, Car B = {B}, Car C = {C}, Car D = {D}')
        print(f'Lucky Was (+2)  {More} | Unlukcy was (-2) {Less}|')
        print(f'{Winner} Was The Winner!')
        break
    if A > B and A > C and A > D:
        Winner = 'A'
    elif B > A and B > C and B > D:
        Winner = 'B'
    elif C > B and C > A and C > D:
        Winner = 'C'
    elif D > B and D > C and D > A:
        Winner = 'D'

    Car_A = random.randint(1, 5)
    A = A + Car_A
    Car_B = random.randint(1, 5)
    B = B + Car_B
    Car_C = random.randint(1, 5)
    C = C + Car_C
    Car_D = random.randint(1, 5)
    D = D + Car_D
    print(f'Car A Has Moved, A Now = {A}')
    print(f'Car B Has Moved, B Now = {B}')
    print(f'Car C Has Moved, C Now = {C}')
    print(f'Car D Has Moved, D Now = {D}')
    Round = Round + 1
    # Make round roads so it constantly goes and make milestones
