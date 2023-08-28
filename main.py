from src.conect_with_user import HelloUser

if __name__ == '__main__':
    user = input('''Здравствуйте, это программа для парсинга на сайтах hh.ru и Superjob.ru
   Введите ваше имя:''')
    human = HelloUser()
    human.options_for_action(int(input(
        f'''
   Здравствуйте {user}!
   Введите цифру желаемого действия:
   1.Получить вакансии
   2.Показать избранные вакансии.
   3.Удалить избранную(-ые) вакансию(-ии)
   0.Завершить работу.
   ''')))
