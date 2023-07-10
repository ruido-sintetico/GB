/**

Условие:
Таблица для работы на слайде.
1. Напишите запрос который вывел бы таблицу со столбцами в следующем порядке: city, sname, snum, comm. (к первой или второй таблице, используя SELECT)
2. Напишите команду SELECT, которая вывела бы оценку(rating), сопровождаемую именем каждого заказчика в городе San Jose. (“заказчики”)
3. Напишите запрос, который вывел бы значения snum всех продавцов из таблицы заказов без каких бы то ни было повторений. (уникальные значения в “snum“ “Продавцы”)
4*. Напишите запрос, который бы выбирал заказчиков, чьи имена начинаются с буквы G. Используется оператор "LIKE": (“заказчики”) https://dev.mysql.com/doc/refman/8.0/en/string-comparison-functions.html
5. Напишите запрос, который может дать вам все заказы со значениями суммы выше чем $1,000. (“Заказы”, “amt” - сумма)
6. Напишите запрос который выбрал бы наименьшую сумму заказа.
(Из поля “amt” - сумма в табличке “Заказы” выбрать наименьшее значение)
7. Напишите запрос к табличке “Заказчики”, который может показать всех заказчиков, у которых рейтинг больше 100 и они находятся не в Риме.

Таблица workers:
1. Отсортируйте поле “зарплата” в порядке убывания и возрастания
2. Отсортируйте по возрастанию поле “Зарплата” и выведите 5 строк с наибольшей заработной платой
3. Выполните группировку всех сотрудников по специальности , суммарная зарплата которых превышает 100000

**/
drop database customers_and_sellers;
drop database job;

create database if not exists customers_and_sellers;
use customers_and_sellers;
create table if not exists salespeople 
	(
    snum int not null primary key,
    sname text not null, 
    city text not null,
    comm float not null
    );
    
insert into salespeople values
    (1001, "Peel", "London", 0.12),
    (1002, "Serres", "San Jose", 0.13),
    (1004, "Motica", "London", 0.11),
    (1007, "Rifkin", "Barselona", 0.15),
    (1003, "Axelrod", "New York", 0.10);
    
create table if not exists customers
	(
    cnum int not null primary key,
    cname text not null, 
    city text not null,
    rating int not null default 0,
    snum int not null
    );
    
insert into customers values
    (2001, "Hoffman", "London", 100, 1001),
    (2002, "Giovanni", "Rome", 200, 1003),
    (2003, "Liu", "San Jose", 200, 1002),
    (2004, "Grass", "Berlin", 300, 1002),
    (2006, "Glemens", "London", 100, 1001),
    (2008, "Cisneros", "San Jose", 300, 1007),
    (2007, "Pereira", "Rome", 100, 1004);

create table if not exists orders
	(
    onum int not null primary key,
    amt float not null, 
    odate date not null,
    cnum int not null,
    snum int not null
    );

insert into orders values
    (3001, 18.69, "1990-03-10", 2008, 1007),
    (3003, 767.19, "1990-03-10", 2001, 1001),
    (3002, 1900.10, "1990-03-10", 2007, 1004),
    (3005, 5160.45, "1990-03-10", 2003, 1002),
    (3006, 1098.16, "1990-03-10", 2008, 1007),
    (3009, 1713.23, "1990-04-10", 2002, 1003),
    (3007, 75.75, "1990-04-10", 2004, 1002),
    (3008, 4723.00, "1990-05-10", 2006, 1001),
    (3010, 1309.95, "1990-06-10", 2004, 1002),
    (3011, 9891.88, "1990-06-10", 2006, 1001);
    
-- Task 1
select city, sname, snum, comm from salespeople;

-- Task 2
select rating, cname from customers
where city = "San Jose";

-- Tasl 3 
select distinct snum from salespeople;

-- Task 4
select * from customers
where cname like "G%";

-- Task 5
select * from orders
where amt > 1000;

-- Task 6
select min(amt) from orders;

-- Task 7
select * from customers 
where rating > 100
and not city = "Rome";


-- Workers
create database if not exists job;
use job;
create table if not exists workers
	(
    id int not null auto_increment primary key,
    name varchar(20) not null, 
    surname varchar(30) not null,
    speciality varchar(20) not null,
    seniority int not null,
    salary bigint not null,
    age int not null
    );

insert into workers values
    (1, "Вася", "Васькин", "Начальник", 40, 100000, 60),
    (2, "Петя", "Петькин", "Начальник", 8, 70000, 30),
    (3, "Катя", "Каткина", "Инженер", 2, 70000, 25),
    (4, "Саша", "Сашкин", "Инженер", 12, 50000, 35),
    (5, "Иван", "Иванов", "Рабочий", 40, 30000, 59),
    (6, "Петр", "Петров", "Рабочий", 20, 25000, 40),
    (7, "Сидор", "Сидоров", "Рабочий", 10, 20000, 35),
    (8, "Антон", "Антонов", "Рабочий", 8, 19000, 28),
    (9, "Юра", "Юркин", "Рабочий", 5, 15000, 25),
    (10, "Максим", "Воронин", "Рабочий", 2, 11000, 22),
    (11, "Юра", "Галкин", "Рабочий", 3, 12000, 24),
    (12, "Люся", "Люськина", "Уборщик", 10, 10000, 49);
    
-- Task 1
select name, surname, salary
from workers
order by salary desc;

select name, surname, salary
from workers
order by salary;

-- Task 2
select name, surname, salary
from workers
order by salary desc 
limit 5;

-- Task 3
--  Выполните группировку всех сотрудников по специальности , суммарная зарплата которых превышает 100000

select speciality, count(*) as amnt, sum(salary) as sal_amnt
from workers
group by speciality
having sal_amnt > 100000;

