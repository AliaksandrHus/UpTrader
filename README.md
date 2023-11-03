### UpTrader
UpTrader - test task

### Задача:
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
* Меню реализовано через template tag
* Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
* Хранится в БД.
* Редактируется в стандартной админке Django
* Активный пункт меню определяется исходя из URL текущей страницы
* Меню на одной странице может быть несколько. Они определяются по названию.
* При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
* На отрисовку каждого меню требуется ровно 1 запрос к БД
 
<br>
<br>

### Скрины:
 
<div style="display: flex; width: 100%;">
  <img src="https://github.com/AliaksandrHus/UpTrader/blob/master/uptrader/screenshot/1.jpg" style="width: 49%;" />
  <img src="https://github.com/AliaksandrHus/UpTrader/blob/master/uptrader/screenshot/2.jpg" style="width: 49%;" />
</div>


### Примечания:
* Cоздание администратора и миграций, а также их применение:
 
    ```sh
    python manage.py makemigrations
    python manage.py migrate

    python manage.py createsuperuser
    ```
