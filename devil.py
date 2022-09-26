import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import random
from PIL import Image
import requests

Image.open(requests.get(https://twitter.com/black_swan_man/status/1525097236564254722/photo/1, stream=True).raw)

money_human = int(input("How much money should Spitz start out with?"))
class Dice:
    sides = [1,2,3,4,5,6]
    converter = {1: 0.5, 2: 1.05, 3: 1.05, 4:1.05, 5:1.05, 6:1.5}
    def roll(self):
        return random.choice(self.sides)

    def convert(self, roll):
        return self.converter[roll]

class Person:
    def __init__(self,money, name):
        self.money = money
        self.name  = name

class Game:
    def __init__(self, person_1, person_2, dice):
        self.person_1 = person_1
        self.person_2  = person_2
        self.dice  = dice

    def round(self):
        roll  = self.dice.roll()
        percent = self.dice.convert(roll)

        is_win = True if percent > 1 else False

        if is_win:
            difference = self.person_1.money*percent - self.person_1.money 
            self.person_1.money *= percent
            self.person_2.money - difference
        else:
            demon_gains = self.person_1.money * percent
            self.person_1.money *= percent
            self.person_2.money += demon_gains


    def simulate(self, rounds):
        rounds = range(rounds)
        for x in rounds:
            self.round()


results = []
for _ in range(10_000):
    dice = Dice()
    spitz = Person(money_human, "Spitz")
    demon = Person(float('inf'), "DEMON")
    game = Game(spitz,demon,dice)

    game.simulate(300)

    results.append(spitz.money)

#plt.hist(results, bin=range(0,1_000_000, ))
plt.hist(results, bins=np.linspace(0,100_000,110))
plt.show()
