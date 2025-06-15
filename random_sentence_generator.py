import random

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

def get_random_word(word_list):
    return random.choice(word_list)

print("This is your random sentence generator. Press [Enter] to get a new one or type 'end' to exit.")
while True:
    command = input()
    if command == "end":
        break

    who = f"{get_random_word(names)} from {get_random_word(places)}"
    action = f"{get_random_word(adverbs)} {get_random_word(verbs)} {get_random_word(nouns)}"
    sentence = f"{who} {action} {get_random_word(details)}"
    print(sentence)
