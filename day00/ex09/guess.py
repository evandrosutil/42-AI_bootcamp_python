import random

print('This is an iteractive guessing game')
print(
    'You have to enter a number  between 1 and 99 to'
    'find out the secret number')
print("Type 'exit' to end the game\nGood luck!")

count = 0
secret = random.randint(1, 99)
while True:
    user_input = input("What's your guess between 1 and 99?\n")
    if user_input == 'exit':
        print('Goodbye!')
        break
    count += 1
    try:
        user_input = int(user_input)
    except ValueError:
        print("That's not a number")
        continue
    if user_input not in range(1, 99):
        print("Not a valid guess. Trye again")
        continue
    elif user_input == secret and count == 1:
        message_42 = (
            "The answer to the ultimate question of life, the universe"
            "and everything is 42.")
        message = "Congratulations! You got it on your first try!"
        if secret == 42:
            print(message_42 + ' ' + message)
            break
        print(message)
        break
    elif user_input == secret:
        print("Congratulations! You've got it!")
        print(f"You won in {count} attempts!")
        break
    elif user_input > secret:
        print("Too high!")
        continue
    elif user_input < secret:
        print("Too low!")
        continue
