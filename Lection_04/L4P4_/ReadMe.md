# Идея: совместная разработка

Есть файл, состоящий из N тысяч строк, содержащих информацию о неких пользователях.
Предлагаемые поля: id, имя, фамилия, день рождения, место работы, номер телефона (может быть несколько).
В качестве симпвола разделителя использовать пустую строку.

* Модуль 1: сбор информации с датчиков (**data_provider**)
            *get_temperature, get_pressure, get_wind_speed*
* Модуль 2: логирование (**logger**)
            *temperature_logger, pressure_logger, wind_speed_logger*
* Модуль 3: UI (**user_interface**)
            *temperature_view, pressure_view, wind_speed_view*
* Модуль 4: HTML-генератор (**html_creater**)
            *create*
* Модуль 5: главный модуль (**main**)