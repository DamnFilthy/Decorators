import datetime
from typing import Callable
import os
import json
from collections import Counter


# Декоратор с параметрами
def path_logger(str_path, file_name):
    def logger(old_finction: Callable):
        def new_function(*args, **kwargs):
            complete_name = os.path.join(str_path + '\\' + file_name + ".txt")
            now = datetime.datetime.now()

            with open(complete_name, 'a+', encoding='UTF-8') as f:
                func_name = f'\nВызвана функция {old_finction.__name__}\n'
                f.write(func_name)

                func_time = f'Время вызова: {now} \n'
                f.write(func_time)

                func_args = f'С аргументами {args, kwargs} \n'
                f.write(func_args)

                result = old_finction(*args, **kwargs)
                f.write(f'результат {result} \n')

            return result

        return new_function

    return logger


@path_logger('C:\\Users\\User\\Desktop\\logs', 'my_logs')
def text_func(a, b):
    return a + ' ' + b + '!'


text_func('Hello', 'World')


# Функция из прошлых уроков, применяем декоратор
@path_logger('C:\\Users\\User\\Desktop\\logs', 'country_logs')
def get_json_top(filename, char, rating):
    # Reading
    with open(filename, encoding='utf-8') as f:
        file = json.load(f)
        # Empty string
        all_words = ''
        titles = file["rss"]["channel"]["items"]
        # One big string
        for title in titles:
            all_words = all_words + ' ' + title["description"]

    # List of words
    lst = all_words.split()

    # List where word bigger than 6 char
    total_lst = []
    for word in lst:
        if len(word) >= char:
            total_lst.append(word)

    # count how many times the word appears in the text
    cap_words = [word.upper() for word in total_lst]
    word_counts = Counter(cap_words).most_common(rating)

    return word_counts


get_json_top("text.json", 6, 10)
