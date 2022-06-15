from loto import *

if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_game()
        if score == 1:
            print('You win')
            break
        elif score == 2:
            print('You lose')
            break
