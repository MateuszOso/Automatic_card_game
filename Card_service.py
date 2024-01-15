def ace(card):
    # TODO, ta logika powinna byc w serwisie do zarządzania kartami, encje slużą do określania kontraktów - DONE
    if card.rank == "As":
        if card.value == 0:
            while card.value not in [1, 11]:
                try:
                    card.value = int(input(f"\nWybierz wartość dla swojego {card.__str__()} (1 lub 11)\n"))
                except:
                    print("Wpisz wartość cyfrą (1 lub 11)")
                if card.value in [1, 11]:
                    return card.value
        if card.value == 1:
            print(f"\nTeraz Twój {card.__str__()} jest równy 11")
            card.value = 11
            return card.value
        elif card.value == 11:
            print(f"\nTeraz Twój {card.__str__()} jest równy 1")
            card.value = 1
            return card.value
