import paintings
import winsound
import threading
import time
import random


d=1
e=1
g=1
v=1
t=1
z=1
u=1
w=1
l=1
c1=1
r1=1
o1=1
a2=1
e1=1
l1=1
f2=1
k2=1
w3=1



def play_music():
    winsound.PlaySound('music.wav', winsound.SND_FILENAME)
    

    
def play_music_2():
    winsound.PlaySound('music_2.wav', winsound.SND_FILENAME)


    
def play_music_3():
    winsound.PlaySound('music_3.wav', winsound.SND_FILENAME)
    

    
def music():
    global f2
    if f2==1:
        music_thread = threading.Thread(target=play_music)
        music_thread.start()
        f2=2
        time_()
    elif f2==2:
        music_thread_2 = threading.Thread(target=play_music_2)
        music_thread_2.start()
        f2=3
    elif f2==3:
        music_thread_3 = threading.Thread(target=play_music_3)
        music_thread_3.start()
        f2=1



       
def time_():
    music()
    time.sleep(300)
    music()
    time.sleep(249)
    music()
    time.sleep(254)
    time_()
    
    
    
def moy_print(text):
    input()
    print(text)


    
def end():
    print('Я выбрался!')
    moy_print('Спускаюсь по пожарной лестнице в какие-то задворки')
    time.sleep(3)
    moy_print('Через подворотню есть выход на улицу')
    moy_print('Выйду, посмотрю, может найду кого-нибудь или хотя бы адрес узнаю')
    moy_print('Стоп, знакомое место...')
    moy_print('Это... Это моя улица... Соседний дом...')
    moy_print('Кто же меня запер?')
    moy_print('Хотя, это пока не важно...')
    moy_print('Боже, как я устал')
    moy_print('Пойду отсплюсь...')
    paintings.ending()
        

    
def exit_():
    global a2
    if a2==1:
      print('Вот и выход! Скорее на свободу!')
      a2=2
    elif a2==2:
      print('Пора уходить')
    print('''Свалить отсюда (1)
Пока остаться (2)''')
    b2=input()
    if b2=='1':
        end()
    elif b2=='2':
        moy_print('Что мне еще здесь нужно?!')
        hole_2()
    else:
        moy_print('Мне выходить или нет?')
        exit_()
    
        
    
def room4():
    global w
    a1=random.randint(1,2)
    if w==1:
        print('Здесь вроде никого нет')
        moy_print('Надо поскорее найти ключ и выбираться отсюда')
        moy_print('Посмотрим что у нас тут')
        time.sleep(3)
        moy_print('Здесь ничего!')
        moy_print('Только холодильник и ковер!')
        moy_print('Хотя, есть одна идейка')
        w=2
    else:
        if a1==1:
            print('Похоже здесь недавно кто-то был')
            moy_print('Не время оставаться в этих комнатах еще хоть немного')
        elif a1==2:
            print('Мрачноватое место')
            moy_print('Не могу представить чтобы человеку захотелось быть здесь')
        else:
            print('Интересно, этот холодильнтк времен Гражданской войны?')
            moy_print('А тогда были холодильники?')
    room4_2()


    
def room4_2():
    global b1, e1, c1, k2, r1
    if k2==1:
       paintings.fridge_carpet()
       k2=2
    print('''Приподнять ковер (1)
Открыть холодильник (2)
Выйти в коридор (3)''')
    b1=input()
    if b1=='1':
        if e1==1:
             e1=2
             print('Я так и думал!')
             moy_print('Здесь люк! Но он закрыт...')
             moy_print('Доски довольно хлипкие, но руками их не отодрать')
             moy_print('У меня же есть топор! Знал, что он мне пригодится')
             time.sleep(3)
             moy_print('Давай! Ну же! Есть! Я победил деревянный люк...')
             moy_print('Здесь деревянная коробка (в этом доме все деревянное?)')
             moy_print('Она открыта! (не может быть) Посмотрим...')
             moy_print('Здесь бумажка! А на ней... Код! В одной из комнат был сейф, скорее всего он от него')
             moy_print('Код-1870, надо бы запомнить')
             c1=2
             r1=2
        else:
             print('Здесь больше ничего нет')
             moy_print('Думаю код и так ценный приз')
        room4_2()
    elif b1=='2':
        fridge()
    elif b1=='3':
        hole()
    else:
        print('Я не знаю что мне делать')
        room4_2()


        
