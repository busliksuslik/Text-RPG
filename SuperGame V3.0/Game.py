import time
import random
import fight
from colorama import Fore
print("");print(Fore.CYAN + "Super Game")
time.sleep(0.5)
done = 0
hp_max = 1
hp_current = 1
dmg = 1
defen = 1
ilg = 1
x = 0
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
def kitchen(): #Функция, отвечающая за приход в столовую
    print("");print(Fore.GREEN + "> Вы пришли в столовую ")
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
            #hp_current += 10
            time.sleep(x + 1.6)
            print("");print("> Радостный и сытый вы ушли из столовой")
        elif current_food == "Печенка":
            time.sleep(x + 1.7)
            print("");print('> Сегодня дают печенку! Вы говорите: "Фууууу" (HP -10)')
            #hp_current -= 10
            time.sleep(x + 1.6)
            print("");print("> Голодный вы ушли из столовой")
        elif current_food == "Человечина":
            time.sleep(x + 1.7)
            print("");print('> Сегодня дают человечину! Вы говорите: "Фууууу" (HP -10)')
            #hp_current -= 10
            time.sleep(x + 1.6)
            print("");print("> Голодный вы ушли из столовой")
        else:
            time.sleep(x + 1.7)
            print("");print('> Сегодняшнее блюдо:', current_food, '! Вы утолили голод!')
            time.sleep(x + 1.6)
            print("");print("> Сытый вы ушли из столовой")
    else:
        time.sleep(x + 1.5)
        print("");print("> У вас нет карточки, приходите завтра! (HP -10)")
        #hp_current -= 10
while True: # Цикл выбора имени персонажа
    name = input(Fore.GREEN + "Выберите имя персонажа: ")
    if len(name) > 12:
        print("");print(Fore.RED +"Имя не может быть длиннее 12 символов!")
        continue
    else:
        break
while True: # Цикл выбора класса персонажа
    hero_class = input(Fore.GREEN + "Выберите класс персонажа(Инфотехнолог/Повар/Металлист/Логист): ") 
    if hero_class == "Инфотехнолог":
        hp_max = 100
        hp_current = 100
        dmg = 40
        defen = 40
        ilg = 100
        break
    elif hero_class == "Повар":
        hp_max = 300
        hp_current = 300
        dmg = 75
        defen = 50
        ilg = 0
        break
    elif hero_class == "Металлист":
        hp_max = 500
        hp_current = 500
        dmg = 95
        defen = 70
        ilg = 0
        break
    elif hero_class == "Логист":
        hp_max = 200
        hp_current = 200
        dmg = 35
        defen = 40
        ilg = 50
        break
    else:
        print("");print(Fore.RED + "Выберите корректный класс!")
        continue
