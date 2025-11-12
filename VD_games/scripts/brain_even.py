from VD_games.engine.game_engine import run_game
from VD_games.games.even import get_question_and_answer, DESCRIPTION


def main():

    run_game("VD-even", get_question_and_answer, DESCRIPTION)


if __name__ == "__main__":
    main()
