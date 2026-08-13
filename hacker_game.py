import random
import string
import os
from datetime import datetime

# ---------------- LOGGING ----------------

LOG_FILE = "game.log"

def log(message):
    print(message)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {message}\n")


def logged_input(prompt):
    value = input(prompt)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"[{datetime.now().strftime('%H:%M:%S')}] "
            f"USER INPUT: {value}\n"
        )

    return value


# ---------------- GAME ----------------

log("=" * 50)
log("🕵️ CYBER BREAK-IN SIMULATOR")
log("=" * 50)

CI_MODE = os.getenv("CI") == "true"

if CI_MODE:
    log("🤖 CI MODE: Automatic test running")
    length = 3
    password = "842"
    attempts = 3
else:
    log("🎮 LOCAL MODE: Player mode")

    log("Choose difficulty:")
    log("1. Easy")
    log("2. Medium")
    log("3. Hard")

    choice = logged_input("Enter choice: ")

    if choice == "1":
        length = 3
        attempts = 8
    elif choice == "2":
        length = 4
        attempts = 6
    else:
        length = 5
        attempts = 5

    password = ''.join(
        random.choice(string.digits)
        for _ in range(length)
    )

score = 100

# Automatic guesses for GitHub Actions
if CI_MODE:
    guesses = ["123", "731", "842"]

for attempt in range(1, attempts + 1):

    log("-" * 50)
    log(f"Attempt {attempt}/{attempts}")

    if CI_MODE:
        guess = guesses[attempt - 1]
        log(f"CI INPUT: {guess}")
    else:
        guess = logged_input("Enter password: ")

    if guess == password:
        log("🚨 SERVER HACKED SUCCESSFULLY!")
        log(f"🔑 Password cracked: {password}")
        log(f"🏆 Score: {score}")
        log("BUILD TEST: SUCCESS")
        break

    log("❌ ACCESS DENIED")

    if int(guess) < int(password):
        log("💡 Hint: Try a HIGHER number.")
    else:
        log("💡 Hint: Try a LOWER number.")

    score -= 15

else:
    log("💀 SYSTEM LOCKED")
    log(f"🔑 Password was: {password}")
    log("BUILD TEST: FAILED")