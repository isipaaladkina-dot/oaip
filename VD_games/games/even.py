import random


def is_even(number):

    return number % 2 == 0


def get_question_and_answer():

    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'да' if is_even(number) else 'нет'
    return question, correct_answer


DESCRIPTION = 'Ответьте "да", если число чётное, и "нет", если нечётное.'
