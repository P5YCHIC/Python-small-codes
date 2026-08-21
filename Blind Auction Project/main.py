from art import logo
print(logo)
dictionary = {}
# TODO-1: Ask the user for input
nick = True
while nick:
    name_key = input("What is your name?:")
    bid_value = int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    dictionary[name_key] = bid_value
    ask_for_other_bidders = input("Is there any other bidders? Type 'yes or 'no'.").lower()

    if ask_for_other_bidders == "yes":
        print("\n" * 20)
    else:
        print("\n" * 20)
        print(f"The winner is {max(dictionary ,key=dictionary.get)} with a bid of {max(dictionary.values())}")
        nick = False

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