print("");print("...")
time.sleep(x + 1.25)
print("");print(Fore.GREEN + "> Вы сидите на уроке карьерного планирования")
time.sleep(x + 2.15)
print("");print('> "..Я рада видеть вас здесь сегодня.."')
time.sleep(x + 2.15)
print("");print('> "..На данный момент у нас обучается около 2500 студентов.."')
time.sleep(x + 2.15)
print("");print('> "..Учеба проходит как на русском, так и на эстонском языке.."')
time.sleep(x + 2.15)
print("");print('> "..Хорошие ученики получают степендию.."')
time.sleep(x + 2.15)
print("");print('> "..Если вы чувствуете себя плохо, можете сходить к медсестре.."')
time.sleep(x + 2.15)
print("");print('> "..После 2 пары все дружно идем кушать в столовую.."')
time.sleep(x + 2.15)
print("");print('> "..Курить на территории профтеха запрещено.."')
time.sleep(x + 2.15)
print("");print('> "..Надеюсь вы будете вести себя хорошо!.."')
time.sleep(x + 2.15)
print("");print("...")
time.sleep(x + 1.75)
print("");print('> * звенит звонок *')
time.sleep(x + 2.15)
print("");print('> "..Идите кушать!.."')
time.sleep(x + 2)
print("");print('> Вы выходите из класса')
time.sleep(x + 1.8)
print("");print("> Новый квест : [Сходи покури!]")
time.sleep(x + 1.8)
print("");print("...")
time.sleep(x + 1.65)
print("");print('> Вас окликивает малышня, кажется они хотят драться')
while True:
    if done == 1:
        break
    if quest_smoked == False:
        answer = input(Fore.GREEN + "Что делать(Уйти/Драться/Покурить): ")
        if answer == "Драться":
            hero = 1
            money += fight.fight(level,hp_max,hp_current,dmg,defen,hero)
            while True:
                if done == 1:
                    break
                answer = input(Fore.GREEN + "Что делать(Уйти/Покурить): ")
                if answer == "Покурить":
                    time.sleep(x + 1.5)
                    print("");print("...")
                    time.sleep(x + 1.5)
                    print("");print(Fore.GREEN + '> Вы пошли курить')
                    time.sleep(x + 1.5)
                    print("");print("...")
                    time.sleep(x + 1.5)
                    print(""); print(Fore.GREEN + "> Подходит Захар и просит сигарету")
                    while True:
                        if done == 1:
                            break
                        answer = input(Fore.GREEN + 'Дать сигарету?(Да/Нет): ')
                        if answer == "Да":
                            print(""); print(Fore.GREEN + "> Вы дали Захару сигарету, он уходит")
                            time.sleep(x + 2)
                            print(""); print(Fore.GREEN + "> Вы спокойно докурили сигарету и пошли в школу")
                            time.sleep(x + 2)
                            print(""); print(Fore.MAGENTA + "> Миссия выполнена : [Сходи покури!]")
                            quest_smoked = True 
                            time.sleep(x + 1)
                            print("");print(Fore.GREEN + '> Довольный собой вы пошли в столовую')
                            time.sleep(x + 2)
                            kitchen()
                            done = 1
                        else:
                            print(""); print("> На вас напал Захар!")
                            hero = 0
                            money += fight.fight(level,hp_max,hp_current,dmg,defen, hero)
                            print(""); print(Fore.GREEN + "> Захару, кажется, больше не нужна сигарета")
                            time.sleep(x + 2)
                            print(""); print(Fore.GREEN + "> Вы спокойно докурили сигарету и пошли в школу")
                            time.sleep(x + 2)
                            print(""); print(Fore.MAGENTA + "> Миссия выполнена : [Сходи покури!]")
                            quest_smoked = True                            
                            time.sleep(x + 2)
                            print("");print(Fore.GREEN + '> Довольный собой вы пошли в столовую')
                            time.sleep(x + 1)
                            kitchen()
                            done = 1
                elif answer == "Уйти":
                    time.sleep(x + 2.15)
                    print("");print(Fore.GREEN + '> Довольный собой вы пошли в столовую')
                    time.sleep(x + 1)
                    kitchen()
                    done = 1
                else:
                    print("");print(Fore.RED +'[Такого варианта нет!]')
                    time.sleep(x + 1)
                    continue
        elif answer == "Уйти":
            time.sleep(x + 2.15)
            print("");print(Fore.GREEN + '> Вы решили не бить малышню и пошли дальше')
            time.sleep(x + 1)
            kitchen()
            done = 1
        elif answer == "Покурить":
            time.sleep(x + 1.5)
            print("");print("...")
            time.sleep(x + 1.5)
            print("");print(Fore.GREEN + '> Вы пошли курить')
            time.sleep(x + 1.5)
            print("");print("...")
            time.sleep(x + 1.5)
            print(""); print(Fore.GREEN + "> Подходит Захар и просит сигарету")
            while True:
                if done == 1:
                        break
                answer = input(Fore.GREEN + 'Дать сигарету?(Да/Нет): ')
                if answer == "Да":
                    print(""); print(Fore.GREEN + "> Вы дали Захару сигарету, он уходит")
                    time.sleep(x + 2)
                    print(""); print(Fore.GREEN + "> Вы спокойно докурили сигарету и пошли в школу")
                    time.sleep(x + 2)
                    print(""); print(Fore.MAGENTA + "> Миссия выполнена : [Сходи покури!]")
                    quest_smoked = True 
                    time.sleep(x + 2)
                    break
                else:
                    print(""); print(Fore.RED +"> На вас напал Захар!")
                    hero = 0
                    money += fight.fight(level,hp_max,hp_current,dmg,defen,hero)
                    print(""); print(Fore.GREEN + "> Захару, кажется, больше не нужна сигарета")
                    time.sleep(x + 2)
                    print(""); print(Fore.GREEN + "> Вы спокойно докурили сигарету и пошли в школу")
                    time.sleep(x + 2)
                    print(""); print(Fore.MAGENTA + "> Миссия выполнена : [Сходи покури!]")
                    quest_smoked = True 
                    time.sleep(x + 2)
                    break
        else:
            print("");print(Fore.RED +'[Такого варианта нет!]')       
            continue
    else:
        answer = input(Fore.GREEN + "Что делать(Уйти/Драться): ")
        if answer == "Драться":
            hero = 1
            money += fight.fight(level,hp_max,hp_current,dmg,defen, hero)
            time.sleep(x + 2.15)
            print("");print(Fore.GREEN +'> Довольный собой вы пошли в столовую')
            time.sleep(x + 1)
            kitchen()
            done = 1       
        elif answer == "Уйти":
            time.sleep(x + 2.15)
            print("");print(Fore.GREEN + '> Вы решили не бить малышню и пошли дальше')
            time.sleep(x + 2)
            kitchen()
            done = 1  
        else:
            print("");print(Fore.RED +'[Такого варианта нет!]')
            continue
time.sleep(x + 1) 
print("");print("")
print(Fore.CYAN + " ~ ~ ~ ~ ~ ~ ~ ~ ~ ") 
print(Fore.CYAN + " ~ ~ ~ Конец ~ ~ ~ ")
print(Fore.CYAN + " ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
input("")