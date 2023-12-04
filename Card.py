import Global

class Card:

    specific_bhevaior_predicate = None

    def __init__(self, kolor, figura):
        self.kolor = kolor
        self.figura = figura
        self.wartość = Global.wartość[figura]

    def __str__(self):
        return f"{self.figura} {self.kolor}"


    def ace(self, card):
        # TODO, ta logika powinna byc w serwisie do zarządzania kartami, encje slużą do określania kontraktów
        if card.figura == "As":
            if card.wartość == 0:
                while card.wartość not in ["1", "11"]:
                    card.wartość = input(f"\nWybierz wartość dla swojego {card.__str__()} (1 lub 11)\n")
                    if card.wartość in ["1", "11"]:
                        value = int(card.wartość)
                        return value
            if card.wartość == 1:
                print(f"\nTeraz Twój {card.__str__()} jest równy 11")
                card.wartość = "11"
                value = int(card.wartość)
                return value
            elif card.wartość == 11:
                print(f"\nTeraz Twój {card.__str__()} jest równy 1")
                card.wartość = "1"
                value = int(card.wartość)
                return value