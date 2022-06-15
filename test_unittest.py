import unittest
from loto import generate_random_nums, Card, Game


class TestRandom(unittest.TestCase):

    def test_random_numbers(self):
        count = 15
        self.assertEqual(len(generate_random_nums(count, 1, 90)), count)
        self.assertTrue(generate_random_nums(count, 1, 90), list)

    def test_exception(self):
        with self.assertRaises(ValueError):
            generate_random_nums(8, 1, 90)


class TestCard(unittest.TestCase):

    # def SetUp(self):
    #     self.card = Card()
    #     print('Выполняюсь перед каждым тестом')
    #
    # def tearDown(self):
    #     del self.card

    def test__init__(self):
        card = Card()
        number_of_zeros_in_lst = 0
        self.assertEqual(len(card.OUR_RAW_LST), len(card.tmp_lst) * 3)
        self.assertEqual(card.COLUMNS - card.NUMS_IN_LINE, 4)
        self.assertEqual(card.OUR_RAW_LST.count(number_of_zeros_in_lst), 12)

    def test_when_num_hits(self):
        card = Card()
        num = 90
        a = [90, -1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, 0, -1, 0, 0, -1, 0, 0, -1, -1, 0, -1, 0, -1, -1, 0]
        b = [-1, -1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, 0, -1, 0, 0, -1, 0, 0, -1, -1, 0, -1, 0, -1, -1, 0]
        self.WHEN_HIT_NUM = -1
        self.assertTrue([item == card.WHEN_HIT_NUM for item in a if num == item])
        self.assertTrue([a == b for num in a if card.when_num_hit(num)])

    def test_closed(self):
        card = Card()
        a = [0, 0, 0, -1, -1, 0, -1]
        self.assertEqual(set(a), {card.BLIND_NUM, card.WHEN_HIT_NUM})


class TestGame(unittest.TestCase):

    def test__init__(self):
        game = Game()
        self.assertEqual(len(game.KEGS), 90)

    def test_play_game(self):
        self.USER_CARD = [0, -1, 0, -1, 65, -1]
        game_closed = [0, -1, 0, -1, -1, -1]
        self.assertTrue([self == 1 if self.USER_CARD == set(game_closed) else self == 2])