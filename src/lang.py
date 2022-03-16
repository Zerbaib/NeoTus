import i18n
import requests
from random import choice
from bs4 import BeautifulSoup

def langFR():
    i18n.add_translation('startGame',"__**Les régles:**__\n>>> Le but est de trouver le mot en un minimum de coups.\nPour jouer il vous suffit de poster un mot avec le bon nombre de lettre et de trouver le bon (comme un pendue en quelque sorte).\n\n***ATTENTION:***\nLes lettre en rouge <:a_red:953254371460788224> sont des lettre bien placer.\nLes lettre en jaune <:a_yellow:953254371439812608> sont mal placer.\nEt les lettre bleu :regional_indicator_a: sont fausse.")
    i18n.add_translation('startError','Il y a deja une partie en cours !')
    i18n.add_translation('nombreLettreError',':x: Pas le bon nombre de lettre !')
    i18n.add_translation('finDeGame','La partie est terminée !')

def langEN():
    i18n.add_translation('startGame','__**Rules:**__\n>>> The goal is to find the word in as few moves as possible.\nTo play, all you have to do is post a word with the right number of letters and find the right one (like a hangman in a way).\n\n***WARNING:***\nThe letters in red <:a_red:953254371460788224> are well placed letters.\nThe letters in yellow <:a_yellow:953254371439812608> are badly placed .\nAnd the blue letters :regional_indicator_a: are wrong.')
    i18n.add_translation('startError','There is already a game in progress !')
    i18n.add_translation('nombreLettreError',':x: Wrong number of letters !')
    i18n.add_translation('finDeGame','The game is finish !')
