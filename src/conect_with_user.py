from src.Parser import HHParser
from src.Parser import SJParser
from src.Parser import FullParser
from src.vacancy import HHVacancy
from src.vacancy import SJVacancy
from src.vacancy import CombVacancy
from src.favorites_vacancy import FavJson
import json


#класс для работы с интерфейсом пользователя
class HelloUser:

    def options_for_action(self, number):
        if number == 0:
            exit(0)
        elif number == 1:
            numb = self.text(number)
            if numb == 4:
                num = self.take_hh_vacancy(input('''
                Если желаете, введите ключевое слово для сортировки поиска. 
                Иначе, нажмите "Enter.
                "'''))
                if num == 7:
                    self.add_to_favorites_hh()
                elif num == 8:
                    self.take_ge_hh()
                elif num == 0:
                    breakpoint(0)
            elif numb == 5:
                num = self.take_sj_vacancy(input('''
                Если желаете, введите ключевое слово для сортировки поиска. 
                Иначе, нажмите "Enter."'''))
                if num == 7:
                    self.add_to_favorites_sj()
                elif num == 8:
                    self.take_ge_sj()
                elif num == 0:
                    breakpoint(0)
            elif numb == 6:
                num = self.take_comb_vacancy(input('''
                Если желаете, введите ключевое слово для сортировки поиска. 
                Иначе, нажмите "Enter."'''))
                if num == 7:
                    self.add_to_favorites_comb()
                elif num == 8:
                    self.take_ge_comb()
                elif num == 0:
                    breakpoint(0)
        elif number == 2:
            with open('favorites_vacancy.json', 'r') as file:
                vac = json.load(file)
                counter = 1
                if vac:
                    for counter, vacancy in enumerate(vac, start=1):
                        print(f"Вакансия номер {counter}:")
                        print(f"Название: {vacancy['name']}")
                        print(f"Зарплата: {vacancy['salery_from']}")
                        print(f"URL: {vacancy['url']}")
                        if vacancy['responsibility']:
                            print(f"Обязанности: {vacancy['responsibility']}")
                        else:
                            print("Обязанности: Не указаны")
                        print("\n")
                else:
                    print('Файл пуст.')
        elif number == 3:
            self.del_the_fav()

    def text(self, number):
        if number == 1:
            return int(input(f'''
            4.Получить вакансии с сайта hh.ru
            5.Получить вакансии с сайта Superjob.ru
            6.Получить вакансии с обоих сайтов    
            '''))
        elif number == 3:
            return int(input('''
            Введите номер вакансии, которую желаете удалить:
            Если желаете удалить все, введите 'Все'
            '''))

