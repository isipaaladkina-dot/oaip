import random

DESCRIPTION = "Ответьте \"да\", если число простое. Иначе ответьте \"нет\"."

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_question_and_answer():
    number = random.randint(2, 100)
    question = str(number)
    answer = "да" if is_prime(number) else "нет"
    return question, answer

