import requests
from lang import *
from random import choice
from bs4 import BeautifulSoup

def doesGameExist(games, id):
    curr_game = games.get(id, None)

    if curr_game is None:
        return False
        
    return True

def enumsToString(enum_list):
    return " ".join(map(lambda l: l.value,enum_list))

def getRandomWordByDifficulty(words, difficulty: str):
    filter_enum = difficulty_filters[difficulty]

    filtered_words = list(filter(filter_enum, words))

    random_word = choice(filtered_words)  

    return random_word
    
def getRandomPhrase(user):

    phrases = [
        f"Bravo {user.name}, tu as trouvé le mot.",
        f"C'est presque trop facile pour toi {user.name}, bravo.",
        f"Tu as trouvé le mot, mais tu as eu de la chance {user.name}.",
        f"{user.name} a trouvé la réponse ! Mo Mo Motus !",
        f"Bravo {user.name}, tu es un champion !"
    ]
    
    return choice(phrases)

difficulty_filters = {
    "easy": lambda x: (len(x) < 6),
    "medium": lambda x: (5 < len(x) < 9),
    "hard": lambda x: (8 < len(x))
}