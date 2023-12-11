import os
import sys
import itertools

# example_path = '/Users/vycheslav/PycharmProjects/python-course/practical-exercise-3'
#
# os.walk(example_path, topdown=True)

# def project_stats(path, extensions):
#     # Вернуть число строк во всех файлах с заданным расширением
#     example_extensions = ['.py', '.md']
#     example_path = '/Users/vycheslav/PycharmProjects/python-course/practical-exercise-3'
#
#
#     """
#     Вернуть число строк в исходниках проекта.
#
#     Файлами, входящими в проект, считаются все файлы
#     в папке ``path`` (и подпапках), имеющие расширение
#     из множества ``extensions``.
#     """
#     pass
#
#
# def total_number_of_lines(filenames):
#     """
#     Вернуть общее число строк в файлах ``filenames``.
#     """
#     pass
#
#
# def number_of_lines(filename):
#     """
#     Вернуть число строк в файле.
#     """
#     pass
#
#
# def iter_filenames(path):
#     """
#     Итератор по именам файлов в дереве.
#     """
#     pass
#
#
# def with_extensions(extensions, filenames):
#     """
#     Оставить из итератора ``filenames`` только
#     имена файлов, у которых расширение - одно из ``extensions``.
#     """
#     pass
#
#

def get_extension(filename):
    # Возвращает расширение файла
    return os.path.splitext(filename)[1]
    pass

print(get_extension('jopa.py'))