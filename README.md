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
