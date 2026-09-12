from random import choice

choices = ["камінь", "ножиці", "папір"]

wins = 0
losses = 0
draws = 0

print("🎮 КАМІНЬ, НОЖИЦІ, ПАПІР")
print("Напиши 'вихід', щоб завершити гру.")

while True:
    player = input("\nТвій вибір (камінь, ножиці, папір): ").lower()

    if player == "вихід":
        break

    if player not in choices:
        print("❌ Такого варіанту немає!")
        continue

    computer = choice(choices)

    print("🤖 Комп'ютер обрав:", computer)

    if player == computer:
        print("🤝 Нічия!")
        draws += 1

    elif (
        (player == "камінь" and computer == "ножиці") or
        (player == "ножиці" and computer == "папір") or
        (player == "папір" and computer == "камінь")
    ):
        print("🏆 Ти переміг!")
        wins += 1

    else:
        print("🤖 Комп'ютер переміг!")
        losses += 1

    print(f"📊 Рахунок: перемоги — {wins} | поразки — {losses} | нічиї — {draws}")

print("\n👋 Дякую за гру!")
print(f"Фінальний рахунок: {wins} перемог, {losses} поразок, {draws} нічиїх.")
