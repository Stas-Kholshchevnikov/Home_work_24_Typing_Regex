#Используемые процедуры

def create_generator(file_name):
    """
    Функция задания генератора для построчного чтения файла
    """
    with open(file_name) as file:
        for line in file:
            yield line


def filter_proc(value, data):
    """
    Функция filter
    """
    return filter(lambda item: value in item, data)


def map_proc(value, data):
    """
    Функция map
    """
    return map(lambda item: item.split(' ')[int(value)], data)


def sort_proc(value, data):
    """
    Функция sorted
    """
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def unique_proc(value, data):
    """
    Функция unique
    """
    return set(data)


def limit_proc(value, data):
    """
    Функция limit
    """
    return list(data)[:int(value)]
