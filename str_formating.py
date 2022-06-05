# Строки и форматирование
# Последовательность букв

# Список
"""
from hashlib import new
from signal import pthread_kill


friends = ['Сергей', 'Maks', 'Rusy', 'Sony', 'Alina']

print(friends[1])"""

# Метод split() разбирает строку по фрагментам
"""
milk_str = 'молоковоз'

new_milk = milk_str.split('о')

print(new_milk)"""

"""poem_str = 'Дама сдавала багаж'

words_list = poem_str.split(' ')

print(words_list)"""

# метод join 

"""words_list = ['раз', 'два', 'три', 'четыре', 'пять', 'вышел', 'зайчик', 'погулять']
# Метод join() "склеивает" элементы списка,
# создавая строку, в которой 
# элементы исходного списка разделены текстовым символом;
# для разделения применим дефис:
new_string = ' '.join(words_list)

print(new_string)"""

# Задача 1
"""quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    word_list = message.split()
    return word_list[-3]

# Вызовы функции готовы к работе, не изменяйте их!

# Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
print(penult_word(quote_1))

# То же, но с аргументом quote_2.
print(penult_word(quote_2))

# То же с аргументом quote_3.
print(penult_word(quote_3))"""


#
"""message = 'У меня опять всё сломалось и не работает соединение с интернетом!!11'

# Разбиваем сообщение по пробелам на слова
words = message.split()
# Проверяем, есть ли ключевые слова в письме
if 'стоимость' in words:
    print('Переслать письмо в отдел биллинга')
elif 'сломалось' in words:
    print('Переслать письмо в техподдержку')
else:
    print('Содержание письма не определено, придётся прочесть самостоятельно') """

# Задача 2
"""def check_query(query):
# Допишите код тела функции
    elements = query.split(', ')
    if 'Анфиса' in elements:
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'



# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

# Напечатаем результат.
# Переберём список вопросов в цикле
for q in queries:
    # Каждый из вопросов передадим аргументом
    # в функцию check_query()
    result = check_query(q)
    # И для каждого вызова напечатаем вопрос и, через дефис - вердикт программы
    print(q, '-', result)"""


# Задача 3
"""def check_query(query):
    elements  = query.split(', ')
    # Напишите код функции
    return elements[1]

# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '—', result)"""

# Задача 4

"""DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        # Из словаря DATABASE создайте строку с помощью join();
        # имена друзей разделите запятой и пробелом.
        # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
        friends_string = ', '.join(DATABASE)

        # Этот цикл больше не понадобится, удалите его
        
        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        # Из сета unique_cities создайте строку с помощью join();
        # названия городов разделите запятой и пробелом.
        # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
        cities_string = ', '.join(unique_cities)

        # Этот цикл больше не понадобится, удалите его
         

        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))"""

# f-строки: переменные прямо в тексте
"""
weather = 'облачно'
print(f'На улице сейчас {weather}.')"""

#
"""one_hundred = 100
rubles = 'рублей'
friends = 'друзей'
print(f'Не имей {one_hundred} {rubles}, а имей {one_hundred} {friends}.')

# А без применения f-строк тот же код выглядит похуже:
print('Не имей ' + str(one_hundred) + ' ' + rubles + ', а имей ' + str(one_hundred) +' ' + friends + '.')"""

#
"""for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count <= 4:
        print(f'У вас {messages_count} новых сообщения')
    else:
        print(f'У вас {messages_count} новых сообщений')"""

# 
"""def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    return f'Вы прослушали {len(listened)} песен.'
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))"""

#
"""def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    summ = 0
    for i in range (len(listened)):
        summ += int(listened[i])
    return f'Вы прослушали {len(listened)} песен общей продолжительностью {summ//60} минут.'
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))"""

# Задача 1
"""DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья" 
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        f'У тебя {format_friends_count(count)}.'
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение, 
        # которое вернёт функция format_friends_count()
        return f'У тебя {count} друзей.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('сколько у меня друзей?'))
print(process_anfisa('кто все мои друзья?'))
print(process_anfisa('где все мои друзья?'))
print(process_anfisa('кто виноват?'))"""

