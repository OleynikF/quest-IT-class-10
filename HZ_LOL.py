import sys
from time import sleep

letter = 0
blue_room_safe = 0
green_room_safe = 0

popitki = 3
green_key = 0
blue_room_key = 0
blue_room_knife = 0
b = 0
green_key = 0


def inventory():
    f = open('inventory', 'r')
    slowprint(f.read())
    f.close()

def addpredmet(srtg):
    f = open('inventory', 'a')
    f.write(str(strg))
    f.close()


def exit_blue_room():
    slowprint("Когда я нашел ключ, я начал искать замок, куда его можно вставить. И тут я нашел дверь, которая была тщательно замаскирована. Отодвинув заслонку, которая закрывала замочную скважину от лишних глаз, я вставил туда ключ\n")
    slowprint("Дверь легко поддалась и я зашел в новую комнату\n")

def osmotr_green_room():
    slowprint("Я вошел в новую комнату. Передо мной появилось Огромное, вырезанное из камня лицо Сфинкса. Кроме него в этой комнате зеленого цвета ничего не было. \n")
    slowprint("Я тщательно осмотрел скульптуру, и увидел что на носу сфинкса есть кнопка, на которую можно нажать. Так как делать было больше нечего, я нажал на нее. \n")
    slowprint("Из колонок внутри статуи вдруг послышался голос: 'Кто ходит утром на четырех ногах, днем на двух, вечером на трех?' \n")
    slowprint("Это загадка, значит я должен дать на нее ответ. Учитывая что в статуе есть колонки, то скорее всего должен быть и микрофон. Так что я просто должен громко и четко сказать ответ.\n")
    slowprint("Какой же ответ я дам?\n")
    otvet = input()
    if (otvet.lower() == "человек"):
        slowprint("Я услышал звуки механические откуда-то из-за стены. Спустя несколько минут, механическая дверь начала открываться с характерным скрипом ржавого металла. \n")
    else:
        if (popitki != 0):
            popitki -= 1




def slowprint(letters):
    words = letters
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

def tochki(chislo):
    for i in range(chislo):
        print(".")
        sleep(1)

def sofa_blue_room():
    global letter
    global blue_room_knife
    if (letter == 0):
        slowprint("Я подошел к дивану, как и все в этой комнате он был синего цвета. Что я сейчас сделаю\n")
        if (blue_room_knife == 1):
            slowprint(">>>>>>> 1. Попробовать найти что-то между подушек \n>>>>>>> 2. Вскрыть подушки ножом \n>>>>>>> 3. Вернуться к осмотру комнаты\n")
            if(int(input()) == 1):
                slowprint("Я осмотрел внимательно диван, отодвинул подушки, но так ничего и не нашел.\n")
                slowprint("После этого я вернулся к осмотру комнаты.\n")
            elif(int(input()) == 2):
                slowprint("Я вскрыл подушки ножом, и среди кучи поролона обнаружил письмо, без адресов. Аккуратно распаковав конверт, я увидел аккуратно выведенную красивым почерком стихотворение следующего содержания:\n")
                slowprint("'Синее море шумело 7 дней\nУ зеленого монстра 9 очей\nКрасное пламя съело 10 домов\nВ желтом сарае было 8 голов'\n")
                slowprint("Я положил листок в карман, и вернулся к осмотрю комнаты\n")
                f = open('inventory', 'a')
                f.write("Письмо\n")
                f.close()
                letter = 1
            elif(int(input()) == 3):
                slowprint("Я вернулся к осмотру комнаты.\n")
        else:
            slowprint(">>>>>>> 1. Попробовать найти что-то между подушек \n>>>>>>> 2. Вернуться к осмотру комнаты\n")
            if(int(input()) == 1):
                slowprint("Я осмотрел внимательно диван, отодвинул подушки, но так ничего и не нашел.\n")
                slowprint("После этого я вернулся к осмотру комнаты.\n")
            elif(int(input()) == 2):
               slowprint("Я вернулся к осмотру комнаты.\n")
    else:
        slowprint("Мне показалось что я уже достаточно исследовал диван, поэтому я решил вернуться к осмотру комнаты\n")

def tumba_blue_room():
    global green_key
    global blue_room_key
    slowprint("Я подошел к тумбе синего цвета, как и все в этой комнате. Верхний ящик его был заперт на ключ, а в остальных ничего не было.\n")
    if (blue_room_key == 1):
        slowprint(">>>>>>> 1. Попробовать открыть ящик ключем.\n>>>>>>> 2. Вернуться к осмотру комнаты.\n")
        if(int(input()) == 1):
            slowprint("Замок легко поддался и я увидел содержимое ящика. В нем лежал шоколадный батончик, зеленый ключ, и банка энергетика. Увидев еду, мой организм вспомнил о чувстве голода, просигнализировав жутким урчанием моего желудка.\n")
            slowprint("Я решил что упакованную еду вряд ли так просто отравить, и что можно есть эту еду без опаски. Несмотря на рекламный слоган батончика, я довольно сильно затормозил, так как упаковка не поддавалась моим трясущимся рукам.\n")
            green_key = 1
            slowprint("Вконце концов мне удалось достать батончик из упаковки, я моментально его съел, и запил энергетиком. Подкрепившись, я положил мусор в ящик, и забрав из него ключ, пошел дальше обследовать комнату. \n")
            f = open('inventory', 'a')
            f.write("Зеленый ключ\n")
            f.close()
        if(int(input()) == 2):
            slowprint("Я вернулся к осмотру комнаты\n")
    elif (blue_room_key == 0):
        slowprint("Смотреть здесь было больше нечего, и я решил вернуться к осмотру комнаты.\n")

