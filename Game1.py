import random

print("🎮 Welcome to the Snake, Water and Gun Game!")

game = [1, 2, 3]
computer = random.choice(game)

print("\nChoose your option:")
print("1. Snake 🐍")
print("2. Water 💧")
print("3. Gun 🔫")

user = int(input("Enter your choice (1/2/3): "))

# Display computer's choice
if computer == 1:
    print("\nComputer chose: Snake 🐍")
elif computer == 2:
    print("\nComputer chose: Water 💧")
else:
    print("\nComputer chose: Gun 🔫")

# Decide winner
if user == computer:
    print("🤝 Match Draw!")

elif user == 1 and computer == 2:
    print("🐍 Snake drinks the Water.")
    print("🎉 You Won!")

elif user == 1 and computer == 3:
    print("🔫 Gun shot the Snake.")
    print("❌ You Lose!")

elif user == 2 and computer == 1:
    print("🐍 Snake drinks the Water.")
    print("❌ You Lose!")

elif user == 2 and computer == 3:
    print("💧 Water damaged the Gun.")
    print("🎉 You Won!")

elif user == 3 and computer == 1:
    print("🔫 Gun shot the Snake.")
    print("🎉 You Won!")

elif user == 3 and computer == 2:
    print("💧 Water damaged your Gun.")
    print("❌ You Lose!")

else:
    print("⚠️ Invalid Choice! Please enter only 1, 2, or 3.")