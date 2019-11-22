import time
import random
import fight
import chubrik
from colorama import Fore
x = 1.1
level = 1
day_time = "day"
days_ = 1
card = True
quest_main = False
quest_current = ""
quest_completed = 0
quest_smoked = False
money = 0
random_dialogues = ['> "..Фу, я видел крысу.."','> "..Мне явно поставят двойку.."','> "..Раньше еда была лучше.."','> "..Сегодня плохой день.."','> "..Где бы найти хату на НГ.."','> "..Хочу в туалет.."','> "..Надо бы сесть на диету.."','> "..Патриархат рулит.."']
food = ["Пицца","Человечина","Борщ","Бифштекс из говядины","Филе лосося с пюре","Солянка","Греча с котлетой","Макароны по-флотски","Курица с рисом","Печенка"]
def kitchen():
    print("");print("> Вы пришли в столовую ")
    if card == True:
        time.sleep(x + 1.5)
        print("");print("...")
        time.sleep(x + 2)
        print("");print(random.choice(random_dialogues))
        time.sleep(x + 2)
        print("");print(random.choice(random_dialogues))
        time.sleep(x + 1.5)
        print("");print("...")
        time.sleep(x + 1.7)
        print("");print("> Вы взяли порцию и сели за стол")
        current_food = random.choice(food)
        if current_food == "Пицца":
            time.sleep(x + 1.7)
            print("");print('> Сегодня дают пиццу! Вы говорите: "Найссссс" (HP +10)')
        elif current_food == "Печенка":
            time.sleep(x + 1.7)
            print("");print('> Сегодня дают печенку! Вы говорите: "Фууууу" (HP -10)')
        elif current_food == "Человечина":
            time.sleep(x + 1.7)
            print("");print('> Сегодня дают человечину! Вы говорите: "Фууууу" (HP -10)')
        else:
            time.sleep(x + 1.7)
            print("");print('> Сегодняшнее блюдо:', current_food, '! Вы утолили голод (HP +10)')
    else:
        time.sleep(x + 1.5)
        print("");print("> У вас нет карточки, приходите завтра! (HP -10)")
        hp_current -= 10
#Quest
print("");print(Fore.GREEN + "Super Game")
while True:
    name = input("Выберите имя персонажа: ")
    if len(name) > 12:
        print("");print("Имя не может быть длиннее 12 символов!")
        continue
    else:
        break

while True:
    hero_class = input("Выберите класс персонажа(Инфотехнолог/Повар/Металлист/Логист): ")
    if hero_class == "Инфотехнолог":
        user = chubrik.infotehnolog(name)
        break
    elif hero_class == "Повар":
        user = chubrik.povar(name)
        break
    elif hero_class == "Металлист":
        user = chubrik.matallist(name)
        break
    elif hero_class == "Логист":
        user = chubrik.logist(name)
        break
    else:
        print("");print("Выберите корректный класс!")
        continue
print('good', user.name)
f = open('begin.txt')
for line in f:
    print(line)
    time.sleep(1.25)
f.close()
while True:
    if quest_smoked == False:
        answer = input(Fore.GREEN +"Что делать(Уйти/Драться/Покурить): ")
        if answer == "Драться":
            fight.fight(0,user)
        elif answer == "Уйти":
            time.sleep(x + 2.15)
            print("");print('> Вы решили не бить малышню и пошли дальше')
            kitchen()
        elif answer == "Покурить":
            time.sleep(x + 1.5)
            print("");print("...")
            time.sleep(x + 1.5)
            print("");print('> Вы пошли курить')
            time.sleep(x + 1.5)
            print("");print("...")
            time.sleep(x + 1.5)
            print(""); print("> Подходит Захар и просит сигарету")
            while True:
                answer = input('Дать сигаретету?(Да/Нет): ')
                if answer == "Да":
                    print(""); print("> Вы дали Захару сигарету, он уходит")
                    time.sleep(x + 2)
                    print(""); print("> Вы спокойно докурили сигарету и пошли в школу")
                    time.sleep(x + 2)
                    print(""); print("> Миссия выполнена : [Сходи покури!]")
                    quest_smoked = True 
                    time.sleep(x + 2)
                    break
                else:
                    print(""); print("> На вас напал Захар!")
                    ch = 1
                    fight.fight(1,user)
        else:
            print("");print('[Такого варианта нет!]')       
            continue
    else:
        answer = input(Fore.GREEN +"Что делать(Уйти/Драться): ")
        if answer == "Драться":
            ch = 2
            fight.fight(0,user)
        elif answer == "Уйти":
            time.sleep(x + 2.15)
            print("");print('> Вы решили не бить малышню и пошли дальше')
            time.sleep(x + 2)
            kitchen()
            break
        else:
            print("");print('[Такого варианта нет!]')
            continue