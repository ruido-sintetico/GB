-- Вывести на экран сколько машин каждого цвета для машин марок BMW и LADA

select * from auto;

select mark, color, count(mark) as amt
from auto
Where mark in ("LADA", "BMW")
group by color, mark;

-- Вывести на экран марку авто и количество AUTO не этой марки

select distinct mark, (select count(1) from auto a1 where a1.mark != a.mark) as c
from auto a;

-- Задание №3.
-- Даны 2 таблицы, созданные следующим образом:

-- create table if not exists test_a (id int, data varchar(1));
-- create table if not exists test_b (id int, data varchar(1));
/**
insert into test_a(id, data) values
(10, 'A'),
(20, 'A'),
(30, 'F'),
(40, 'D'),
(50, 'C');
insert into test_b(id) values
(10),
(30),
(50);
**/
-- Напишите запрос, который вернет строки из таблицы test_a, id которых нет в таблице test_b, НЕ используя ключевого слова NOT.

select *
from test_a
left join test_b on test_b.id = test_a.id 
where test_b.id is null