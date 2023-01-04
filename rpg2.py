import random
import time

class Player :
    def __init__(self,name,hp,damage,class_player,race_player):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.lvl = +1
        self.exp = 0
        self.class_player = class_player
        self.race_player = race_player


    # level up
    @staticmethod
    def lvl_up():
        hero.exp = 0
        hero.hp += 10*hero.lvl
        hero.damage += 7*hero.lvl
        hero.lvl += 1
        print(f'Вы достигли уровня {hero.lvl}')
        return hero.lvl

    @staticmethod
    def create_weapon():
        weapon_type_list = ['меч','лук']
        weapon_rare_dict = {
            1:'Обычный',
            1.5:'Редкий',
            2:'Эпический',
            5:'Невероятно редкий!'
        }
        random_weapon_type = weapon_type_list[random.randint(0,len(weapon_type_list)-1)]
        random_weapon_rare = random.choice(list(weapon_rare_dict.keys()))

        if random_weapon_type == weapon_type_list[0]:
            hero.damage += 5*random_weapon_rare
        elif random_weapon_type == weapon_type_list[1]:
            hero.damage += 3*random_weapon_rare
        return random_weapon_type,weapon_rare_dict[random_weapon_rare]

    @staticmethod
    def create_heal():
        heal_dict = {
            15:'Маленькая аптечка',
            25:'Средняя аптечка',
            50:'Большая аптечка',
        }

        random_heal = random.choice(list(heal_dict.keys()))

        hero.hp += random_heal
        return heal_dict[random_heal]

    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print(victim.name, 'Повержен, + 25 опыта.')
            time.sleep(0.5)
            self.exp += 25
            print(f'Ваш опыт : {self.exp}')
            level = 1 + self.lvl*50
            if self.exp >= level:
                Player.lvl_up()

            heal_weapon_choice = random.choice(list(choice_list))
            if heal_weapon_choice == 'weapon':
                weapon = Player.create_weapon()
                print(f'Вам выпало оружие! {weapon[0], weapon[1]}')
                print(f'Ваш урон теперь {self.damage}')
                time.sleep(.7)
            elif heal_weapon_choice == 'heal':
                heal = Player.create_heal()
                print(f'Вам выпало {heal}')
                print(f'Ваше здоровье теперь {self.hp}')
                time.sleep(.7)
                return False
            else:
                print(f'{victim.name} теперь имеет {victim.hp} очков здоровья')
                time.sleep(0.5)
                return True

            return False
        else:
            print(self.name, 'Нанёс атаку:%s' % self.damage)
            print(victim.name, 'Теперь имеет', victim.hp, 'Здоровья')
            return True
# метод создания персонажа
def create_hero(name,race_player,class_player):
    hp = 0
    damage = 0

    if race_player == races_list[0]:
        hp += 200
        damage += 200
    elif race_player == races_list[1]:
        hp += 40
        damage += 35
    elif race_player == races_list[2]:
        hp += 70
        damage += 20
    elif race_player == races_list[3]:
        hp += 40
        damage += 40
    else:
        print('Я не знаю такой расы')
        quit()

    if class_player == class_list[0]:
        hp += 10
        damage += 20
    elif class_player == class_list[1]:
        hp += 20
        damage += 10
    else:
        print('Я не знаю такого класса')
        quit()

    return Player(name,hp,damage,class_player,race_player)



class Enemy :
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage



    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print(victim.name,'Убит.Конец игры')
            quit()
        else:
            print(self.name, 'Нанёс атаку:%s'% self.damage)
            print(victim.name, 'Теперь имеет',victim.hp, 'Здоровья')


def create_enemy():
    names_enemy = ['Вампир', 'Скелет']
    name = random.choice(names_enemy)
    hp = random.randint(40, 90) + 15*hero.lvl
    damage = random.randint(30, 70) + 12*hero.lvl
    return Enemy(name, hp, damage)


# блок со списками
person = []
races_list = ['эльф','гном','хоббит','человек']
class_list =['лучник','мечник']
choice_list =['weapon','heal']

# блок со созданием персонажа

print('Здравстуйте,как вас зовут?')
person.append(input())
print('Кем вы хотите играть?')
for race in races_list:
    print(race,end=' ')
print()
person.append(input())
print('К какому классу вы относитесь?')
for name in class_list:
    print(name,end=' ')
print()
person.append(input())

hero = create_hero(person[0],person[1],person[2])
print(hero.name)
print(hero.hp)
print(hero.damage)
print(hero.race_player)
print(hero.class_player)


def fight_choice():
    answer = int(input('Атаковать(нажми на 1) или бежать (нажми на 2)'))
    if answer == 1:
        win_lose = hero.attack(enemy)
        if win_lose:
            time.sleep(.5)
            enemy.attack(hero)
            fight_choice()
    elif answer == 2:
        plan = random.randint(0, 1)
        if plan == 0:
            print('Побег не удался. Вы подтвергаетесь нападению монстром')
            enemy.attack(hero)
            fight_choice()
        elif plan == 1:
            print('Вы сбежали от монстра')
            time.sleep(1)
    else:
        print('Будь внимательнее,ибо у меня нет такого варианта ответа')
        fight_choice()



while True:
    event = random.randint(0,1)
    if event == 0:
        print('Вам никто не встретился,идём дальше')
        time.sleep(1)
    elif event == 1:
        enemy = create_enemy()
        print(f"Вам встретился {enemy.name} ")
        print(f"Здоровье -> {enemy.hp} \n"
              f"Урон -> {enemy.damage}")
        fight_choice()

