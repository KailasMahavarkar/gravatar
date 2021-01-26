import random
from PIL import Image
from Gravatar.color import *


def func(myList):
    for x in range(5):
        myList[x] = random.choice([0, 1])
    return myList


p1 = p5 = func([0, 0, 0, 0, 0])
p2 = p4 = func([0, 0, 0, 0, 0])
p3 = func([0, 0, 0, 0, 0])

grav = []

for x in [p1, p2, p3, p4, p5]:
    grav.extend(x)


class AVATAR:
    def __init__(self, box=1000, bgColor='ivory', color='red'):
        self.box = box
        self.bgColor = bgColor
        self.color = color
        self.block = box // 5

        # making background
        self.new = Image.new(mode='RGB', size=(box, box), color=self.bgColor)

        self.points = {}
        number = 0
        cordinates = [0, self.block * 1, self.block * 2, self.block * 3, self.block * 4]

        for x in cordinates:
            for y in cordinates:
                self.points.update({number: (x, y)})
                number += 1

    def generate(self):
        colorBlock = Image.new(mode='RGB', size=(self.block, self.block), color=self.color)

        for x in range(len(grav)):
            if grav[x] == 1:
                self.new.paste(colorBlock, self.points[x])

        self.new.save('test.jpg')


if __name__ == '__main__':
    AVATAR(
        box=500,
        bgColor=getRandomName(),
        color=getRandomName()
    ).generate()