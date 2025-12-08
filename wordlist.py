import random

# Word categories
words = {
    "fruits": [
        "apple", "banana", "mango", "orange", "grapes", "pear", "papaya",
        "pineapple", "watermelon", "melon", "kiwi", "strawberry", "cherry",
        "guava", "peach", "plum", "blueberry", "blackberry", "lychee"
    ],

    "animals": [
        "tiger", "elephant", "lion", "zebra", "giraffe", "cheetah", "monkey",
        "panda", "kangaroo", "leopard", "bear", "wolf", "fox", "rabbit",
        "camel", "buffalo", "hippopotamus", "rhinoceros", "deer", "goat"
    ],

    "countries": [
        "india", "china", "france", "nepal", "brazil", "canada", "japan",
        "germany", "italy", "russia", "spain", "mexico", "argentina",
        "australia", "egypt", "turkey", "england", "portugal", "sweden",
        "norway"
    ]
}

# Difficulty levels
def filter_by_difficulty(word_list, difficulty):
    if difficulty == "easy":
        return [w for w in word_list if len(w) <= 5]
    elif difficulty == "medium":
        return [w for w in word_list if 6 <= len(w) <= 8]
    elif difficulty == "hard":
        return [w for w in word_list if len(w) > 8]
    else:
        return word_list   # No difficulty chosen

# Return a random word
def get_random_word(category=None, difficulty=None):
    if category in words:
        word_list = words[category]
    else:
        word_list = words["fruits"] + words["animals"] + words["countries"]

    word_list = filter_by_difficulty(word_list, difficulty)
    return random.choice(word_list)
