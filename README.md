предлагаю созвониться...

Выполненные задачи****

В фильтрации туров показывать только те даты которые совпали с фильтром price_KGZ #### DONE
Показывать только активные туры в листе туров, похожие туры, туры к этой локации #### DONE
Исправить сортировку с заявками, должны быть по датам тура #### DONE

картинки в похожих туров  #### DONE
картинки в теги коллекции туров #### DONE
добавить is_verified в модель бизнес акк #### DONE
добавить отзывы к тур организатору общий рейтинг и кол-во отзывов #### DONE
не добаляет домен в медиа, надо разобраться в business detail view #### DONE
настроить булево значеня заявок  #### DONE

Еще не решенные задачи ***

настроить показа заявок оплачен не оплачен
исправить показа черновиков, завершенные на разных урл 
продумать механику деактивации тура is_archive
Сделать так что бы все видели только свои данные в CRM
обновить рассылку сообщения на почту
Продумать систему токенов
Оплата
Доработать/Настроить булево значения в туре
Права доступа реализованы не полностью

Придется переделать tour/crm/?is_draft
так как главная модель является датой тура,
нужно сделать отдельный url для черновика


переделать TourSerializers update

***Важно провести оптимизацию serializers и views

//////////

BackEnd теперь всегда будет доступен по:
	http://w-backend.ru/
	
	
Добавлен CRM:

	http://w-backend.ru/concrete_tour/booking/crm/
	http://w-backend.ru/tour/crm/
	
	Заявки/Туры/Даты/
	
	Сразу же к ним Фильтрация/Сортировка
	
	***более подробно внизу

/////////////////////////////////////////////

http://w-backend.ru/redoc/ попробуйте этот инструмент, авто-документация как взаимодействовать с API Wanders
подробно показаны как отправить запрос, какие параметры имеют модели и тд. 

/////////////////////////////////////////////

Slug Tour Удален, Теперь идентификаор является ID
Добавлено About Us для отображения картинок на странице о нас
Отзывы - Полностью готов "наверное"
При переходе на страницу организатора добавлено Туры организатора
Туры к этой локации/ Похожие туры - Полностью готова
Добавленный отдельный url для показа тех туров которыми владеет авторизованный пользователь

////////////////////////////////////////////

ЕЩЕ В РАЗРАБОТКЕ ....

Права доступа реализованы не полностью

обновить рассылку сообщения на почту

Продумать систему токенов

Оплата

Доработать/Настроить булево значения

//////////// CRM  \\\\\\\\\\\\

***** Заявки *****
	http://w-backend.ru/concrete_tour/booking/crm/
	
Фильтрация:
	/?tour_id=
	Показать все заявки к этому туру
	
	?search_date_after=2024-05-14&search_date_before=2024-05-16
	Показать заявки по датам ОТ & ДО
	
Сортировка:
	/?ordering=id
	/?ordering=-id
	сортировка по ID Заявки
	
	/?ordering=concrete_tour_date__start_date
	/?ordering=-concrete_tour_date__start_date
	сортировка по датам тура
	
	/?ordering=is_verified
	/?ordering=-is_verified
	Сортировка по статусу
	
Создание заявки:
	/concrete_tour/booking/create/
	Отправляете post запрос
	{
    "seats_count": 5,
    "concrete_tour_date": 1, передаете id даты
    "name": "ffds",
    "phone": "+999 99999999",
    "email": "mai@dsad.cvf",
    "description": "dvsd"
	}
	
	для того что бы увидеть свои туры и даты к нему
	/tour/author_list/
	
	*нужно предоставить токен
	
***** Туры *****
	http://w-backend.ru/tour/crm/

Фильтрация:
	/?tour_id=4
	что бы увидеть все даты данного тура
	
	?is_active=true
	это окно активные туры
	
	?is_archive=true
	это окно завершенные туры
	
	?is_draft=true
	это окно черновики
	
Сортировка:
	/?ordering=tour__id
	/?ordering=-tour__id
	сортировать по id тура
	
	/?ordering=start_date
	/?ordering=-start_date
	сортировать по датам тура
	
	/?ordering=total_seats_count
	/?ordering=-total_seats_count
	сортировать по оставшимся местам

