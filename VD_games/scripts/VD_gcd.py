from VD_games.engine.game_engine import run_game
from VD_games.games.gcd import get_question_and_answer, DESCRIPTION


def main():

    run_game("VD-gcd", get_question_and_answer, DESCRIPTION)


if __name__ == "__main__":
    main()
