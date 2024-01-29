from Card import Card
import Global
import random


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls].cards = []
            cls._instances[cls].populate_deck()
        return cls._instances[cls]


class Deck(metaclass=SingletonMeta):

    def populate_deck(self):
        # TODO, lecimy po angielsku - DONE
        # TODO, zaimplementuj singleton , for fun. https://refactoring.guru/design-patterns/singleton/python/example - KIND OF
        for r in Global.rank:
            for c in Global.suit:
                card = Card(c, r)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def take_one(self):
        return self.cards.pop(0)
