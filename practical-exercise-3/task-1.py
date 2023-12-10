class Student:
    # Атрибуты класса
    skill_level = 0
    # Методы
    def get_python_skill(self):
        return self.skill_level
    def learn_python(self):
        self.skill_level += 1
        return self.skill_level

s = Student()
s.get_python_skill()