def fridge():
    global o1
    if o1==1:
        print('О Господи! Зачем ему это?')
        moy_print('Весь холодильник уставлен банками')
        paintings.jars()
        moy_print('Я сначала подумал, что это варенье...')
        moy_print('Это банки с чьими то органами')
        moy_print('Может здесь и внутренности того мужчины, который написал записку...')
        moy_print('Может скоро и мои будут здесь...')
        moy_print('Нет! Надо поскорее выбираться')
        o1=2
    else:
        moy_print('Я уже видел эту гадость')
        moy_print('Не хочу лишний раз туда заглядывать')
    room4_2()
    
   
        
def hole_2():
    print('''Подняться обратно (1)
Подойти к двери выхода (2)
Пойти в боковую дверь (3)''')
    h2=input()
    if h2=='1':
        room1_5()
    elif h2=='2':
        if r1==2 or r1==3:
           exit_()
        else:
           print('Закрыто, надо бы найти ключ')
           hole_2()
    elif h2=='3':
        room4()
    else:
        moy_print('Ну и куда мне идти?')
        hole_2()

        
        
def hole():
    global l
    j=random.randint(1,3)
    if l==1:
        print('Темно...')
        moy_print('С трудом можно видеть на 5 метров вперед')
        moy_print('Надо было искать фонарик помощнее')
        moy_print('Этим фонарем наверное пользовались еще во время Второй Мировой')
        moy_print('Ладно, будем пользоваться тем что есь')
        moy_print('Здесь должно быть хоть что-нибудь!')
        moy_print('Вон! Там какая-то зеленая надпись!')
        moy_print('Это EXIT!')
        paintings.exit_door()       
        moy_print('Закрыто!!! Нужен ключ')
        moy_print('Пока я шел, видел какую-то дверь в стене, можно вернуться и проверить')
        l=2
    else:
        if j==1:
          print('Опять этот коридор, все время кажется что кто-то выпрыгнет из-за угла')
          moy_print('Тут нет углов, хех')
        elif j==2:
          print('Темно, не нравится мне это')
        else:
          print('Поскорей бы выбраться')
    hole_2()


    
def safe():
    global r1
    if r1==2:
        print('Код надеюсь подойдет')    
    elif r1==1:
        print('Можно попробовать угадать пароль')
    else:
        print('В сейфе больше ничего нет')
        choice()
    moy_print('Введите пароль:')
    d1=input()
    if d1=='1870':
        moy_print('Он открылся! Надеюсь здесь что-нибудь полезное')
        moy_print('ЗДЕСЬ КЛЮЧ!!! Если он подойдет к двери выхода, то я считай что выбрался отсюда!')
        r1=3
        choice()
    else:
        moy_print('Пароль не подходит')
        safe()


       
def room1_2():
    global u, z
    if u==1:
      print('Тут жуткий труп на полу')
      moy_print('Наверное он давно тут лежит')
      paintings.men()
      moy_print('Если не закрывать нос, то больше двух минут тут не продержишься')
      moy_print('Похоже его зарубили топором...')
      moy_print('Вот кстати и топор')
      moy_print('Возьму его')
      moy_print('Оружие однозначно пригодиться')
      moy_print('Что тут у нас еще? Труп это конечно интересно, но пора выбираться отсюда')
      moy_print('Какая-то дыра в полу... И... Записка!!!')
      moy_print('''\" Я сижу тут уже два дня. Из под пола постоянно идут какие-то звуки. Здесь дыра в полу. Вчера ночью, когда не мог заснуть, показалось что кто-то смотрит оттуда на меня.
Ни за что не собираюсь туда спускаться! Я же погибну! Стоп! Надо успокоиться. Долго я здесь не протяну... Подожду кого-нибудь... Надо рассказать о том что уже обнаружил.
Еды здесь нет, точно. Чувствую себя ужасно. Вчера казалось что кто-то зовет меня снизу по имени. Если... Ты... Нуу... Найдешь письмо а меня, нет... В Волгограде, на улице Революции д.8
к.79. Напишите туда что со мной случилось... \"''')
      moy_print('Значит кто-то есть здесь')
      moy_print('И похоже он живет под полом')
      moy_print('Этого убили, да еще и покромсали')
      moy_print('Интересно, когда очередь дойдет до меня?')
      moy_print('Как же не хочется спускаться')
      u=2
    else:
        moy_print('Ужасное место. Не хочу здесь долго оставаться...')
    room1_3()

    
    
