#bunny_counter = ''

#for i in range(1, 6):
#    bunny_counter = bunny_counter + str(i) + ','
#print(bunny_counter + " Вышел зайчик погулять! ")


#countdown_str = ''

#for i in reversed(range(0, 11)):
#    countdown_str = countdown_str + str(i) + ', '
#countdown_str = countdown_str + 'поехали!'
#print(countdown_str)


#for message_cont in range(6):
#    if message_cont > 0:
#        print("Новых сообщений", message_cont)
#    else:
#        print("у вас нет сообщений")

#for current_hour in range(24):
#    if current_hour < 12:
#        print("Доброе утро")
#    else:
#        print("Добрый день")

#for message_cont in range(0, 21):
#    if message_cont == 0:
#        print("У вас нет новых сообщений!")
#    elif message_cont == 1:
#        print("У вас", message_cont, "новых сообщений!")
#    elif message_cont <= 4:
#        print("У вас", message_cont, "новых сообщений!")
#    else:
#        print("У вас", message_cont, "новых сообщений" )


#for current_hour in range(0, 24):
    #print("На часах", str(current_hour) + ":00.")

    #if current_hour < 6:
        #print("Доброй ночи!")
    #elif current_hour < 12:
       # print("Доброе утро!")
    #elif current_hour < 18:
        #print("Доброй день!")
    #elif current_hour < 23:
        #print("Добрый вечер!")
    #else:
    #    print("Доброй ночи!")

#for current_hour in range(0, 24):
    #print("На часах", str(current_hour) + ":00.")

    #if current_hour >= 6 and current_hour <= 11:
        #print("Доброе утро!")
    #elif current_hour >= 12 and current_hour <= 17:
        #print("Добрый день!")
    #elif current_hour >= 18 and current_hour <= 22:
        #print("Добрый вечер!")
    #elif current_hour <= 5 and current_hour >= 23:
        #print("Доброй ночи!")

# and если оба услуовие истино то true
# or если хотябы одно условие истино то true
# оператор not превращает значение в противоположное print(not True) будет False
# Высший приоретет not, затем выполняется and, а последним or

"""for message_cont in range(0, 21):
    if message_cont == 0:
        print("У вас нет новых сообщений!")
    elif message_cont == 1:
        print("У вас", message_cont, "новое сообщение!")
    elif message_cont == 2 or message_cont <= 4:
        print("У вас", message_cont, "новых сообщения!")
    elif message_cont >= 11 or message_cont <= 15:
        print("У вас", message_cont, "новых сообщений!")
    else:
        print("У вас", message_cont, "новых сообщений!")
        """
    
"""good_boy = True

if not good_boy:
    print('1')
else:
    print('2')"""

"""milk = not True
cereals = True
eggs = False

if milk and cereals or eggs:
    if eggs:
        if milk:
            breakfast = "- омлет"
    else:
        breakfast = "- Хлопья с молоком"
else:
    if milk:
       breakfast = "- Стакан молока" 
    elif cereals:
        breakfast = "- можно погрызть сухих хлопьев" 
    else:
       breakfast =  "Ничего не будет: разрузочный день"
print("Сегодня на завтрак", breakfast)"""

"""
def hello(name, bonus):
    print(name + ", приветствую тебя! ", "бери", bonus )

hello('Дарт Вейдер', 'печеньки')

hello('Винни Пух', 'мёд')

hello('Макс', "что то вкусное!")"""

"""def say_hello(current_hour):

    if current_hour >= 6 and current_hour <= 11:
        print("Доброе утро!")
    elif current_hour >= 12 and current_hour <= 17:
        print("Добрый день!")
    elif current_hour >= 18 and current_hour <= 22:
        print("Добрый вечер!")
    elif current_hour <= 5 or current_hour >= 23:
        print("Доброй ночи!")

say_hello(4)
say_hello(10)
say_hello(15)
say_hello(20)
"""
"""
def print_friends_count(friends_count):
    if friends_count == 0:
        print("У тебя нет друзей")
    elif friends_count == 1:
        print("У тебя", friends_count, "друг")
    elif friends_count >= 2 and friends_count <= 4:
        print("У тебя", friends_count, "друзей")
    elif friends_count >= 5 and friends_count <= 20:
        print("У тебя", friends_count, "друзей")
    else:
        print("Ого сколько у тебя друзей! Целых", friends_count)

#print_friends_count(21)

for friends_count in range(0, 21):
    print_friends_count(friends_count)"""