//// Concrete Tour Date  \\\\

отправляете post запрос на concrete_tour/concrete_date/create/
	tour: передаете id тура
	start_date
	end_date
	price_KGZ
	amount_seat
	
	***total_seats_count - это поле вы не заполняете его используете для отображения оставшиеся места в туре
	
	get для получения названия и id туров
	http://w-backend.ru/tour/author_list/
	
	*нужно предоставить токен
	
ну и так другие методы к нему list и detail
	concrete_tour/concrete_date/list/ не знаю пока для чего нужно
	
	concrete_tour/concrete_date/detail/<id>/



//// BookingTour \\\ Наконец-то реализовано создание заявки
	
отправка запроса на создание concrete_tour/booking/create/

передаете:
	
	seats_count	      количество людей
	concrete_tour_date    передаете id тура
	name
	description
	phone
	email
	
Для вывода всех
	concrete_tour/booking/list/

 PUT, PUTCH, GET, DELETE запрос: Доступен только для is_staff админа
	concrete_tour/booking/detail/<id>


/////////Account\\\\\\\\\

"Регистрация"

на url http://w-backend.ru/account/register/

отправляете POST запрос с данными:
	email
	password
	password_confirm

на почту приходит смс, нажимаете активировать, активируется аккаунт

"Вход в систему"

затем можете авторизоваться по  http://w-backend.ru/account/login/ 
отправляете  POST запрос с данными:
	email
	password

вы получаете два токена:
	refresh - для выхода из системы/ Обновления срока access
	access- для действий создания и изменения вывода и тд.

"Изменение пароля"

на url http://w-backend.ru/account/change-password/    отправляете post запрос:
	
	old_password
	new_password
	new_password_confirm

и не забудьте предоставить токен в разделе Authorization - Bearer Token - "вставляете текст из access"

"Востановление пароля"   http://w-backend.ru/account/restore-password/ отправляете post запрос:
	email

*токен предоставлять не надо*

на почту приходит код, скопируйте его, затем нужно отправить post запрос на http://w-backend.ru/account/set-restored-password/ :
	code
	new_password
	new_password_confirm
	
"Удаление Аккаунта"

на http://w-backend.ru/account/delete-account/   отправляете DELETE пустой запрос с токеном access


"Выход из Аккаунта"
 http://w-backend.ru/account/logout/ 

Все такие оказывается  это реализовывается на фронте, Фронт просто берет и сбрасывает полученный токен
На бэке этот токен попадает в черный список и по истечению определенного врмени удаляется
 
 /// Создание бизнес Аккаунта \\\
 
 После того как вы вошли в систему
 отправляете POST запрос на http://w-backend.ru/business/create/
 	title
 	desc
 	image     *фото, остальные поля текст
	phone     *цифры
	email
	additional_contacts
	instagram
	
	*не забудьте предоставить токен

 
 вывод бизнес аккаунтов http://w-backend.ru/business/list/


* Редактирование Бизнес профиля


 отправляете PUT, PUTCH, GET, DELETE запрос на http://w-backend.ru/business/detail/сюда slug TourAgent/
 	title
 	desc
 	image     *фото, остальные поля текст
	phone     *Цифры
	email
	additional_contacts
	instagram
	
	*не забудьте предоставить токен



 /// Продолжение создания простого пользователя \\\
 
 После того как вы вошли в систему
 отправляете POST запрос на http://w-backend.ru/user/create/
 
 	first_name
 	last_name
 	avatar	- передает одно фото
 	gender	- male
	country 
	city
	bio
	user_image - можете передать множество фотографий
	phone	-цифры
	birthday
 
 [ gender choices ('female', 'Женский'),
        	('male', 'Мужской'),
        	('other', 'Другое') ]


*вывод всех пользователей http://w-backend.ru/user/list/


