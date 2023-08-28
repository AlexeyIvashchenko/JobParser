#класс для работы с данными с сайта hh.ru
class HHVacancy:
    def __init__(self, number):
        self.number = number
        self.name = ''
        self.salery_from = ''
        self.url = ''
        self.responsibility = ''

    def __str__(self):
        return f"Номер: {self.number}, Название: {self.name}, Зарплата: {self.salery_from}, URL: {self.url}, Обязанности: {self.responsibility}"

    def __dict__(self):
        return {
            "number": self.number,
            "name": self.name,
            "salery_from": self.salery_from,
            "url": self.url,
            "responsibility": self.responsibility
        }

#функция для сравнения зароботных плат
    def compare_salary(self, other):
        if self.salery_from and other.salery_from:
            if int(self.salery_from) > int(other.salery_from):
                print("Заработная плата первой вакансии больше.")
            elif int(self.salery_from) < int(other.salery_from):
                print("Заработная плата второй вакансии больше.")
            else:
                print("Предлагаемые заработные платы равны, или их невозможно сравнить.")
        else:
            print("У одной из вакансий нет указанной заработной платы.")


#класс для работы с данными с сайта Superjob.ru
class SJVacancy:
    def __init__(self, number):
        self.number = number
        self.name = ''
        self.salery_from = ''
        self.url = ''
        self.responsibility = ''

    def __str__(self):
        return f"Номер: {self.number}, Название: {self.name}, Зарплата: {self.salery_from}, URL: {self.url}, Обязанности: {self.responsibility}"

    def __dict__(self):
        return {
            "number": self.number,
            "name": self.name,
            "salery_from": self.salery_from,
            "url": self.url,
            "responsibility": self.responsibility
        }

    # функция для сравнения зароботных плат
    def compare_salary(self, other):
        if self.salery_from and other.salery_from:
            if int(self.salery_from) > int(other.salery_from):
                print("Заработная плата первой вакансии больше.")
            elif int(self.salery_from) < int(other.salery_from):
                print("Заработная плата второй вакансии больше.")
            else:
                print("Предлагаемые заработные платы равны, или их невозможно сравнить.")
        else:
            print("У одной из вакансий нет указанной заработной платы.")


#класс для работы с данными с обоих сайтов
class CombVacancy:
    def __init__(self, number):
        self.number = number
        self.name = ''
        self.salery_from = ''
        self.url = ''
        self.responsibility = ''

    def __str__(self):
        return f"Номер: {self.number}, Название: {self.name}, Зарплата: {self.salery_from}, URL: {self.url}, Обязанности: {self.responsibility}"

    def __dict__(self):
        return {
            "number": self.number,
            "name": self.name,
            "salery_from": self.salery_from,
            "url": self.url,
            "responsibility": self.responsibility
        }

    # функция для сравнения зароботных плат
    def compare_salary(self, other):
        if self.salery_from and other.salery_from:
            if int(self.salery_from) > int(other.salery_from):
                print("Заработная плата первой вакансии больше.")
            elif int(self.salery_from) < int(other.salery_from):
                print("Заработная плата второй вакансии больше.")
            else:
                print("Предлагаемые заработные платы равны, или их невозможно сравнить.")
        else:
            print("У одной из вакансий нет указанной заработной платы.")
