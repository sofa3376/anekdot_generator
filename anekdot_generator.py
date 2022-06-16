from random import choice
import time
import sys

kto = ['учёный', 'больной', 'пикачу', 'кот', 'никто', 
       'террорист', 'сантехник', 'динозавр', 'мама', 'менеджер']
prihodit = ['в офис', 'в небытие', 'в больницу', 'драться', 'в лабораторию', 'на вызов', 
            'в парк юрского периода', 'на родительское собрание', 'к кошке', 'в метро']
i_govorit = ['я совершил открытие!', 'пика-пика!', 'мысленно:\n- привет, ничто', 
             '\n- у меня болит голова', '\n- давай заведём котят', '\n-я мама Вовочки', 
             '\n- я увольняюсь', '\n- аллах акбар', '\n- возьмите меня есть туристов', 
             '\n- какой серьёзный засор']
A = ['кошка', 'учительница', 'небытие ему в ответ', 'доктор ему', 'тут по громкоговорителю', 
     'учёное сообщество', 'в ответ слышит', 'из трубы голос', 'начальник ему', 'бульбазавр на это']
otvechaet = ['ты не пикачу, ты сантехник', 'я не доктор, я динозавр', 'давай лучше мышат', 
             'привет, ничтожество', 'следущая станция бесконечная', 'вы не мама, вы папа', 
             'нам такие не нужны', 'ты же на пенсию вышел', 'ты новый Эйнштейн', 
             'ну хочешь шутку расскажу']
konets = ['энтропия нарастала', 'и уехали в Казахстан', 'динлзавр всё равно съел туристов', 
          'держите зачётку', 'и все стали танцевать', 'вот и сказочке конец', 'так появилась вселенная', 
          'с тех пор это закон', 'и немедленно выпил', '))))']


#  медленный вывод текста
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)

#  конструктор анекдотов
def constructor():
    slowprint("выберите главного героя анекдота\n")
    for i in range(10):
        print(kto[i])
    a = int(input("ваш выбор?\n"))
    for i in range(10):
        if a == i:
            a = kto[i]
            slowprint("вы выбрали", a)
            break
        elif a > 10:
            slowprint("подумайте ещё раз")
            break
        else:
            continue
    slowprint("выберите куда придёт главный герой\n")
    for i in range(10):
        print(prihodit[i])
    b = int(input("ваш выбор?\n"))
    for i in range(10):
        if b == i:
            b = prihodit[i]
            slowprint("вы выбрали", b)
            break
        elif b > 10:
            slowprint("подумайте ещё раз")
            break
        else:
            continue
    slowprint("выберите фразу главного героя\n")
    for i in range(10):
        print(i_govorit[i])
    c = int(input("ваш выбор?\n"))
    for i in range(10):
        if c == i:
            c = kto[i]
            slowprint("вы выбрали", c)
            break
        elif c > 10:
            slowprint("подумайте ещё раз")
            break
        else:
            continue
    slowprint("выберите того, кто отвечает\n")
    for i in range(10):
        print(A[i])
    d = int(input("ваш выбор?\n"))
    for i in range(10):
        if d == i:
            d = A[i]
            slowprint("вы выбрали", d)
            break
        elif d > 10:
            slowprint("подумайте ещё раз")
            break
        else:
            continue
    slowprint("выберите ответ\n")
    for i in range(10):
        print(otvechaet[i])
    e = int(input("ваш выбор?\n"))
    for i in range(10):
        if e == i:
            e = otvechaet[i]
            slowprint("вы выбрали", e)
            break
        elif e > 10:
            slowprint("подумайте ещё раз")
            break
        else:
            continue
    slowprint("выберите конец\n")
    for i in range(10):
        print(konets[i])
    f = int(input("ваш выбор?\n"))
    for i in range(10):
        if f == i:
            f = konets[i]
            slowprint("вы выбрали", f)
            break
        elif f > 10:
            slowprint("подумайте ещё раз")
            break
        else:
            continue
    print("ваш анекдот:")
    slowprint(f'''{a} приходит {b} и говорит:\n- {c}\nа {d} отвечает:\n- {e}. \n{f}''')


#  основной режим
def standart():
    slowprint(f'''{choice(kto)} приходит {choice(prihodit)} и говорит:\n- {choice(i_govorit)}\n''' 
          f'''а {choice(A)} отвечает:\n- {choice(otvechaet)}. \n{choice(konets)}''')


#  основной цикл
def main():
    while True:
        slowprint("что вы хотите сделать?")
        print("1. сгенерировать анекдот\n"
              "2. составить анекдот\n"
              "3. выйти")
        n = int(input())
        if n == 1:
            standart()
        elif n == 2:
            constructor()
        elif n == 3:
            slowprint("goodye")
            break
        else:
            slowprint("подумайте ещё раз")



if __name__ == '__main__':
    main()
