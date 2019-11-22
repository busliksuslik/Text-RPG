class chubrik(object):
    lvl = 1
    dmg = 1
    defen = 1
    hp = 100 
    def defence(self,damage):
        chubrik.hp = chubrik.hp - damage
class player(chubrik):
    name = ''
    money = 10
    def __init__(self,a):
        player.name = str(a)
    def special():
        print('lol')
    def get_name (self):
        print(player.name)
    def say_money(self):
        print(player.money)
    def get_money(self):
        return player.money
class infotehnolog(player):
    dmg = 100
    defen = 100
    hp = 100
class povar(player):
    dmg = 100
    defen = 100
    hp = 100
class matallist(player):
    dmg = 100
    defen = 100
    hp = 100
class logist(player):
    dmg = 100
    defen = 100
    hp = 100
class enemy(chubrik):
    name = ''
class zahar(enemy):
    name  = 'захар'
    hp = 300
    dmg = 1
    defen = 1
class babes(enemy):
    name  = 'малышня'
    hp = 100
    defen = 1
    dmg = 50
class maria(enemy):
    name  = 'Мария'
    hp = 999
    defen = 999
    dmg = 999
class zadira(enemy):
    name  = 'задира'
    hp = 200
    defen = 100
    dmg = 50
class femka(enemy):
    name  = 'фемка'
    hp = 250
    defen = 100
    dmg = 200
class hitler(enemy):
    name  = 'гитлер'
    hp = 1
    defen = 1
    dmg = 0