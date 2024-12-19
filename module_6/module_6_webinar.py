import random

class Character:

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack (self, other):
    # Расчет атаки
        damage = random.randint(1, self.attack_power)

        print('--------------------------------------------------')
        print(f'{self.name} атакует {other.name}!')

        other.take_damage(damage)

    def take_damage(self, damage):
    # расчет урона
        self.health -= damage
        print(f'{self.name} получает {damage} урона! \n'
              f'Осталось здоровья у {self.name}: {self.health}')


    def is_alive(self):
        # Проверка жив ли герой
        return self.health > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)

    def special_attack(self, other):
        damage = random.randint(5, self.attack_power * 2)
        print('--------------------------------------------------')
        print(f'{self.name} выполняет специальную атаку {other.name}')
        other.take_damage(damage)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=70, attack_power=15)

    def special_attack(self, other):
        damage = random.randint(15, self.attack_power + 25)
        print('--------------------------------------------------')
        print(f'{self.name} выполняет магическую атаку на {other.name}')
        other.take_damage(damage)

def battle(character1, character2):

    while character1.is_alive() and character2.is_alive():

        action = random.choice(['attack', 'spec_attack'])
        if (isinstance(character1, Warrior) and action == 'spec_attack'
                or isinstance(character2, Warrior) and action == 'spec_attack'):
            character1.special_attack(character2)
            character2.special_attack(character1)

        elif (isinstance(character1, Mage) and action == 'spec_attack'
              or isinstance(character2, Mage) and action == 'spec_attack'):
            character1.special_attack(character2)
            character2.special_attack(character1)

        else:
            character1.attack(character2)
            character2.attack(character1)

        if not character1.is_alive():
            print(f'{character1.name} побежден! вы  проиграли ')
            break
        if not character2.is_alive():
            print(f'{character2.name} побежден! Вы одержали победу')
            break

def main():
    print('========================================================')
    print('!!!        Добро пожаловать в игру ГЕРОИ             !!!')
    print('========================================================')
    player_name = input('Введите имя героя: \n')
    choice = input('Выберите класс (воин . маг): \n').lower()

    if choice == 'воин':
        player = Warrior(player_name)
    elif choice == 'маг':
        player = Mage(player_name)
    else:
        print('Некорректный выбор, создается воин по умолчанию')
        player = Warrior(player_name)

    choice = random.choice(['воин', 'маг'])

    if choice == 'воин':
        enemy = Warrior('Дракон')

    else:
        enemy = Mage('Магический дракон')
    print(f'Против Вас играет {enemy.name}, класс {choice}')
    print('--------------------------------------------------')

    print(f'\n{player.name}  начинает бой против {enemy.name}')

    battle(player, enemy)
    print()
    message = input('Хотите продолжить? Нажмите любую клавишу, для выхода нажмите - 0 \n')
    if message == '0':
        exit()
    else:
        main()

main()
