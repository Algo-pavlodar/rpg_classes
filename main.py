from time import sleep
from random import randint

class Hero():
    def __init__(self, nickname, health, armor, power, weapon):
        self.nickname = nickname
        self.hp = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Поприветствуйте героя ->', self.nickname)
        print('Уровень здоровья:', self.hp)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon, '\n')
 
    def strike(self, enemy):
        print('Удар ->')
        print(self.nickname, 'атакует', enemy.nickname, 'используя', self.weapon)
        enemy.armor -= self.power
        if enemy.armor <= 0:
            enemy.hp += enemy.armor
            enemy.armor = 0
        print('Класс брони снизился до', enemy.armor)
        print('Уровень здоровья', enemy.nickname, '-', enemy.hp, '\n')

class Knight(Hero):
    def add_armor(self):
        num = randint(1, 15)
        self.armor += num
        print(self.nickname, 'увеличил свою броню на', num, 'очков!')

class Wizard(Hero):
    def fireball(self, enemy):
        print(self.nickname, 'бросает столб огненного шара в', enemy.nickname)
        enemy.armor = 0
        print(self.nickname, 'расплавил броню', enemy.nickname)
    
    # Массовая атака
    def fire_storm(self):
        global spis
        print(self.nickname, 'призывает силу вулканов, он бросает всю мощь на всех врагов')
        for i in spis:
            if i.nickname == self.nickname:
                continue
            else:
                i.hp -= 9
                print(self.nickname, 'попал в', i.nickname, 'на 9 очков здоровья')
            

ricar = Hero('Ричард', 100, 30, 18, 'меч')
knight = Knight('Геральт', 150, 15, 20, 'меч и щит')
wizard = Wizard('Мерлин', 100, 10, 15, 'Магический посох')

spis = [ricar, knight, wizard]


while len(spis) > 1: #Цикл работает, пока в списке больше 1-го
    for player in spis: # По очереди перебираем всех персонажей
        attack = randint(0, len(spis)-1) # Создаем переменную, где будет рандомное число
        spell = randint(1, 2) # Переменная, для того чтобы понять бить или использовать магию
        if spell == 1: # Если число равно одному, то игрок бьет простым ударом
            player.strike(spis[attack])
            if player.hp < 0:
                print(player.nickname, 'погиб в честном бою.')
                spis.remove(player)
            elif spis[attack].hp < 0:
                print(spis[attack].nickname, 'погиб в честном бою')
                spis.remove(spis[attack])
        elif spell == 2: # Если число равно двум, то игрок использует магию.
            if player.nickname == 'Мерлин':
                player.fire_storm()
            elif player.nickname == 'Геральт':
                player.add_armor()
            else:
                player.strike(spis[attack])
                
            if player.hp < 0:
                print(player.nickname, 'погиб в честном бою.')
                spis.remove(player)
            elif spis[attack].hp < 0:
                print(spis[attack].nickname, 'погиб в честном бою')
                player.strike(spis[attack])
