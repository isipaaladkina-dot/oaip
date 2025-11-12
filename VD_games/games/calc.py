import random
import operator


def get_question_and_answer():

    a = random.randint(1, 50)
    b = random.randint(1, 50)

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    operation = random.choice(list(operations.keys()))
    question = f"{a} {operation} {b}"
    correct_answer = str(operations[operation](a, b))

    return question, correct_answer


DESCRIPTION = 'Вычислите результат выражения.'
