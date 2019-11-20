import random,time
from colorama import Fore
from colorama import init
init()
def fight(lvl,mhp,hp,dmg,defen,hero):
    edmg = ehp = edefen =fdmg= 1
    elvl = round(lvl*1.1*random.randint(1,5))
    ch = random.randint(0,6)
    if hero == -1:
        random.randint(0,6)
    if hero ==0:
        print("");print(Fore.RED + '> Вы встретели Захара')
        time.sleep(0.5)
        ehp = 300
        edefen = 1
        edmg == 70
    elif hero ==1:
        print("");print(Fore.RED + '> Вы встретели малышню')
        time.sleep(0.5)
        ehp = 100
        edefen = 1
        edmg == 60
    elif hero ==2:
        print("");print(Fore.RED + '> Вы встретели задиру')
        time.sleep(0.5)
        ehp = 200
        edefen = 50
        edmg == 100
    elif hero ==3:
        print("");print(Fore.RED + '> Вы встретели Марию')
        time.sleep(0.5)
        ehp = 999
        edefen = 999
        edmg == 999
    elif hero ==4:
        print("");print(Fore.RED + '> Вы встретели фемку')
        time.sleep(0.5)
        ehp = 250
        edefen = 100
        edmg == 200
    elif hero == 5:
        print("");print(Fore.RED + '> Вы встретели Гитлера')
        time.sleep(0.5)
        ehp = 1
        edefen = 1
        edmg == 1
    print(Fore.RED + '> Здоровье противника: ',ehp)
    print(Fore.RED + '> Атака противнка: ',edmg)
    print(Fore.RED + '> Сопротивление урону противника: ',edefen)
    time.sleep(1.2)
    print("");print(Fore.RED + '> Вы ходите первым')
    while True:
        ch = input(Fore.RED + 'Выберете приём(Удар/Лечение): ')
        if ch == "Удар":
            fdmg = dmg * (1/edefen)
            ehp = round(ehp - fdmg) 
            time.sleep(1.2)
            print("");print(Fore.RED + '> Здоровье противника: ',ehp)
            if ehp <=0:
                time.sleep(1.2)
                print("");print(Fore.YELLOW + '~ Вы победили ~')
                time.sleep(1)
                print("");print("...")
                time.sleep(1)
                print("");print(Fore.GREEN + '> Обыскав труп вы заработали',(elvl)*random.randint(3,5),'евро')
                return (elvl)*random.randint(3,5)
                break
        if ch == "Лечение":
            hp  = hp + lvl*12
            if hp>mhp:
                hp =100
            print(Fore.RED + hp,'> Очков здоровья')
        time.sleep(1.2)
        print("");print(Fore.RED + '> Ход противника')
        time.sleep(1.2)
        fdmg = edmg * (1/defen)
        if fdmg ==0:
            print(Fore.RED + '> Противник промахнулся')
            time.sleep(1.2)
        else:
            hp = round(hp - fdmg)
            time.sleep(1)
            print("");print(Fore.RED + '> Ваше здоровье: ',hp)
            time.sleep(1.3)
        if hp<=0:
            print("");print(Fore.RED + '~ Вы проиграли ~')
            return 0