* удаление/изменение 
 
  отправляете PUT, PUTCH, GET, DELETE запрос на http://w-backend.ru/user/detail/сюда username/
 	first_name
 	last_name
 	avatar	- передает одно фото
 	gender	- male
	country 
	city
	bio
	user_image - можете передать множество фотографий
	phone
	birthday
	
	*не забудьте предоставить токен
 
//// Избранное \\\\


Для создания отправляете запрос на http://w-backend.ru/favorites/create/ 
	[
	    {
		"tour": 1
	    },
	    {
		"tour": 1
	    }
	]
	
	*вы должны предоставить токен 
	
	* это пример добавления нескольких одним запросом, монжо передать один, так и несколько
	* если у вас бизнес аккаунт, не даст доступ
	
Для просмотра всех избранных отправляете get http://w-backend.ru/favorites/list/ 
	вы должны предоставить токен 
	*если у вас бизнес аккаунт, не даст доступ
	
Для удаления http://w-backend.ru/favorites/detail/<сюда id>/
	вы должны предоставить токен 
	*если у вас бизнес аккаунт, не даст доступ
	
	
	
//// Отзыв/Оценка \\\\

Для создания отправляете запрос на http://w-backend.ru/review/create/
	comment
	rating - цифру от 1 до 5
	about - Guide
	tour - передать id тура
	
	вы должны предоставить токен 
	*если у вас бизнес аккаунт, не даст доступ

ABOUT_CHOICES = (
        ('Organizer', 'Об организаторе'),
        ('Guide', 'Об Гиде'),
    )

"для вывода Отзывов/Оценка"

Отправить get запрос на <http://w-backend.ru/review/list/


"Для изменения и удаления "
Отправить DELETE, PUTCH, PUT запрос http://w-backend.ru/review/detail/сюда id/


//// About Us \\\\


Для создания отправляете запрос на http://w-backend.ru/about_us/create/
	title
	image - передать 1 фотографию 
	
	вы должны предоставить токен is_staff админ

"для вывода всех данных

Отправить get запрос на http://w-backend.ru/about_us/list/


"Для изменения и удаления "
Отправить DELETE, PUTCH, PUT запрос http://w-backend.ru/about_us/detail/сюда id/



/////// Location \\\\\\\\\\\\\

URL для вывода локации по полям :  http://w-backend.ru/location/list/
	slug, title, location_info_images, location
	
URL для вывода локации со всеми полями :  http://w-backend.ru/location/dev/

URL для методов "CREATE, RETRIEVE, UPDATE, DESTROY":
	http://w-backend.ru/location/сюда подставить slug локации/

URL для создания : http://w-backend.ru/location/create/
Пример POST запроса на создание в JSON формате:

{
    "title": "Ущелье Ала-Арча",
    "short_description": "Ущелье Ала-Арча — это одна из самых знаменитых достопримечательностей Кыргызстана. Располагается ущелье Ала-Арча в Чуйской области, и является национальным парком.",
    "description": "Располагается ущелье Ала-Арча в Чуйской области, и является национальным парком. Ежегодно это высокогорное ущелье принимает сотни тысяч туристов, как местных, так и иностранных. Причин такой популярности несколько. Во-первых, ущелье Ала-Арча находится всего в 30 километрах от Бишкека, потому сюда легко добраться и есть вся необходимая туристическая инфраструктура: хорошая асфальтированная дорога, магазины, гостиницы, кафе, и места для отдыха среди живописной природы. Во-вторых, ущелье Ала-Арча имеет свои географические особенности — оно находится на центральной и высочайшей части Кыргызского хребта — второго по длине хребта Тянь-Шаня. Потому именно здесь горы вздымаются максимально высоко над равниной, и здесь же начинаются многочисленные тропы на высочайшие пики Кыргызского хребта.Ала-Арча знаменита своей нетронутой природой: обширными еловыми лесами, березовыми рощами, многочисленными родниками с чистой ледниковой водой и могучими скалами.",
    "how_to_get_there": "На территории ущелья располагается национальный парк, поэтому вход или въезд на его территорию является платным. ",
    "coordinates": "42.565181, 74.482783",
    "coordinates_map": "42.565181, 74.482783",
    "location_info_images": [],
    "getting_there": [
        {
            "title": "Маршрутка",
            "travel_time": "1,5 часа",
            "price_travel": "50 сом",
            "description": "Можно добраться на 265 маршрутке, которая ходит в течении дня с Ошского рынка (нужно уточнять, идет ли она до заповедника или нет)."
        },
        {
            "title": "На велосипеде",
            "travel_time": "3 часа",
            "price_travel": "250",
            "description": "Можно добраться маршрутке, которая ходит в течении дня с Ошского рынка (нужно уточнять, идет ли она до заповедника или нет)."
        },
        {
            "title": "Пешком",
            "travel_time": "8 часов",
            "price_travel": "Бесплатно",
            "description": "Просто идешь в направлении пока не дойдешь"
        }
    ],
    "country": [
        {
            "title": "Кыргызстан"
        }
    ],
    "collection": [
        {
            "title": "Прогулка"
        }
    ],
    "location": [
        {
            "title": "Ала-Арча"
        }
    ],
    "tourist_region": [
        {
            "title": "Тянь-Шань Хребет"
        }
    ]
}


