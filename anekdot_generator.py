from random import choice
import time
import sys

subjects = ['учёный', 'больной', 'пикачу', 'кот', 'никто', 'Штирлиц', 'Рабинович', 
            'террорист', 'сантехник', 'динозавр', 'мама', 'менеджер', 'кошка', 'Эйнштейн'
            'учительница', 'мама Вовочки', 'бульбазавр', 'доктор', 'начальник']
places = ['в офис', 'в небытие', 'в больницу', 'драться', 'в лабораторию', 'на вызов', 
          'в парк юрского периода', 'на родительское собрание', 'к кошке', 'в метро']
phrases = ['я совершил открытие!', 'пика-пика!', 'мысленно:\n- привет, ничто', 
           'у меня болит голова', 'давай заведём котят', 'я мама Вовочки', 
           'я увольняюсь', 'аллах акбар', 'возьмите меня есть туристов', 
           'какой серьёзный засор', 'шалом']
responders = ['кошка', 'учительница', 'небытие ему в ответ', 'доктор ему', 'тут по громкоговорителю', 
              'учёное сообщество', 'в ответ слышит', 'из трубы голос', 'начальник ему', 'бульбазавр на это',
              'Штирлиц', 'Рабинович', 'больной', 'еврей', 'кот']
response_phrases = ['ты не пикачу, ты сантехник', 'я не доктор, я динозавр', 'давай лучше мышат', 
                    'привет, ничтожество', 'следущая станция бесконечная', 'вы не мама, вы папа', 
                    'нам такие не нужны', 'ты же на пенсию вышел', 'ты новый Эйнштейн', 
                    'ну хочешь шутку расскажу', 'и вам не хворать']
end = ['энтропия нарастала', 'и уехали в Казахстан', 'динлзавр всё равно съел туристов', 
       'держите зачётку', 'и все стали танцевать', 'вот и сказочке конец', 'так появилась вселенная', 
       'с тех пор это закон', 'и немедленно выпил', '))))']


# медленный вывод текста
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)


# выбор вариантов частей анекдота
def ask_variant(variants):
    for variant in variants:
        print("{i}", variant)
    while True:
        selected_item = input("ваш выбор?\n")
        if selected_item not in variants:
            slowprint("подумайте ещё раз")
            continue
        if selected_item == 0..len(variants):
            selected_item = variants[selected_item]
            break
        break
    slowprint("вы выбрали:")
    print(selected_item)
    return selected_item


# конструктор анекдотов
def constructor():
    slowprint("выберите главного героя анекдота\n")
    subj_var = ask_variant(subjects)
    slowprint("выберите куда придёт главный герой\n")
    places_var = ask_variant(places)
    slowprint("выберите фразу главного героя\n")
    phrases_var = ask_variant(phrases)
    slowprint("выберите того, кто отвечает\n")
    respond_var = ask_variant(responders)
    slowprint("выберите ответ\n")
    resp_phrase_var = ask_variant(response_phrases)
    slowprint("выберите конец\n")
    end_var = ask_variant(end)
    print("ваш анекдот:")
    slowprint(f'''{subj_var} приходит {places_var} и говорит:\n- {phrases_var}'''
              f'''\nа {respond_var} отвечает:\n- {resp_phrase_var}. \n{end_var}''')


# основной режим
def standart():
    slowprint(f'''{choice(subjects)} приходит {choice(places)} и говорит:\n- {choice(phrases)}\n''' 
          f'''а {choice(responders)} отвечает:\n- {choice(response_phrases)}. \n{choice(end)}''')


# основной цикл
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
