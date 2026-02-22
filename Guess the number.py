# Number Guessing Game

import random

best_score = None

while True:
    number = random.randint(1, 100)
    attempts = 7
    used_attempts = 0

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it!")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        used_attempts += 1
        attempts -= 1

        if guess == number:
            print("🎉 Congratulations! You guessed correctly.")
            print("Attempts used:", used_attempts)

            if best_score is None or used_attempts < best_score:
                best_score = used_attempts
                print("🏆 New Best Score:", best_score)

            break

        elif guess > number:
            print("Too high!")

        else:
            print("Too low!")

        # Bonus Hint (within 5)
        if abs(guess - number) <= 5 and guess != number:
            print("🔥 Very close!")

        if attempts > 0:
            print("Attempts remaining:", attempts)

    else:
        print("\n❌ You failed to guess the number.")
        print("The correct number was:", number)

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        if best_score is not None:
            print("Your Best Score:", best_score)
        break

  
      output:

===== NUMBER GUESSING GAME =====
I have selected a number between 1 and 100.
You have 7 attempts to guess it!
Enter your guess: 50
Too low!
Attempts remaining: 6
Enter your guess: 75
Too high!
Attempts remaining: 5
Enter your guess: 70
🔥 Very close!
Too high!
Attempts remaining: 4
Enter your guess: 68
🎉 Congratulations! You guessed correctly.
Attempts used: 4
🏆 New Best Score: 4

Play Again

Do you want to play again? (yes/no): yes

===== NUMBER GUESSING GAME =====
I have selected a number between 1 and 100.
You have 7 attempts to guess it!
Enter your guess: 30
Too high!
Attempts remaining: 6
Enter your guess: 15
Too low!
Attempts remaining: 5
Enter your guess: 20
Too high!
Attempts remaining: 4
Enter your guess: 18
🎉 Congratulations! You guessed correctly.
Attempts used: 4
Your Best Score: 4

Fail Scenario
Do you want to play again? (yes/no): yes

===== NUMBER GUESSING GAME =====
I have selected a number between 1 and 100.
You have 7 attempts to guess it!
Enter your guess: 10
Too low!
Attempts remaining: 6
Enter your guess: 20
Too low!
Attempts remaining: 5
Enter your guess: 30
Too high!
Attempts remaining: 4
Enter your guess: 25
Too low!
Attempts remaining: 3
Enter your guess: 27
Too high!
Attempts remaining: 2
Enter your guess: 26
Too high!
Attempts remaining: 1
Enter your guess: 24
Too low!
❌ You failed to guess the number.
The correct number was: 26
