print("""welcome to very basic game, guess the number!""")

answer = 9
guesses = 0

while guesses < 3:
    guess = int(input("guess: "))
    guesses += 1
    if guess == answer:
        print("you win!")
        break
else:
    print("u lost ur chance")