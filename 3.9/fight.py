import chubrik
import random
import time
def fight(num, user):
    if num ==0:
        num = random.randint(1,6)
    if num == 1:
        ene = chubrik.zahar()     
    if num == 2:
        ene = chubrik.babes() 
    if num == 3:
        ene = chubrik.maria()  
    if num == 4:
        ene = chubrik.zadira() 
    if num == 5:
        ene = chubrik.femka() 
    if num == 6:
        ene = chubrik.hitler() 
    print('вы встретели врага:',ene.name)
    print('его очки здоровья:',ene.hp)
    print('его урон:',ene.dmg)
    print('его защита',ene.defen)
    print('ваши очки здоровья:',user.hp)
    print('ваш урон:',user.dmg)
    print('ваша защита',user.defen)
    time.sleep(1.25)
    print('вы атакуете первым')
    for  i in range(1,10):
        ene.hp = ene.hp - user.dmg
        print('вы нанесли',user.dmg,'урона')
        print(ene.hp)
        if ene.hp<0:
            print('вы победили')
            print('обыскав труп вы нашли')
            user.money += 10 
            break
        user.hp = user.hp - ene.dmg
        print('противник нанёс',user.dmg,'урона')
        print(user.hp)
        if user.hp < 0:
            print('вы проиграли')
            return 0 
            break            
            