"""
def print_home(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

print_home('Дроид-убийца')
"""
"""
def print_home(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

print_home(planet='Земля')


print_home(planet='Земля', name='Марк Уотни ')"""

# len() количество элементов в списке
"""
flat = [
    5.55, 22.19, 7.88, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

room_size = 22.19
count = 0

for room in flat:
    if room == room_size:
        count += 1
#rooms_num = len(flat)

print('Комната площадью ', room_size, 'кв.м', count)
"""
"""flat = [
    5.55, 22.19, 7.88, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

sum_area = 0

for room in flat:
    sum_area += room

print("Общая площадь", sum_area)"""

"""
years = [
    1981, 1982, 1983, 1984, 1986, 1987, 1990,
    1993, 1997, 2001, 2005, 2009, 2013, 2017
]

count = 0

for year in years:
    if year > 2000:
        count += 1

print('Выпущено альбомов в ХХI ', count)"""

"""def rooms_equal(room_size, room_list):
    count = 0

    for room in room_list:
        if room == room_size:
            count += 1
    print("Комната площадью", room_size, "кв.м", count)


flat = [
    5.55, 22.19, 7.88, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]


rooms_equal(5.55, flat)

rooms_equal(9.2, hut)"""

"""may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]


def comfort_count(temperatures):
    
    count = 0

    for temp in temperatures:
        if temp >= 22 and temp <= 26:
            count += 1
    print("Количество тёплых дней в этом месяце", count)

comfort_count(may_2017)
comfort_count(may_2018)"""



"""
def calc_square(side_a, side_b):
    result = side_a * side_b

    return result

rectangle_area = calc_square(16, 9)
print(rectangle_area)"""

"""
may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]


def comfort_count(temperatures):
    
    count = 0

    for temp in temperatures:
        if temp >= 22 and temp <= 26:
            count += 1
    return  count

nice_days = comfort_count(may_2017)

print("Количество тёплых дней в этом месяце ", nice_days)"""

"""def calc_cube_perimeter(side):
    return side * 12

one_cube_perimeter = calc_cube_perimeter(3)

full_lenght = one_cube_perimeter * 8

print("Необходимый метраж палок для 8 кубов ", full_lenght)"""



"""def calc_cube_area(side):
    one_face = side * side

    cube_area = one_face * 6

    return cube_area

one_cube_area = calc_cube_area(3)

full_area = one_cube_area * 8

print("Необходимая площадь стекла для 8 кубов, кв.м  ", full_area)"""



"""# Функция для вычеслений периметра куба
def calc_cube_perimeter(side):
    return side * 12

# Функция для вычесления площади куба
def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area

# Оснавная функция, которая принимает длину ребра

def calc_cube(side):
    # Вызываем функцию расчитываем периметр
    # и пеоедаём в неё нужный размер

    one_cube_perimeter = calc_cube_perimeter(side)
    full_lenght = one_cube_perimeter * 8

    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * 8

    print("Для 8 кубов понадобится палок  (м): ", full_lenght, "и стекла (кв.м): ", full_area )

calc_cube(3)"""


"""def calc_cube_perimeter(side):
    return side * 12

def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area

def calc_cube(side, amount):
    one_cube_perimeter = calc_cube_perimeter(side)

    full_lenght = one_cube_perimeter * amount

    one_cube_area = calc_cube_area(side)

    full_area = one_cube_area * amount

    print('Для', amount, 'кубов понадобится палок (м): ', full_lenght, 'и стекла (кв.м): ', full_area)

calc_cube(3, 2)"""
"""
concert_song = {
    'Ничего на свете лучше нету',
    'Мы к вам заехали на час',
    'Рок колыбельная',
    'Луч Солнца Золотого',
    'Ничего на свете лучше нету',
    'Куда ты, тропинка, меня завела',
    'А как известно, мы народ горячий',
}
print(type(concert_song))   
print(concert_song)
"""
"""
bermen_musicians = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух']

for i in bermen_musicians:
    print(i)"""

