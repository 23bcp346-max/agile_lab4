import random
import string
import time

print("=" * 55)
print("        🕵️ CYBER BREAK-IN SIMULATOR 🕵️")
print("=" * 55)

print("\nYou have breached a secure server...")
print("Your mission: crack the password before the system locks you out!")
print()

# Difficulty
print("Choose difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("\nEnter choice: ")

if choice == "1":
    length = 3
    attempts = 8
elif choice == "2":
    length = 4
    attempts = 6
else:
    length = 5
    attempts = 5

# Generate secret password
characters = string.digits
password = ''.join(random.choice(characters) for _ in range(length))

# Give first clue
print("\n🔐 Password generated!")
print("Password contains", length, "digits.")

time.sleep(1)

score = 100

for attempt in range(1, attempts + 1):

    print("\n" + "-" * 55)
    print(f"Attempt {attempt}/{attempts}")
    
    guess = input("💻 Enter your password guess: ")

    # Validate
    if not guess.isdigit() or len(guess) != length:
        print(f"❌ Enter exactly {length} digits!")
        continue

    # Correct
    if guess == password:
        print("\n🚨 ACCESS GRANTED 🚨")
        print("You cracked the server!")
        print("🔑 Password:", password)
        print("🏆 Score:", score)
        break

    # Analyze guess
    correct_position = 0
    correct_digit = 0

    for i in range(length):
        if guess[i] == password[i]:
            correct_position += 1

    for digit in set(guess):
        if digit in password:
            correct_digit += 1

    print("❌ ACCESS DENIED")

    print(f"📍 Correct position: {correct_position}")
    print(f"🔎 Correct digit(s): {correct_digit}")

    # Extra clues
    if int(guess) < int(password):
        print("💡 Hint: Try a HIGHER number.")
    else:
        print("💡 Hint: Try a LOWER number.")

    score -= 15

else:
    print("\n💀 SYSTEM LOCKED 💀")
    print("You failed to crack the password.")
    print("🔑 The password was:", password)
    print("🏆 Final score:", max(score, 0))

print("\n" + "=" * 55)
print("             CONNECTION TERMINATED")
print("=" * 55)