////////\\\\\\

варианты чойсез для "type_accommodation" :
	('Tent', 'Палатка'),
        ('Glamping', 'Глэмпинг'),
        ('Hostel', 'Гостинница'),
        ('Hotel', 'Отель'),
        ('Holiday House', 'Дом отдыха'),
        ('Apartments', 'Апартаменты'),
        ('Camp site', 'Турбаза'),
        ('Sanatorium', 'Санаторий'),
        ('Villa', 'Вилла'),


/// Tags \\\


tags/tour_currency/create/
tags/tour_currency/list/
tags/tour_currency/<str:slug>/

tags/type_tour/create/
tags/type_tour/list/
tags/type_tour/<str:slug>/

tags/comfort_level/create/
tags/comfort_level/list/
tags/comfort_level/<str:slug>/

tags/difficulty_level/create/
tags/difficulty_level/list/
tags/difficulty_level/<str:slug>/

tags/insure_condition/create/
tags/insure_condition/list/
tags/insure_condition/<str:slug>/

tags/language/create/
tags/language/list/
tags/language/<str:slug>/

tags/collection/create/
tags/collection/list/
tags/collection/<str:slug>/

tags/country/create/
tags/country/list/
tags/country/<str:slug>/

tags/location/create/
tags/location/list/
tags/location/<str:slug>/

tags/tourist_region/create/
tags/tourist_region/list/
tags/tourist_region/<str:slug>/

tags/all/

# Ну вы поняли короче

вот пример POST запроса:
	{"location": "Срачка"}


	 /////// TOUR \\\\\\\
	
/////////Фильтрация&Сортировка\\\\\\\\\\

все параметры можете посмотреть если перейти по http://w-backend.ru/tour/dev/
нажать на фильтры и в самом низу будет кнопка отправить
после этого в url у вас будут видные все возможные фильтры

ВАЖНО! Самое первое значение для фильтрации ГЛАВНАЯ следующие примененные будут фильтровать из первого парраметра 

Можно сразу отмечать и искать несколько тегов 
Сортировка по одному пукту

***Ключ сортировки /?ordering=

Сортировка/Фильтрация доступна на:
	http://w-backend.ru/tour/list/
	http://w-backend.ru/tour/dev/

Сортировка с самых популярных:
	/?ordering=popular

Сортировка с высокин рейтингом:
	/?ordering=high_rating

От старых к новым: /?ordering=create_date
От новых к старым: /?ordering=-create_date

По price_KGZ от меньшего к большему: /?ordering=concrete_tour_date__price_KGZ
По price_KGZ от большего к меньшему: /?ordering=-concrete_tour_date__price_KGZ

Добавлена фильтраци детям от:
	/?kid_age=


Добавлена фильтраци рейтинг тура от:
	/?rating=

Фильтрация длительности тура от/до: /?amount_of_days_min=2&amount_of_days_max=5
Фильтрация по стоимости тура от/до: /?price_KGZ_min=30&price_KGZ_max=12231


