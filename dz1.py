import random

N = int(input("Введите количество команд: "))
current_players = list()
dict_of_players = dict()
num_of_stage = int(N/2)

def game(dict_p, p1, p2, st):
    gol1 = random.randint(0,5)
    gol2 = random.randint(0,5)
    if gol1 > gol2 or gol2 > gol1:
        dict_p[p1][st] =[p2, gol1, gol2]
        dict_p[p2][st] = [p1, gol2, gol1]
    if gol1 == gol2:
        pen1 = 0
        pen2 = 0
        while pen1 == pen2:
            pen1 = pen1+random.randint(0,1)
            pen2 = pen2 + random.randint(0, 1)
        dict_p[p1][st] = [p2, gol1, gol2, "пенальти", pen1, pen2]
        dict_p[p2][st] = [p1, gol2, gol1, "пенальти", pen2, pen1]
    return

def stage(dict_p,list_p,st):
    while len(list_p) !=0:
        player1 = random.choice(list_p)
        list_p.remove(player1)
        player2 = random.choice(list_p)
        list_p.remove(player2)
        game(dict_p, player1, player2, st)
    return

def play_off(st):
    for key in dict_of_players:
        if dict_of_players[key].get(st):
            temp = dict_of_players[key][st]
            if temp[1] == temp[2]:
                if temp[4] > temp[5]:
                    current_players.append(key)
            if temp[1] > temp[2]:
                current_players.append(key)

for i in range(N):
    s=input("Введите название команды: ")
    current_players.append(s)
    dict_of_players[s] = {num_of_stage: list()}

print("Турнир начался!!!!")

while num_of_stage >= 1:
    stage(dict_of_players,current_players,num_of_stage)
    print(dict_of_players)
    play_off(num_of_stage)
    if num_of_stage == 1:
        break
    num_of_stage = int(num_of_stage/2)
    for key in dict_of_players:
        if key in current_players:
            dict_of_players[key][num_of_stage] = list()

for key in dict_of_players:
    if dict_of_players[key].get(1):
        temp = dict_of_players[key][1]
        if temp[1] == temp[2]:
            if temp[4] > temp[5]:
                print("Турнир закончился!!! Победила команда {}\n".format(key))
                break
        if temp[1] > temp[2]:
            print("Турнир закончился!!! Победила команда {}\n".format(key))
            break


while 1 :
    an = input("Хотите подробнее узнать о том, как сыграла определенная команда? Введите название команды или no: ")
    if an == "no":
        break
    for key in dict_of_players[an]:
        if dict_of_players[an][key][1] != dict_of_players[an][key][2]:
            print("Cтадия 1/{} ,играла с {}, счет {}:{}".format(key,dict_of_players[an][key][0],
                                                                dict_of_players[an][key][1],
                                                                dict_of_players[an][key][2]))
        if dict_of_players[an][key][1] == dict_of_players[an][key][2]:
            print("Cтадия 1/{} ,играла с {}, счет {}:{} пенальти {}:{}".format(key, dict_of_players[an][key][0],
                                                                dict_of_players[an][key][1],
                                                                dict_of_players[an][key][2],
                                                                dict_of_players[an][key][4],
                                                                dict_of_players[an][key][5]))





