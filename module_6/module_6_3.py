import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANDER = 0

    def __init__(self, speed, _cords = [0, 0, 0]):
        self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        flag= True

        self._cords[0] = self._cords[0] + dx*self.speed
        self._cords[1] = self._cords[1] + dy*self.speed
        self._cords[2] = self._cords[2] + dz*self.speed

        for i in range(len(self._cords)):
            if self._cords[i] < 0:
                self._cords[i] = 0
                flag = False
        if not flag:
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X:{ self._cords[0]}, Y:{self._cords[1]}, Z:{ self._cords[2]}')

    def attack(self):
        danger = self._DEGREE_OF_DANDER
        if danger < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        sound = self.sound
        print(sound)

class Bird(Animal):
    beak = True
    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        random_eggs = random.randint(1,4)
        print(f"Here are(is) {random_eggs} eggs for you")

class AquaticAnimals(Animal):
    _DEGREE_OF_DANDER = 3

    def dive_in(self, dz):
        self._cords[2] = int(abs(self._cords[2] - dz*(self.speed/2)))
        return self._cords[2]

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANDER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimals):
    sound = "Click-click-click"


db = Duckbill(10)

# print(Duckbill.mro())
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()

db.dive_in(6)
db.get_cords()

db.lay_eggs()