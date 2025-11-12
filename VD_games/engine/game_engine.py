import prompt

def run_game(game_name, get_question_and_answer, description):
    print(f"Добро пожаловать в {game_name}!")
    name = prompt.string('Как тебя зовут? ')
    print(f"Привет, {name}!")
    print(description)

    rounds_count = 3

    for _ in range(rounds_count):
        question, correct_answer = get_question_and_answer()
        print(f"Вопрос: {question}")
        user_answer = prompt.string('Твой ответ: ')

        if user_answer == correct_answer:
            print("Правильно!")
        else:
            print(f"'{user_answer}' это неправильный ответ ;(. Правильный ответ был '{correct_answer}'.")
            print(f"Давайте попробуем снова, {name}!")
            return

    print(f"Поздравляем, {name}!")

