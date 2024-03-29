from multiprocessing.sharedctypes import Value
import string
from typing import Counter
import discord
import json
import platform
import random
import sys
import os
import i18n
import collections
from discord import *
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.message import Message
from unidecode import unidecode
from os import getenv
from dotenv import load_dotenv
from random import choice
from readWords import readWordsJSON
from Enums import RedLetters, YellowLetters, BlueLetters
from Classes.game import Game, games
from utils import *
from lang import *
import config

load_dotenv()
PREFIX = "!"
words=[]
dict_words_accents={}
DISCORD_TOKEN = config.DISCORD_TOKEN
bot = commands.Bot(command_prefix=PREFIX)
scoreboard = []

def displayScorboard():
    counter = collections.Counter(scoreboard)
    print(counter)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://neovel.io/"))
    print(f"connecté en tant que {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Run sur: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    scoreboard.extend(["Hugo", "Thibo", "Eudrey", "Hugo", "Hugo"])
    counter = collections.Counter(scoreboard)
    # print(counter)
    # next(iter(counter))
    print(counter)
    for i in counter.items():
        print("i a pour valeur", list(i)[0],list(i)[1])


@bot.command()
@commands.has_any_role('Ancient Immortal Ancestor (Administrator)', 'Immemorial Supreme Elder (Manager)', 'Team Neovel', 'Entering Dao')
async def reset(message: Message):
    scoreboard.clear()
    displayScorboard()
    await message.channel.send("Le scoreboard a bien été reset")

@bot.command()
@commands.has_any_role('Ancient Immortal Ancestor (Administrator)', 'Immemorial Supreme Elder (Manager)', 'Team Neovel', 'Entering Dao')
async def top(message: Message):
    counter = collections.Counter(scoreboard)
    await message.channel.send(counter.items())

@bot.command()
@commands.has_any_role('Ancient Immortal Ancestor (Administrator)', 'Immemorial Supreme Elder (Manager)', 'Team Neovel', 'Entering Dao')
async def starten(ctx: Context, difficulty: str = "medium"):
    langEN()
    await start(ctx, difficulty,'EN')

@bot.command()
@commands.has_any_role('Ancient Immortal Ancestor (Administrator)', 'Immemorial Supreme Elder (Manager)', 'Team Neovel', 'Entering Dao')
async def startfr(ctx: Context, difficulty: str = "medium"):
    langFR()
    await start(ctx, difficulty,'FR')

async def start(ctx: Context, difficulty: str = "medium", lang: string = 'EN'):
    if doesGameExist(games, ctx.channel.id):
        await ctx.send(i18n.t('startError'))
        return

    if lang == 'EN':
        words, dict_words_accents = readWordsJSON("../public/motsEN.json")
    else:
        words, dict_words_accents = readWordsJSON("../public/motsFR.json")
    
    random_word = getRandomWordByDifficulty(words, difficulty)

    game = Game(ctx.channel.id, random_word)

    game.setRandomCorrectLetters(2)

    await ctx.send(i18n.t('startGame'))
    await ctx.send(game.correctLettersToString())

@bot.event
async def on_message(message: Message):
    msg = unidecode(message.content).lower()

    # Pass message by bot
    if message.author == bot.user:
        return

    # Pass message not starting with prefix
    if msg.startswith(PREFIX):
        return await bot.process_commands(message)
    
    # if msg.__contains__('<:'):
        return

    # Pass message if no active games in channel
    if not games.get(message.channel.id):
        return

    random_word = games.get(message.channel.id).word

    # Pass if the length of the word is not the same as the random_word
    if len(msg) != len(random_word):
        await message.channel.send(i18n.t('nombreLettreError'))
        return

    # if not msg in words:
    #    return await message.channel.send("Le mot que vous avez écrit n'est pas français.")

    game = games.get(message.channel.id)

    # Create a list with every valid letters
    list_letters = list(random_word)

    # [-, -, -, -, -, -]
    result = [BlueLetters.EMPTY for i in range(len(random_word))]

    # Set all correctly placed letters
    for i, letter in enumerate(msg):
        # If letter is correctly placed
        if letter == random_word[i]:
            # Remove letter from list
            index = list_letters.index(letter)
            list_letters.pop(index)

            # Replace - with valid letter

            letter_append = RedLetters[letter]

            game.correct[i] = letter_append
            result[i] = letter_append

        else:
            result[i] = BlueLetters[letter]

    # Set all letters not correctly placed
    for i, letter in enumerate(msg):
        # If letter is in the list of correct letters
        if letter in list_letters:
            # If letter is already placed continue
            if type(result[i]) != BlueLetters:
                continue

            # Remove letter from list
            index = list_letters.index(letter)
            list_letters.pop(index)

            # Replace - with incorrectly placed letter
            result[i] = YellowLetters[letter]

    historique = game.history
    historique.append(result)

    game.current += 1

    if len(historique) > 2:
        historique.pop(0)

    await message.channel.send(game.historyToString())

    if msg == game.word:
        game.delete()
        await message.channel.send(getRandomPhrase(message.author))
        scoreboard.append(message.author.display_name)
        displayScorboard()
        return

bot.run(DISCORD_TOKEN)