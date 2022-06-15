from random import randint


def generate_random_nums(count, start, end):  # count - общее кол-во чисел в карте.
    if not (count == 15 or count == 90):
        raise ValueError('Переменная count принимает только два значения: или 15, или 90')
    lst = []
    while len(lst) < count:
        new_number = randint(start, end)
        if new_number not in lst:
            lst.append(new_number)
    return lst


class Card:
    LINES = 3           # кол-во рядов в карте.
    COLUMNS = 9         # кол-во столбцов в карте.
    NUMS_IN_LINE = 5    # кол-во чисел в одном ряду.
    OUR_RAW_LST = None  # будет включать список из 27 рандомных чисел.
    BLIND_NUM = 0       # заглушка для пропущенных цифр в рядах.
    WHEN_HIT_NUM = -1   # заглушка для угаданных чисел.

    def __init__(self):
        nums_in_card = generate_random_nums((self.NUMS_IN_LINE * self.LINES), 1, 90)  # список из 15 случайных чисел.
        self.OUR_RAW_LST = []
        for i in range(0, self.LINES):
            # берем из списка nums_in_card по индексу числа от 0 до 5 затем от 5 до 10 и от 10 до 15.
            self.tmp_lst = sorted(nums_in_card[self.NUMS_IN_LINE * i: self.NUMS_IN_LINE * (i + 1)])  # временный список.
            empty_nums_in_line = self.COLUMNS - self.NUMS_IN_LINE  # кол-во пустых мест в ряду == 4
            for j in range(0, empty_nums_in_line):                 # добавим в цикле в рандомной позиции заглушки.
                index = randint(0, len(self.tmp_lst))              # рандомная позиция для добавляемого нуля.
                self.tmp_lst.insert(index, self.BLIND_NUM)         # вносим ноль в список согласно рандомному индексу.
            self.OUR_RAW_LST += self.tmp_lst                       # финальный список из 27 элем-ов.

    def __str__(self):
        """
        dunder __str__ визуализацию карты игрока.
        :return: ret - карта игрока.
        """
        separator = '--------------------------'         # разделитель.
        carta = separator + '\n'                         # переменная, в которой формируем карту лото.
        for index, num in enumerate(self.OUR_RAW_LST):   # пронумеруем список с помощью enumerate().
            if num == self.BLIND_NUM:                    # если число равно нулю, заменяем его на два пробела.
                carta += '  '
            elif num == self.WHEN_HIT_NUM:               # если, во время игры число совпадет с номером кегля, он
                carta += ' -'                            # заменяется в списке на -1, а в карте соответственно на дефис.
            elif num < 10:
                carta += f' {str(num)}'                  # выключка одно знаковых чисел по правому краю.
            else:
                carta += str(num)                        # добавляем очередное число в строку.
            if (index + 1) % self.COLUMNS == 0:          # перенос строки (index+1, т.к. отсчет в enumerate() c нуля).
                carta += '\n'
            else:
                carta += ' '                             # добавляем пробел между числами в ряду.
        return carta + separator                         # возвращаем сформированную строку + разделитель.

    def __contains__(self, item):                        # содержит ли строка элемент item(номер кегля).
        return item in self.OUR_RAW_LST

    def when_num_hit(self, num):
        for index, item in enumerate(self.OUR_RAW_LST):  # функция заменяет угаданный номер на -1
            if item == num:
                self.OUR_RAW_LST[index] = self.WHEN_HIT_NUM
        return num

    def closed(self) -> bool:                        # True - конец игры. В set(списке) остались лишь уникальные 0 и -1.
        return set(self.OUR_RAW_LST) == {self.BLIND_NUM, self.WHEN_HIT_NUM}


class Game:
    USER_CARD = None
    COMP_CARD = None
    NUM_KEGS = 90
    KEGS = []

    def __init__(self):
        self.USER_CARD = Card()
        self.COMP_CARD = Card()
        self.KEGS = generate_random_nums(self.NUM_KEGS, 1, 90)  # рандомный список из 90 бочонков.

    def play_game(self) -> int:
        """
        :return:
        0 - игра продолжается, если не соблюдено ни одно из условий
        1 - выиграл человек
        2 - выиграл компьютер
        """
        keg = self.KEGS.pop()                                        # берем последний бочонок применив функцию .pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.KEGS)})')   # печатаем номер кегля и карточки в консоль.
        print(f'----- Ваша карточка ------\n{self.USER_CARD}')       # карта игрока.
        print(f'-- Карточка компьютера ---\n{self.COMP_CARD}')       # карта компьютера.

        user_answer = input('Зачеркнуть цифру? (y/n)').lower().strip()  # предлагаем ответить.
        if user_answer == 'y' and keg not in self.USER_CARD or \
           user_answer != 'y' and keg in self.USER_CARD:  # проигрыш, если введен 'y' и номера нет в карте,
            return 2                                      # также проигрыш, если введен любой другой символ кроме 'y',
                                                          # но номер есть в карте.
        if keg in self.USER_CARD:               # если номер кегля есть в карте игрока.
            self.USER_CARD.when_num_hit(keg)    # заменяем его в списке на -1.
            if self.USER_CARD.closed():         # проверка списка на остаток номеров. Если True - конец игры.
                return 1
        if keg in self.COMP_CARD:               # если номер кегля есть в карте компьютера.
            self.COMP_CARD.when_num_hit(keg)    # заменяем на -1.
            if self.COMP_CARD.closed():         # проверяем, остались ли в списке еще номера. Если True - конец игры.
                return 2
