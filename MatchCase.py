value=7
while True:
    guess=int(input("Guess a number between 1-10:"))
    if guess==value:
        print('Correct')
        break
    else:
        print("Take another guess")

print()
user_input=int(input("Enter a number between 1-4:"))
match user_input:
    case 2:
        print("You entered",user_input)
    case 3:
        print("You entered",user_input)
    case _:
        print("Are you dumb?")