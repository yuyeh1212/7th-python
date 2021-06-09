import random
number = random.randint(1, 10)

choose = int(input("1 for play,0 for end:"))
if choose == 0:
    print("Game over")
elif choose == 1:
    guess = int(input("please enter a number:"))
    if guess == number:
        print("Win the game")
    elif guess < number:
        print("你輸入的數字太小")
    else:
        print("你輸入的數字太大")
