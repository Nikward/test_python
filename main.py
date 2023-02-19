geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def get_vis_russia(geo_logs):
    # Дан список с визитами по городам и странам.
    # Напишите код, который возвращает отфильтрованный список geo_logs,
    # содержащий только визиты из России."

    geo_logs_Russia = []
    for element in range(0, len(geo_logs)):
        if 'Россия' in list(geo_logs[element].values())[0]:
            geo_logs_Russia.append(geo_logs[element])
    return geo_logs_Russia


def get_unique_alues(ids):
    # Выведите на экран все уникальные гео-ID из значений словаря ids.
    # Т.е. список вида [213, 15, 54, 119, 98, 35]

    list_values = []
    for values in ids.values():
        list_values.append(values)
    list_values = list(set(sum(list_values, [])))
    return list_values


def name_chanel_max(stats):
    # Напишите скрипт, который возвращает название канала с максимальным объемом.
    final = max(stats.items())
    return final[0]
