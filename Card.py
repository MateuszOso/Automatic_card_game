import Global

class Card:

    specific_bhevaior_predicate = None

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Global.value[rank]

    def __str__(self):
        return f"{self.rank} {self.suit}"


