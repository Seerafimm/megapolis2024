import csv
m=open('game.txt')
f=m.read()
a=[]
fs= f.split('\n')
for i in fs:
    a.append(i.split(sep='$'))

for i in a:
    if '55' in i[2]:
        characters = str(i[1])
        GameName=str(i[0])
        nameError=str(i[2])
        date=str(i[3])
        print('У персонажа '+ characters+' в игре '+GameName+' нашлась ошибка с кодом: '+ nameError+' Дата фиксации: '+date)
        i[2] = 'Done'
        i[3]= "0000-00-00"

newgame=open('game_new.csv','w')
for el in a:
    newgame.write(','.join(el)+'\n')
