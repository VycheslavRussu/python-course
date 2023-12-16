import os
import sys
import itertools

def project_stats(path, extensions):
    # Возвращает число строк в исходниках проекта с выбранными файловыми форматами

    file_list = list()
    for root, directories, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root) + '/' + file)

    selected_filepaths = list()
    for filepath in file_list:
        file_name = os.path.basename(filepath)
        if os.path.splitext(file_name)[1] in extensions:
            selected_filepaths.append(filepath)

    string_count = int()
    for file_path in selected_filepaths:
        print(file_path)
        with open(file_path, 'r') as file:
            string_count += file.read().count('\n')

    return string_count
    pass

def total_number_of_lines(filenames):
    # Вернуть общее число строк в файлах ``filenames``
    string_count = int()
    for file_name in filenames:
        with open(file_name, 'r') as file:
            string_count += file.read().count('\n')
    return string_count
    pass

def number_of_lines(filename):
    # Вернуть число строк в файле.
    with open(filename, 'r') as file:
        string_count = file.read().count('\n')
    return string_count
    pass

def iter_filenames(path):
    # Итератор по именам файлов в дереве
    file_list = list()
    for root, directories, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root) + '/' + file)
    return file_list
    pass

def with_extensions(extensions, filenames):
    # Оставляем только те имена файлов, у которых расширение одно из списка
    list_filenames = list()

    for filepath in filenames:
        file_name = os.path.basename(filepath)
        if os.path.splitext(file_name)[1] in extensions:
            list_filenames.append(os.path.splitext(file_name)[0])

    return list_filenames
    pass

def get_extension(filename):
    # Возвращает расширение файла
    return os.path.splitext(filename)[1]
    pass
