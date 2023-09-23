Курсовая работа по ООП ("Парсер вакансий").
Мы используем API для доступа к сайтам с вакансиями, в частности к HeadHunter, и получения информации о вакансиях на основе специфических данных. Основные параметры для этого включают ключевое слово и номер страницы с заданной максимальной вместимостью (100 вакансий на страницу), которые предоставляются пользователем.

Затем мы сохраняем полученные с помощью API данные в файле формата Json, что позволяет нам в последующем работать с этими данными без необходимости делать новые запросы. Если нужно изменить ключевое слово или номер страницы, информацию можно дополнять в файле.

Далее, эти данные обрабатываются с помощью методов класса Vacancy и инициализируются в его атрибутах, образуя список объектов, с которым мы можем продолжить работать.

Мы также разработали специальный метод, который позволяет сравнивать вакансии по уровню заработной платы (при условии, что эта информация изначально доступна), и реализовали магический метод str.

В рамках пользовательского интерфейса мы уточняем у пользователей, с какого сайта они хотели бы видеть вакансии, какие ключевые слова и номер страницы использовать, какое количество вакансий с топовыми зарплатами отобразить, и какой город учесть при выборе вакансий. Кроме того, в случае с HeadHunter, мы уточняем, интересуют ли пользователей вакансии за границей и с возможностью релокации из России.