def lamp_blue_room():
    global blue_room_key
    slowprint("Я поднял голову и, прищурив глаза, из-за того что лампа светила довольно ярко, присмотрелся к люстре. Я обнаружил что из одного плафона не шел свет.\n")
    if(blue_room_key == 0):
        slowprint(">>>>>>> 1. Взять табуретку и посмотреть что лежит в том плафоне.\n>>>>>>> 2. Вернуться к осмотру комнаты.\n")
        if(int(input()) == 1):
            slowprint("Я взял табуретку из угла комнаты, подставил под люстру, и встал на нее. Я увидел что в плафоне, из которого не шел свет, действительно не было лампочки, но зато я достал их него ключ.\n")
            blue_room_key = 1
            f = open('inventory', 'a')
            f.write("Синий ключ\n")
            f.close()
            slowprint("После того как я взял ключ, я спустился, поставил табуретку на место, и вернулся к осмотру комнаты.\n")
    else:
        slowprint("Я уже осматривал люстру, так что лучше я вернусь к осмотру комнаты.\n")

def picture_blue_room():
    global blue_room_knife
    slowprint("Я подошел к картине на стене. На ней была изображена морская гладь, и терпящий кораблекрушение корабль. Снизу было надпись 'Айвазовский'. Картина подвешена при помощи веревочки на гвоздик\n")
    slowprint(">>>>>>> 1. посмотреть что находится сзади картины\n>>>>>>> 2. вернуться к осмотру комнаты\n")
    if(int(input()) == 1 and blue_room_knife == 0):
        slowprint("Когда я взялся за картину, чтобы снять её с гвоздика, откуда-то сзади выпал нож. \n")
        slowprint("Я поднял его, и начал осматривать картину, но её тыльная сторона, как и участок стены, который закрывала эта картина была совсем непримечательна. Я повесил картину обратно, и продолжил осмотр комнаты\n")
        blue_room_knife = 1
        f = open('inventory', 'a')
        f.write("Нож\n")
        f.close()
    elif(int(input()) == 1 and blue_room_knife == 1):
        slowprint("Сзади картины я ничего не увидел, и вернулся к осмотру комнаты\n")
    elif(int(input()) == 0):
        slowprint("Я вернулся к осмотру комнаты\n")

def no_red_button():
    slowprint("Оно уходит навсегда, и запирает за собой дверь. После нескольких минут, я встал, осмотрел комнату.")
    slowprint("Из комнаты было лишь два выхода: большая металлическая дверь, на которую я опирался, когда передо мной было Оно, и дверь, из которой Оно вышло, заперев меня.\n")
    slowprint("Больше в этой комнате ничего не было. Абсолютно. Я был наедине с воздухом этой комнаты. Я пытался открыть то одну дверь, то другую, но все было зря.\n")
    slowprint("Спустя несколько часов, заполненных беспомощными криками, стонами, возней, я вымотался окончательно. Я лег на холодный бетонный пол и заснул.\n")
    slowprint("Я проснулся с жуткой головной болью, и желудок порядочно журчал от отсутствия еды. Вздремнуть было единственное доступное мне решение.")
    slowprint("Дальше я продолжил свои бесполезные попытки попытаться выбраться из этой комнаты, докричаться до кого-нибудь. Но все это было бесполезно, и я опять заснул.")
    tochki(4)
    slowprint("Вновь проснулся, и заснул от бессилия")
    sleep(5)
    tochki(3)
    slowprint("Проснулся, и заснул.....")
    sleep(5)
    tochki(6)
    sleep(1)
    slowprint("Плохая концовка")
def yes_red_button():
    slowprint("Дверь на которую я опирался спиной открылась. От неожиданности я упал, и ударившись головой об пол, потерял сознание. Проснулся я уже полностью находясь в новой комнате. Я встал, отряхнулся, и окинул беглым взглядом комнату где я находился. \n")
    slowprint("'Она слишком синяя' - сказал я вслух. В этой комнате просто не было предметов не принадлежащих синему цвету, или его оттенку. \n")
    slowprint("Стены были в синих обоях с узором морской волны. На правой стене висела репродукция какой-то картины Айвазовского. Также в комнате был синий диван, рядом с которым стояла синяя тумбочка, и на потолке висела большая люстра. В углу стояла табуретка синего цвета\n")


def osmotr_blue_room():
    print("Что я сейчас хочу сделать?\n")
    print(">>>>>>> 1. Осмотреть картину\n>>>>>>> 2. Осмотреть диван \n>>>>>>> 3. Осмотреть тумбочку\n>>>>>>> 4. Осмотреть Люстру \n>>>>>>> 5. Открыть инвентарь\n")


f = open('inventory', 'w+')
f.write('Вы находитесь в синей комнате \n \nВаши предметы:\n')
f.close()

slowprint("Я очнулся где-то в незнакомом мне месте. Серые, бетонные стены. Глухая и всепоглощающая тишина.\n")
sleep(1.5)
slowprint("И тут входит оно, черное кружевное пальто, маска чумного доктора...\n")
sleep(1.5)
slowprint("Оно протягивает мне красную кнопку.\n")
sleep(2)
slowprint("Нажму ли я на неё?\n>>>>>>> 1.да\n>>>>>>> 2.нет\n")
a = int(input())
if (a == 2):
    sleep(1)
    no_red_button()
elif (a == 1):
    sleep(1)
    yes_red_button()
    while (green_key != 1 or letter != 1):
        osmotr_blue_room()
        b = ""
        while( b == ""):
            b = input()
        if (b == '1'):
            picture_blue_room()
        elif (b == '2'):
                sofa_blue_room()
        elif (b =='3'):
            tumba_blue_room()
        elif (b == '4'):
            lamp_blue_room()
        elif (b == '5'):
            inventory()

    exit_blue_room()
    blue_room_safe = 1;





