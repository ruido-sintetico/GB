/**
1. Создайте представление, в которое попадут автомобили стоимостью до 25 000 долларов
2. Изменить в существующем представлении порог для стоимости: пусть цена будет до 30 000 долларов (используя оператор ALTER VIEW)
3. Создайте представление, в котором будут только автомобили марки “Шкода” и “Ауди” (аналогично)
**/

-- Task1
use cars;

create or replace view cars_less_25000 as
	select * 
	from cars
	where cost < 25000; 

select *
from cars_less_25000;

-- Task2
alter view cars_less_25000 as
	select * 
	from cars
	where cost < 30000; 

select *
from cars_less_25000;

-- Task3
create or replace view cars_shkoda_and_audi as
	select * 
	from cars
	where name in ("skoda", "audi");
    
select *
from cars_shkoda_and_audi;    

-- Вывести название и цену для всех анализов, которые продавались 5 февраля 2020 и всю следующую неделю.
use analysis;

select a.an_name, a.an_cost, o.ord_datetime
from anls a
join orders o
on o.ord_an = a.an_id
where o.ord_datetime between '2020-02-05 00:00'
and '2020-02-12 23:59'
