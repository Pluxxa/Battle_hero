import random
import time


class Hero():
    def __init__(self, name="Hero", hp=100, s=20):
        self.name = name
        self.s = s
        self.hp = hp

    def attack(self, other):
        a = random.randint(1, self.s)
        other.hp = other.hp - a
        print(f"{self.name} нанес {a} урона")

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False


class Game():
    def __init__(self):
        self.hero = Hero()
        self.computer = Hero(name="Computer")

    def start(self):
        for _ in range(100):
            ini1 = random.randint(0, 10)
            ini2 = random.randint(0, 10)
            if self.hero.is_alive() == True and self.computer.is_alive() == True:
                print(f"Раунд {_+1}\n")
                time.sleep(1)
                self.hero.attack(other=self.computer)
                print(f"У {self.computer.name} осталось {self.computer.hp} жизней\n")
                time.sleep(1)
                self.computer.attack(other=self.hero)
                print(f"У {self.hero.name} осталось {self.hero.hp} жизней\n")
                time.sleep(1)
            else:
                if self.computer.is_alive() == True:
                    print(f"{self.computer.name} победил!!!")
                    exit()
                else:
                    print(f"{self.hero.name} победил!!!")
                    exit()


game = Game()

game.start()