ставите знак "&" и вводите ключ значение

для нескольких аргументов для одного ключа через ","
вот ключи:
{
	'price_KGZ_min', 'price_KGZ_max', 'amount_of_days_min',
	'amount_of_days_max', 'type_accommodation', 'main_location',
	'main_activity', 'search_date_after', 'search_date_before', 
        'tourist_region', 'collection', 'difficulty_level', 'location',
        'people_count', 'rating', 'comfort_level', 'country', 'kid_age',
        'type_tour', 'language'
}

////


url <ip_adress>/tour/author_list/  показ тех туров которыми владеет авторизованный пользователь  

Теперь почти все поля не обязательные для заполнения,"для функцияонала Черновик"
можно отправить пустые фигурные скобки, тур создастся и назовется Черновик

* добавлена возможность редактирования созданного тура 
 PUT, PUTCH, GET, DELETE запрос на <ip_adress>/tour/detail/<id>/

get могут отправлять все, а остальные только владелец

* добавлены 3 булево значения 

is_archive     если она True  то Тур Удален/Окончен
is_draft       если она True  то Тур Находится в черновике
is_verified ---если они оба True  то Тур потвержден, и на данный момент в активной продаже
is_active   ---/


URL для создания http://w-backend.ru/tour/create/

URL для вывода всех туров отфильтрованые по полям: <ip_adress>/tour/list/
	slug, title, amount_of_days, difficulty_level, tour_images,
	main_location, main_activity, country, collection, location,
	tourist_region, price_KGZ, start_dates

URL для вывода всех туров со всеми полями <ip_adress>/tour/dev/

URL для методов "CREATE, RETRIEVE, UPDATE, DESTROY":
	http://w-backend.ru/tour/detail/сюда подставить id тура/
	
Вот пример:
	http://w-backend.ru/tour/detail/2/


Дата создания и статус активный создаются автоматически
        


вот пример POST запроса в JSON формате, отправленный через Postman raw/json:


