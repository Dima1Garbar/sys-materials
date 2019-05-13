import math
from My_parser import main
class Room():

    def __init__(self, user_1, user_2, finance):
        self.user_1 = user_1
        self.user_2 = user_2
        self.dict_materials = None
        self.finance = finance

class Wall(Room):

    def __init__(self, user_1, user_2, height, wight, length, long, kind, finance):
        super().__init__(user_1, user_2, finance)
        self.height = height
        self.wight = wight
        self.length = length
        self.long = long
        self.kind = kind
        if self.kind == 1:
            self.kind = 0.53
        elif self.kind == 2:
            self.kind = 0.7
        else:
            self.kind = 1.06

    def calculation(self):
        if self.length == 0 or self.wight == 0 or self.height == 0:
            parser = 0
            g = 0
        else:
            g = 1
            parser = main(self.finance, self.user_2, self.user_1, None)
        if self.user_2 == 1:
            a = (((self.height * self.length) * 2 + (self.height * self.wight) * 2) - self.long) / self.kind
            self.dict_materials = {'Шпалери': {'Кількість': str(math.ceil(a + (a * 0.05)) * g) + ' рул.',
                                                  'Ціна': str('%.2f' % (math.ceil((a + (a * 0.05))) * parser)) + ' грн'}}
        elif self.user_2 == 2:
            a = ((self.height * self.length) * 2 + (self.height * self.wight) * 2) / self.long
            self.dict_materials = {'Дерево': {'Кількість': str(math.ceil(a + (a * 0.05)) * g) + ' м кв',
                                                  'Ціна': str('%.2f' % (math.ceil(a + (a * 0.05)) * parser)) + ' грн'}}
        else:
            a = math.ceil(((self.height * self.length) * 2 + (self.height * self.wight) * 2) - self.long)
            self.dict_materials = {'Плитка': {'Кількість': str(math.ceil((a + (a * 0.05))/0.36) * g) + ' шт',
                                            'Ціна': str(math.ceil((a + (a * 0.05))/0.36/10) * parser) + ' грн'},
                                   'Клей': {'Кількість': str(math.ceil(a * 5.2 + (a * 5.2 * 0.05)) * g) + ' кг',
                                            'Ціна': str('%.2f' % (math.ceil(((a * 5.2 + (a * 5.2 * 0.05)) / 25) * g * main(None, self.user_2, self.user_1, self.finance)))) + ' грн'}}

        return self.dict_materials



class Ceiling(Room):

    def __init__(self, user_1, user_2, area, finance):
        super().__init__(user_1, user_2, finance)
        self.area = area

    def calculation(self):

        parse = main(self.finance, self.user_2, self.user_1, None)
        a = math.ceil(self.area + (self.area * 0.05))
        if self.user_2 == 1:
            b = math.ceil(a / 0.36)
            self.dict_materials = {'Плитка': {'Кількість': str(b) + ' шт',
                                            'Ціна': str('%.2f' % (math.ceil(b / 10) * parse)) + ' грн'},
                                   'Клей': {'Кількість': str(math.ceil(self.area * 5.2 + (self.area * 5.2 * 0.05))) + ' кг',
                                            'Ціна': str('%.2f' % (math.ceil(((self.area * 5.2 + (self.area * 5.2 * 0.05)) / 25)) * main(None, self.user_2, self.user_1, self.finance))) + ' грн'}}


        else:
            self.dict_materials = {'Натяжна стеля': {'Кількість': str(a) + ' кв',
                                                        'Ціна': str('%.2f' % (a * parse)) + ' грн'}}


        return self.dict_materials

class Floor(Room):

    def __init__(self, user_1, user_2, area, finance):
        super().__init__(user_1, user_2, finance)
        self.area = area

    def calculation(self):

        a = math.ceil(self.area + (self.area * 0.05))
        parse = main(self.finance, self.user_2, self.user_1, None)

        if self.user_2 == 1:
            self.dict_materials = {'Лінолеум': {'Кількість': str(a) + ' кв',
                                                'Ціна': str('%.2f' % (a * parse)) + 'грн'}}
        elif self.user_2 == 2:
            self.dict_materials = {'Дерево': {'Кількість': str(a) + ' кв',
                                            'Ціна': str('%.2f' % (a * parse)) + 'грн'}}

        else:
            b = math.ceil((self.area / 0.36) + (self.area / 0.36) * 0.05)
            self.dict_materials = {'Плитка': {'Кількість': str(b) + ' шт',
                                            'Ціна': str('%.2f' % (a / 10 * parse)) + ' грн'},
                                   'Клей': {'Кількість': str(math.ceil(self.area * 5.2 + (self.area * 5.2 * 0.5))) + ' кг',
                                            'Ціна': str('%.2f' % (math.ceil(((self.area * 5.2 + (self.area * 5.2 * 0.5)) / 25) * main(None, self.user_2, self.user_1, self.finance)))) + ' грн'}}
        return self.dict_materials