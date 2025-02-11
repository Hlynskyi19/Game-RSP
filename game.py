import random


def get_computer_choice():
    return random.choice(["камінь", "ножиці", "папір"])


def get_winner(player, computer):
    if player == computer:
        return "Нічия!"
    elif (
        (player == "камінь" and computer == "ножиці")
        or (player == "ножиці" and computer == "папір")
        or (player == "папір" and computer == "камінь")
    ):
        return "Ви перемогли!"
    else:
        return "Комп'ютер переміг!"


def main():
    while True:
        player_choice = input(
            "Введіть 'камінь', 'ножиці' або 'папір' (або 'вийти' для завершення): "
        ).lower()
        if player_choice == "вийти":
            print("Гра завершена. Дякую за гру!")
            break
        if player_choice not in ["камінь", "ножиці", "папір"]:
            print("Неправильний вибір, спробуйте ще раз.")
            continue

        computer_choice = get_computer_choice()
        print(f"Комп'ютер обрав: {computer_choice}")
        print(get_winner(player_choice, computer_choice))
        print("-" * 30)


if __name__ == "__main__":
    main()
