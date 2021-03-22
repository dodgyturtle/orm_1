#  Пульт охраны труда
 Отображает сотрудников:
 - С активными картами доступа.
 - Находящимися в хранилище на дату и время запроса.
 - Список посещения хранилища. Если длительность прибывания в хранилища более 60 минут, выставляется флаг "подозрительности".

### Установка
- Скачать скрипт с [GitHub](https://github.com/dumbturtle/orm_1).

-  В `project/settings.py` в разделе `DATABASES` внести данные для доступа к базе данных.

- Установить необходимые пакеты: 
     
```
$ pip install -r requirements.txt
```
- Запустить:
```
$ python main.py
``` 