{   "title": "Иссык-Куль. Жемчужина Кыргызстана.",
    "type_tour": 1,
    "description": "Добро пожаловать в магический мир Иссык-Куль, одного из самых красивых горных озер в мире. Это природное чудо расположено в сердце Киргизии и приглашает вас на незабываемое приключение. От удивительных пейзажей до богатой культурной истории, Иссык-Куль обещает удовольствие и вдохновение для путешественников всех возрастов.",
    "language": [
        {"title": "Русский"},
        {"title": "Кыргызский"}
    ],
    "amount_of_days": 8,
    "min_people": 15,
    "max_people": 25,
    "min_age": 15,
    "max_age": 50,
    "difficulty_level": 1,
    "comfort_level": 1,
    "tour_currency": [
        { "title": "Российский Рубль"} ],
    "insurance_conditions":1,
    "main_activity": "Пеший тур",
    "main_location": "Иссык-Куль",
        "concrete_tour_date": [
            {
            "start_date": "2024-04-01",
            "end_date": "2024-04-10",
            "price_KGZ": 35600,
            "amount_seat": 20
            },
             {
            "start_date": "2024-04-20",
            "end_date": "2024-04-29",
            "price_KGZ": 35600,
            "amount_seat": 20
            }
        ],
    "list_of_things": [
        {
            "title": "Теплею одежду, бутылку воды, термобелье"
        }
    ],
    "included": [
        {"included": "транспортная доставка от аэропорта (в первый и последний день)"},
        {"included": "весь трансфер на комфортном микроавтобусе по программе путешествия"},
        {"included": "проживание в комфортных гостиницах Бишкека (1 день), Каракола (2 дня), Чолпон-Аты на берегу Иссык-Куля (2 день), номера с душем"},
        {"included": "авторская экскурсия по Бишкеку от местных жителей (художников, экскурсоводов)"},
        {"included": "плата за посещение термальных источников Алтын-Арашан"}

    ],
    "not_included": [
        {"not_included": "обеды (средний чек – 500 сом), кроме обеда в ущелье Алтын-Арашан"},
        {"not_included": "ужины, кроме ужина в юртах во второй день"},
        {"not_included": "дополнительные переезды, не включенные в программу"}
    ],
  "country": [
        {"title":"Кыргызстан"}
        ],
  "collection": [
        {"title": "На чиле"},
        {"title": "Прогулка"}
        ],
  "location": [
        {"title": "Иссык-Кульская область"},
        {"title": "Ала-Арча"}
        ],
  "tourist_region": [
        {"title": "Джеты-Огуз"},
        {"title": "Девичьи Слезы"},
        {"title": "Алтын-Арашана"}
        ],
    "question": [
        {
            "question": "Можно ли с детьми?",
            "answer": "Можно с детьми от 7 лет"
        },
        {
            "question": "В основном какую одежду брать?",
            "answer": "Возьмите спортивную одежду, вечером бывает прохладно"
        }
    ],
    "tour_images": [],
    "days": [
        {
            "title": "День 1: Бишкек - знакомство",
            "description": "Встреча группы в аэропорту Бишкека Манас с 15:00 до 15:30. Если ваш самолет прибывает в другое время, сообщите нам об этом, мы поможем найти лучшее решение.На трансфере едем в гостиницу Бишкека. Оставляем вещи и идем на обед. После будет обзорная вечерняя экскурсия по старому центру с экскурсоводом. Мы пройдем цирк, музей Фрунзе, Администрацию президента, можно увидеть, где работает глава государства, и познакомиться с архитектурой этого исторического места. Увидим исторический музей, площадь Ала-Тоо. Рядом найдем нулевой километр, символический центр города. В завершении погуляем по площади Победы. Увидим русский театр драмы и оперный театр.Ночуем в комфортной гостинице Бишкека.",
            "days_images": []
        },
        {
            "title": "День 2: К горам и озеру Иссык-Куль. Беркут шоу",
            "description": "Встреча группы в аэропорту Бишкека Манас с 15:00 до 15:30. Если ваш самолет прибывает в другое время, сообщите нам об этом, мы поможем найти лучшее решение.На трансфере едем в гостиницу Бишкека. Оставляем вещи и идем на обед.",
            "days_images": []
        }
            ],
    "place": [
                {
                    "amount_days": 3,
                    "place_residence": [
                        {
                            "title": "День 1-8: Гостиница SALVE 3*",
                            "description": "Встреча группы в аэропорту Бишкека Манас с 15:00 до 15:30. Если ваш самолет прибывает в другое время, сообщите нам об этом, мы поможем найти лучшее решение. На трансфере едем в гостиницу Бишкека. Оставляем вещи и идем на обед. После будет обзорная вечерняя экскурсия по старому центру с экскурсоводом. Мы пройдем цирк, музей Фрунзе, Администрацию президента, можно увидеть, где работает глава государства, и познакомиться с архитектурой этого исторического места. Увидим исторический музей, площадь Ала-Тоо. Рядом найдем нулевой километр, символический центр города. В завершении погуляем по площади Победы. Увидим русский театр драмы и оперный театр. Ночуем в комфортной гостинице Бишкека. ",
                            "type_accommodation": "Tent",
                            "place_residence_images": []
                        },
                        {
                            "title": "День 5-9: Гостиница SLAV 8*",
                            "description": "Встреча группы в аэропорту Бишкека Манас с 15:00 до 15:30. Если ваш самолет прибывает в другое время, сообщите нам об этом, мы поможем найти лучшее решение. На трансфере едем в гостиницу Бишкека. Оставляем вещи и идем на обед. После будет обзорная вечерняя экскурсия по старому центру с экскурсоводом. Мы пройдем цирк, музей Фрунзе, Администрацию президента,",
                            "type_accommodation": "Holiday House",
                            "place_residence_images": []
                        }
                    ]
                }
        ],
    "guide": [
        {
            "first_name": "Иван",
            "last_name": "Иванов"
        }
    ],
    "is_active": true,
    "is_draft": false
}
