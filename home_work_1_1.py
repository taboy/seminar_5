import random as r
print("press any button")
input()
n = r.randint(0, 1)
if n == 0:
    print(" first play 1 player")
else:
    print(" first play 2 player")
sweets = 2021
i = 28

print(f'we have  {sweets} sweets')


def give_number():
    while True:
        try:
            m = int(input(" player 1write how much sweets your want"))
            if m > i:
                print("YOU CAN GIVE MAX 28")
                return give_number()
            elif m <= 0:
                print("you can bring from 1 to 28")
            else:
                return m
        except ValueError:
            print('Invalid input')


def give_number2():
    while True:
        try:
            m = int(input(" player 2write how much sweets your want:"))

            if m > i:
                print("YOU CAN GIVE MAX 28")
                return give_number()
            elif m <= 0:
                print("you can bring from 1 to 28")
            else:
                return m
        except ValueError:
            print('Invalid input')


while (sweets >= 0):
    sweets = sweets - give_number()
    if sweets <= 0:
        print("player 1 win")
        break
    else:
        print(f'left {sweets}')

    sweets = sweets - give_number2()
    if sweets <= 0:
        print("player 2 win")
        break
    else:
        print(f'left {sweets}')
