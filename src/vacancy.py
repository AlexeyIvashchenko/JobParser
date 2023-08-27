from abc import ABC, abstractmethod


class Vacancy(ABC):
    @abstractmethod
    def __init__(self):
        pass


class HHVacancy(Vacancy):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        self.name = str()
        self.salery_from = int()
        self.currency = 'RUB'
        self.url = str()
        self.responsibility = str()

    def __ge__(self, other):
        if self.salery_from > other.salery_from:
            print("Заработная плата первой вакансии больше.")
        elif self.salery_from < other.salery_from:
            print("Заработная плата второй вакансии больше.")
        else:
            print("Предлагаемые заработные платы равны, или их невозможно сравнить.")

    class SJVacancy(Vacancy):
        def __init__(self, number):
            self.number = number

        def __str__(self):
            self.name = ''
            self.salery_from = 0
            self.currency = 'RUB'
            self.url = ''
            self.responsibility = ''

        def __ge__(self, other):
            if self.salery_from > other.salery_from:
                print("Заработная плата первой вакансии больше.")
            elif self.salery_from < other.salery_from:
                print("Заработная плата второй вакансии больше.")
            else:
                print("Предлагаемые заработные платы равны, или их невозможно сравнить.")