def room1_3():
    global l
    print('''Спуститься вниз (1)
Вернуться в коридор (2)''')
    c2=input()
    if c2=='1':
           hole()
    elif c2=='2':
           room3()
    else:
        moy_print('Не могу я туда пойти!')
        room1_3()

        
    
def room3():
    global d, z
    if d==1:
        print('Уффф...')
        moy_print('Как болит голова...')
        moy_print('Просто раскалывается')
        moy_print('У меня шишка на затылке, где я так ударился?')
        moy_print('Ксати где я?)))')
        moy_print('Это какой-то коридор')
        moy_print('Здесь достаточно сыро и прохладно')
        moy_print('Как я здесь оказался, вряд ли сам сюда зашел')
        moy_print('Помню только, как вышел в магазин за хлебом и... Вроде все')
        moy_print('Ладно, потом повспоминаю, пора  возвращаться домой')
        moy_print('Сейчас огляжусь и найду выход')
        moy_print('Тут две двери')
        d=2
    elif z==2:
        print('Фуух... Ужас какой')
        moy_print('Но мне придется туда вернуться')
        moy_print('Если здесь и есть выход то он там')
        z=3
    else:
        print('Ну вот я и снова в коридоре...')
    room3_2()


    
def room3_2():
    print('''Пойти в первую комнату (1)
Пойти во вторую комнату (2)''')
    a=input()
    if a=='1':
        if z==3:
            room1_2()
        else:
            room1()
    elif a=='2':
        room2()
    else:
        moy_print('Здесь только две двери!')
        room3_2()


        
def room1():
        global g, t, z
        if v==1:
           g=2
           print('Темно... Выключатель сломан, надо найти чем посветить')
           room1_4()
        elif z==2:
            room1_2()
        else:
            print('Наконец-то свет, теперь можно хоть что-то найти')
            moy_print('О @#*$#!')
            time.sleep(2)
            moy_print('Лучше бы я не находил фонарь')
            moy_print('Не могу сдесь больше находится')
            z=2
            room3()


            
def room1_4():
           print('Вернуться обратно (1)')
           b=input()
           if b=='1':
               room3()
           else:
               moy_print('Не видно ничего, надо найти что-нибудь что светит')
               room1_4()
            
                
                
def room2():
    global e
    if e==1:
       print('Здесь только тумбочка и сейф на ней... Вроде все')
       paintings.cupboard()
       e=2
    choice()

    
    
def choice():
    print('''Пошарить в тумбочке (1)
Открыть сейф (2)
Вернуться в коридор (3)''')
    c=input()
    if c=='3':
        room3()
    elif c=='2':
        safe()
        room2()
    elif c=='1':
        global v
        if v==1:
             print('Так что у нас тут?')
             v=2
             if g==1: 
                moy_print('О! Фонарик! Возможно пригодится...')
             else:
                moy_print('Фонарик! Возможно в первой комнате я смогу что-нибудь насветить!')
        else:
            print('Пусто... Никаких тайников...')
        room2()
    else:
        print('Я пока не могу сделать ничего другого')
        choice()

        

def room1_5():
    moy_print('Ужасное место. Не хочу здесь долго оставаться...')
    room1_3()


    
time_thread = threading.Thread(target=time_)
time_thread.start()

print('                                                                                ПРЕДПОЛОЖИТЕЛЬНО МОСКВА')

paintings.year()
                     
room3()








