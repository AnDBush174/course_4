# user_interaction.py
from src.api_classes import HHApi
from src.json_operations import JSon
from src.vacancy import Vacancy


def user_interaction():
    """
    Функция, реализущая взаимодействие с пользователем.
    Пользователь выбирает платформу, ключевое слово, страницу сайта
    Фунцкция сортирует полученные данные по зарплате, и пользователь указывает какое количество вакансий вывести
    Также происходит сортировка город, который также определяется пользователем
    Для платформы HeadHunter выводится информация по зарубежным вакансиям.
    """
    input_keyword = input('Введите ключевое слово, по которому будем получать поиск вакансии с сайта: ')
    input_page_number = int(input('С какой страницы получать информацию?\n'
                                  'Для получения самых свежих данных укажите пожалуйста цифру 0: '))
    input_top_number = int(input('Какое количество самых высокооплачеваемых профессий показать?'
                                 '(Только для RU-региона): '))
    input_area = input('По какому городу хотите узнать о вакансиях, отвечающих вашему запросу: ')
    try:
        hh_vacancies = HHApi(input_page_number, input_keyword).get_info_from_site()
    except Exception as e:
        print("Возникла ошибка при получении информации с сайта: ", e)
        return

    JSon('vacancies_from_hh.json', hh_vacancies).write_info()
    Vacancy.hh_create_list_of_objects('vacancies_from_hh.json')
    input_region = input('Отобразить доступные вакансии из зарубежных государств '
                         'и вакансии с релокацией?(Да/Нет): ')
    if input_region == 'Да':
        hh_foreign_vacancies = [vacancy for vacancy in Vacancy.hh_list_of_objects if
                                vacancy.salary['currency'] != 'RUR']  # получаем зарубежные вакансии
        print('\nДоступные вакансии зарубежом и вакансии с релокацией:')
        for job in hh_foreign_vacancies:
            print(f'{job}\n')
    hh_list = [vacancy for vacancy in Vacancy.hh_list_of_objects if vacancy.salary['to'] is not None and
               vacancy.salary['currency'] == 'RUR']  # отфильтрованный список для вывода топа по зарплате
    hh_list.sort(key=lambda x: x.salary['to'])
    hh_list.reverse()
    print('Топ вакансий:\n')
    for vacancy in hh_list[:input_top_number]:
        print(vacancy)
    hh_sorted_area = [work for work in Vacancy.hh_list_of_objects
                      if work.area == input_area]  # получаем вакансии по городу
    if len(hh_sorted_area) == 0:
        print('В этом городе вакансий нет')
    else:
        print('В указанном городе есть следующие вакансии: ')
        for work_in_city in hh_sorted_area:
            print(work_in_city)