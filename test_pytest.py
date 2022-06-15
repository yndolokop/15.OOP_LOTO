import pytest

from loto import *


def test_generate_random_nums():
    count = 15
    assert len(generate_random_nums(count, 1, 90)) == count
    assert type(generate_random_nums(count, 1, 90)) == list


def test_generate_random_nums_exception():
    with pytest.raises(ValueError):
        generate_random_nums(8, 1, 90)


class TestCard:

    def test__init__(self):
        card = Card()
        number_of_zeros_in_lst = 0
        assert len(card.OUR_RAW_LST) == len(card.tmp_lst) * 3        # длинна RAW списка равна сумме длин 3-х tmp_lst.
        assert card.COLUMNS - card.NUMS_IN_LINE == 4                 # количество нулей в линии равно 4ём.
        assert card.OUR_RAW_LST.count(number_of_zeros_in_lst) == 12  # количество нулей в RAW списке равно 12.

    def test_when_num_hit(self):
        num = 90
        a = [0, -1, 0, -1, 90, -1]
        assert [item for item in a if num == item]

    def test_closed(self):
        card = Card()
        a = [0, 0, 0, -1, -1, 0, -1]
        assert set(a) == {card.BLIND_NUM, card.WHEN_HIT_NUM}


class TestGame:

    def test__init__(self):
        game = Game()
        assert len(game.KEGS) == 90

    def test_play_game(self):
        self.USER_CARD = [0, -1, 0, -1, 65, -1]
        game_closed = [0, -1, 0, -1, -1, -1]
        assert [self == 1 if self.USER_CARD == set(game_closed) else self == 2]


'''
Предварительно устанавливаем pip install pytest-cov
Покрытие тестами осуществляется pytest --cov=src'''