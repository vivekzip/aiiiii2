Suits = ["\u2663", "\u2665", "\u2666", "\u2660"]  # Clubs, Hearts, Diamonds, Spades
Ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for rank in Ranks:
    for suit in Suits:
        print(f'{rank} of {suit}'.ljust(10), end='')
    print()
