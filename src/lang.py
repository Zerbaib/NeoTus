import i18n
import requests
from utils import *
from random import choice
from bs4 import BeautifulSoup

def langFR():
    i18n.add_translation('startGame', "__**Les régles:**__\n>>> Le but est de trouver le mot en un minimum d’essais.\nPour jouer il vous suffit de poster un mot avec le bon nombre de lettres et de trouver le bon mot (comme une sorte de pendu).\n\n***ATTENTION:***\nUne lettre en rouge <:a_red:953254371460788224> est bien placée.\nUne lettre en jaune <:a_yellow:953254371439812608> existe dans le mot mais est mal placée.\nUne lettre en bleu :regional_indicator_a: n'existe pas dans le mot.")
    i18n.add_translation('startError', 'Il y a déjà une partie en cours !')
    i18n.add_translation('nombreLettreError', ':x: Pas le bon nombre de lettres !')
    i18n.add_translation('finDeGame', 'La partie est terminée !')

def langEN():
    i18n.add_translation('startGame', '__**Rules:**__\n>>> The goal is to find the word in as few tries as possible.\nTo play you just have to post a word with the right number of letters and find the right word (like a kind of hangman).\n\n***WARNING:***\nA letter in red <:a_red:953254371460788224> is well placed.\nA yellow letter <:a_yellow:953254371439812608> exists in the word but is misplaced.\nA blue letter :regional_indicator_a: does not exist in the word')
    i18n.add_translation('startError', 'There is already a game in progress !')
    i18n.add_translation('nombreLettreError', ':x: Wrong number of letters !')
    i18n.add_translation('finDeGame', 'The game is finish !')