#получает и выводит вакансии с hh.ru в читабельном виде, предварительно записав в файл и отсортировав
    def take_hh_vacancy(self, word=None):
        hhp = HHParser(word)
        hhp.to_json()
        show = []
        with open('vacansies_from_hh.json', 'r') as file:
            vacancies_data = json.load(file)
            for counter, case in enumerate(vacancies_data):
                vacancy = HHVacancy(counter)
                try:
                    vacancy.salery_from = case['salary']['from']
                except (KeyError, TypeError):
                    vacancy.salery_from = ''
                vacancy.name = case.get('name', '')
                vacancy.url = case.get('alternate_url', '')
                vacancy.responsibility = case.get('snippet', {}).get('responsibility', '')
                show.append(vacancy)
                print(f'''Вакансия номер {counter}:\n{vacancy}''')
        with open('vacansies_from_hh.json', 'w') as file:
            json.dump([v.__dict__() for v in show], file, indent=4, ensure_ascii=False)
        return int(input('''
        7.Добавить вакансию из списка в избранное
        8.Сравнить зарплаты в вакансиях
        0.Завершить работу
        '''))

    # получает и выводит вакансии с Superjob.ru в читабельном виде, предварительно записав в файл и отсортировав
    def take_sj_vacancy(self, word=None):
        sjp = SJParser(word)
        sjp.to_json()
        show = []
        with open('vacansies_from_sj.json', 'r') as file:
            vacancies_data = json.load(file)
            for counter, case in enumerate(vacancies_data):
                vacancy = SJVacancy(counter)
                try:
                    vacancy.salery_from = case.get('payment_from', '')
                except (KeyError, TypeError):
                    vacancy.salery_from = ''
                vacancy.name = case.get('profession', '')
                vacancy.url = case.get('link', '')
                vacancy.responsibility = case.get('candidat', '')
                show.append(vacancy)
                print(f'''Вакансия номер {counter}:\n{vacancy}''')
        with open('vacansies_from_sj.json', 'w') as file:
            json.dump([v.__dict__() for v in show], file, indent=4, ensure_ascii=False)
        return int(input('''
        7.Добавить вакансию из списка в избранное
        8.Сравнить зарплаты в вакансиях
        0.Завершить работу
        '''))

    # получает и выводит вакансии с двух сайтов в читабельном виде, предварительно записав в файл и отсортировав
    def take_comb_vacancy(self, word=None):
        cp = FullParser(word)
        cp.to_json()
        show = []
        with open('combined_vacancies.json', 'r') as file:
            vacancies_data = json.load(file)
            for counter, case in enumerate(vacancies_data):
                vacancy = CombVacancy(counter)
                try:
                    vacancy.salery_from = case.get('payment_from', '') or case.get('salery', {}).get('from', '')
                except (KeyError, TypeError):
                    vacancy.salery_from = ''
                vacancy.name = case.get('profession', '') or case.get('name', '')
                vacancy.url = case.get('link', '') or case.get('alternate_url', '')
                vacancy.responsibility = case.get('candidat', '') or case.get('snippet', {}).get('responsibility', '')
                show.append(vacancy)
                print(f'''Вакансия номер {counter}:\n{vacancy}''')
        with open('combined_vacancies.json', 'w') as file:
            json.dump([v.__dict__() for v in show], file, indent=4, ensure_ascii=False)
        return int(input('''
        7.Добавить вакансию из списка в избранное
        8.Сравнить зарплаты в вакансиях
        0.Завершить работу
        '''))

    def add_to_favorites_hh(self):
        with open('vacansies_from_hh.json', 'r') as file:
            try:
                show = json.loads(file.read())
            except json.JSONDecodeError:
                print("Файл пуст или имеет неверный формат JSON.")
                return

        n = int(input('Введите номер вакансии, которую желаете добавить в избранное:'))
        fav = FavJson()
        fav.add_to_file(show[n])

    def add_to_favorites_sj(self):
        with open('vacansies_from_sj.json', 'r') as file:
            try:
                show = json.loads(file.read())
            except json.JSONDecodeError:
                print("Файл пуст или имеет неверный формат JSON.")
                return

        n = int(input('Введите номер вакансии, которую желаете добавить в избранное:'))
        fav = FavJson()
        fav.add_to_file(show[n])

    def add_to_favorites_comb(self):
        with open('combined_vacancies.json', 'r') as file:
            try:
                show = json.loads(file.read())
            except json.JSONDecodeError:
                print("Файл пуст или имеет неверный формат JSON.")
                return

        n = int(input('Введите номер вакансии, которую желаете добавить в избранное:'))
        fav = FavJson()
        fav.add_to_file(show[n])

    def take_ge_hh(self):
        with open('vacansies_from_hh.json', 'r') as file:
            show = json.load(file)

        num = input('Введите две цифры через пробел:').split(' ')

        vacancy1 = HHVacancy(int(num[0]))
        vacancy2 = HHVacancy(int(num[1]))

        vacancy1.salery_from = show[int(num[0])]['salery_from']
        vacancy2.salery_from = show[int(num[1])]['salery_from']

        vacancy1.compare_salary(vacancy2)

    def take_ge_sj(self):
        with open('vacansies_from_sj.json', 'r') as file:
            show = json.load(file)
        num = input('Введите две цифры через пробел:').split(' ')

        vacancy1 = SJVacancy(int(num[0]))
        vacancy2 = SJVacancy(int(num[1]))

        vacancy1.salery_from = show[int(num[0])]['salery_from']
        vacancy2.salery_from = show[int(num[1])]['salery_from']

        vacancy1.compare_salary(vacancy2)

    def take_ge_comb(self):
        with open('combined_vacancies.json', 'r') as file:
            show = json.load(file)
        num = input('Введите две цифры через пробел:').split(' ')

        vacancy1 = CombVacancy(int(num[0]))
        vacancy2 = CombVacancy(int(num[1]))

        vacancy1.salery_from = show[int(num[0])]['salery_from']
        vacancy2.salery_from = show[int(num[1])]['salery_from']

        vacancy1.compare_salary(vacancy2)

    def del_the_fav(self):
        a = input('''
        Введите номер, который желаете удалить:
        Если хотете удалить всё, нажмите "Enter
        "''')
        if isinstance(a, int):
            fv = FavJson()
            fv.delete_from_file(int(a))
        else:
            with open('favorites_vacancy.json', 'w') as file:
                file.truncate(0)
