import random


def get_guess(low, high):
    while True:
        try:
            guess = int(input(f"Your guess ({low}-{high}): "))
        except ValueError:
            print("That's not a whole number. Try again.")
            continue

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        return guess


def play_round(low=1, high=100):
    secret = random.randint(low, high)
    attempts = 0

    print(f"\nI've picked a number between {low} and {high}.")
    print("Try to guess it!")

    while True:
        guess = get_guess(low, high)
        attempts += 1

        if guess == secret:
            print(f"\n✅ Correct! The number was {secret}.")
            print(f"You got it in {attempts} attempt(s).")
            return attempts
        elif guess > secret:
            print("📉 Too high. Try again.")
        else:
            print("📈 Too low. Try again.")


def main():
    print("=== Number Guessing Game ===")

    while True:
        play_round(1, 100)

        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            break

    print("\nThanks for playing. Bye!")


if __name__ == "__main__":
    main()