"""favorite_song = {
    'Тополиный пух': 'Иванушки intenational',
    'Город золотой': 'Аквариум',
    'Звезда по имени солнце': 'Кино',
    'Spacy Oddity': 'David Bowie',
    'Рыба': 'Аквариум',
    'Серенада Трубадура': 'Муслим Магомаев',
}

for song, perfomer in favorite_song.items(): # items метод перебора ключей и значений 
    print(' Песню ' + song + ' исполняет ' + perfomer)"""

"""favorite_song = {
    'Тополиный пух': 'Иванушки intenational',
    'Город золотой': 'Аквариум',
    'Звезда по имени солнце': 'Кино',
    'Spacy Oddity': 'David Bowie',
    'Рыба': 'Аквариум',
    'Серенада Трубадура': 'Муслим Магомаев',
    }
for singer in favorite_song.values(): # values медот значение элемента
    print('Доктор, я больше не могу слушать исполнителя ' + singer) 
for music in favorite_song.keys(): # keys метод ключ элемента , по умолчанию python для итерации по словарю использует ключи. Поэтому можно использовать без keys()
    print('Доктор, я каждый день слушаю песни', music)"""




"""friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

friends = {}

for i in range(len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]


print("Лена живёт в городе", friends['Лена'])"""


"""favorite_song = {
    'Серёга': ['Un', 'Holl', 'High'],
    'Соня': ['Sh', 'The', 'Let'],
    'Дима': ['!', '@', '$']
}

print(len(favorite_song['Дима']))

for i in favorite_song['Соня']:
    print(i)"""




"""
# Операции с коллекциями 

# Список (List): в квадратных скобках
sleep_list = [
    'спать',
    'дрыхнуть',
    'кемарить',
    'спать'
]


# Множества set в фигурных скобках, выглядят как в списке. 
# Но не могут повторяться.   
sleep_set = {
    'дрыхнуть',
    'Спать',
    'Кемарить'
}

# Словарь (dict): в фигурных скобках, элементы выглядят как ключс:значение;
# ключи не могут повторяться
sleep_dict = {
    'Спать': 'дрыхнуть',
    'Почивать': 'кемарить'
}


# Есть ли элемент 'дрыхнуть' в списке sleep_list

if 'дрыхнуть' in sleep_list:
    print('В списке нашлось!')
else:
    print('В списке не нашлось')

# Есть ли элемент 'дрыхнуть' в сете sleep_set

if 'дрыхнуть' in sleep_set:
    print('В списке нашлось!')
else:
    print('В списке не нашлось')

# Есть ли элемент 'дрыхнуть' в словаре sleep_dict
if 'дрыхнуть' in sleep_dict:
    print('В списке нашлось!')
else:
    print('В списке не нашлось')
"""





"""

sleep_list = [
    'спать',
    'дрыхнуть',
    'кемарить',
    'спать'
]

# Метод append добавит посыпывать в конце списка
sleep_list.append('посыпывать')
print(sleep_list)"""

"""
play_list = {
    '1',
    '2',
    '3',
    '4',
    '5',
}

play_list2 = [
    '6',
    '7',
    '8',
    '9',
    '10',
]

for music in play_list2:
    play_list.add(music)


print(play_list)"""

"""

DATABASE = {
'Серёга': 'Омск',
'Соня': 'Москва',
'Миша': 'Москва',
'Дима': 'Челябинск',
'Алина': 'Красноярск',
'Егор': 'Пермь',
'Коля': 'Красноярск'
}

"""
l1 = [1, 99, 1, 21, 35, 176]

res = 0
for i in l1:
    res += i

print(res)
