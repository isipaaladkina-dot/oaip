import random

DESCRIPTION = "Какое число пропущено в прогрессии?"

def get_question_and_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    progression = [start + i * step for i in range(length)]
    hidden_pos = random.randint(0, length - 1)
    answer = str(progression[hidden_pos])
    progression_display = [
        '..' if i == hidden_pos else str(x)
        for i, x in enumerate(progression)
    ]
    question = ' '.join(progression_display)
    return question, answer

