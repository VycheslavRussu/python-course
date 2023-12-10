# Класс человека
class Person:
    # Параметры
    name = str()
    age = int()

    # Конструктор класса
    def __init__(self, name_str, age_int):
        self.__name = name_str
        self.__age = age_int

    # Методы класса
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name_str):
        self.__name = name_str

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age_int):
        if 1 < age_int < 100:
            self.__age = age_int
        else:
            print('Некорректный возраст')


# Класс, который наследует класс Person. При инициализации в него передаются все нужные парамеры класса Personю
class Student(Person):
    # Параметры класса
    is_person_student = bool()

    #Конструктор класса
    def __init__(self, name_str, age_int, is_student):
        super().__init__(name_str, age_int)
        self.__is_person_student = is_student

    # Методы
    @property
    def studies(self):
        return self.__is_person_student
    @studies.setter
    def studies(self, is_student):
        self.__is_person_student = is_student


# Вызов класса

print('Введите имя человека')
name = str(input())

print('Введите возраст человека')
age_sting = input()
if age_sting.isdigit():
    age = int(age_sting)

Serega = Student(name, age, True)

print(Serega.name, Serega.age, Serega.studies)

