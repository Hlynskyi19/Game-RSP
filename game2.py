import random
from typing import Dict

"""
Гра 'Камінь, ножиці, папір'.
Гравець обирає один із варіантів, після чого вибір робить комп'ютер.
Переможець визначається за класичними правилами гри.
"""

# Словник, що зберігає можливі дії
ACTIONS: Dict[int, str] = {0: "Камінь", 1: "Папір", 2: "Ножиці"}

# Словник перемог: який вибір перемагає який
VICTORIES: Dict[str, str] = {
    "Камінь": "Ножиці",  # Камінь перемагає ножиці
    "Папір": "Камінь",  # Папір перемагає камінь
    "Ножиці": "Папір",  # Ножиці перемагають папір
}


def get_user_selection(actions: Dict[int, str]) -> str:
    """
    Отримує вибір користувача.

    Параметри:
    actions (Dict[int, str]): Можливі дії гри.

    Повертає:
    str: Вибір користувача у вигляді рядка.
    """
    choices = [f"{actions[action]}[{action}]" for action in actions]
    choices_str = ", ".join(choices)
    selection = int(input(f"Оберіть варіант ({choices_str}): "))
    action = actions[selection]
    return action


def get_computer_selection(actions: Dict[int, str]) -> str:
    """
    Генерує випадковий вибір комп'ютера.

    Параметри:
    actions (Dict[int, str]): Можливі дії гри.

    Повертає:
    str: Випадковий вибір комп'ютера у вигляді рядка.
    """
    selection = random.randint(0, len(actions) - 1)
    action = actions[selection]
    return action


def determine_winner(
    victories: Dict[str, str], user_action: str, computer_action: str
) -> str:
    """
    Визначає переможця гри.

    Параметри:
    victories (Dict[str, str]): Правила перемог у грі.
    user_action (str): Вибір користувача.
    computer_action (str): Вибір комп'ютера.

    Повертає:
    str: Результат гри у вигляді рядка.
    """
    defeats = victories[user_action]
    if user_action == computer_action:
        result = f"Обидва вибрали {user_action}. Нічия!"
    elif computer_action in defeats:
        result = f"{user_action} перемагає {computer_action}! Ви виграли!"
    else:
        result = f"{computer_action} перемагає {user_action}! Ви програли."
    return result


if __name__ == "__main__":
    while True:
        try:
            user_selection = get_user_selection(ACTIONS)  # Отримуємо вибір користувача
            print(f"Ваш вибір: {user_selection}")

            computer_selection = get_computer_selection(
                ACTIONS
            )  # Отримуємо вибір комп'ютера
            print(f"Вибір комп'ютера: {computer_selection}")

            result = determine_winner(VICTORIES, user_selection, computer_selection)
            print(result)

        except (ValueError, KeyError):  # Обробка неправильного вводу
            range_str = f"[0, {len(ACTIONS) - 1}]"
            print(f"Некоректний вибір. Введіть число в межах {range_str}.")
            continue

        play_again = input("Хочете зіграти ще раз? (y/n): ")
        if play_again.lower() != "y":
            break
