import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ace = 11


def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    score = 0
    for card in card_list:
        score += card
    return score


user_cards = []
user_first_card = deal_card()
user_second_card = deal_card()
user_cards.append(user_first_card)
user_cards.append(user_second_card)

print(user_cards)
print(f"Your score is: {calculate_score(user_cards)}")

computer_cards = []
computer_first_card = deal_card()
computer_second_card = deal_card()
computer_cards.append(computer_first_card)
computer_cards.append(computer_second_card)

print(f"Computer first card: {computer_first_card}")
# print(calculate_score(computer_cards))

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

# Detect when computer has blackjack
if computer_score == 21:
    print("Computer has blackjack. You LOSE.")
elif user_score == 21:
    print("You have a blackjack. You WIN.")
else:
    result = input("Do you want to get another card?\n")
    while result == "yes" and user_score < 21:
        user_cards.append(random.choice(cards))
        user_score = calculate_score(user_cards)
        print(f"Your cards are {user_cards}.")
        print(f"Your score is {calculate_score(user_cards)}.")
        if user_score > 21:
            if ace in user_cards:
                # user_score -= 10 # ace counts as 1 not 11
                i = user_cards.index(ace)
                user_cards[i] = 1
                user_score = calculate_score(user_cards)
                print(f"Your cards are {user_cards}.")
                print(f"Your score is {calculate_score(user_cards)}.")
            else:
                print("BUST. You LOSE")
                break
            if user_score > 21:
                print("BUST. You LOSE")
                break
        result = input("Do you want to get another card\n")
    else:  # if result == "no":
        # Computer has to play until its score is over 16
        while computer_score < 17:
            computer_cards.append(random.choice(cards))
            computer_score = calculate_score(computer_cards)
        if computer_score > 21:
            print(f"Computer score is {computer_score}, you WIN.")
        elif computer_score > user_score:
            print(f"Computer score: {computer_score}.\nYour score: {user_score}.\n You LOSE.")
        elif computer_score < user_score:
            print(f"Computer score: {computer_score}.\nYour score: {user_score}.\n You WIN.")
        else:
            print(f"Computer score: {computer_score}.\nYour score: {user_score}.\n DRAW.")
print(f"Computer cards are {computer_cards}.")
