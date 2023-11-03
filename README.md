# UpTrader
UpTrader - test task

Задача :
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
 
<div style="display: flex; width: 100%;">
  <img src="https://github.com/AliaksandrHus/UpTrader/blob/master/uptrader/screenshot/1.jpg" style="width: 45%;" />
  <img src="https://github.com/AliaksandrHus/UpTrader/blob/master/uptrader/screenshot/2.jpg" style="width: 45%;" />
</div>
