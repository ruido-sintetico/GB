/**
1. Создайте представление, в которое попадут автомобили стоимостью до 25 000 долларов
2. Изменить в существующем представлении порог для стоимости: пусть цена будет до 30 000 долларов (используя оператор ALTER VIEW)
3. Создайте представление, в котором будут только автомобили марки “Шкода” и “Ауди” (аналогично)
**/

drop database cars;
create database if not exists cars;
use cars;

create table cars
(
    id  int auto_increment primary key,
    name varchar(255) not null,
    cost  float not null
);

INSERT INTO cars (id, name, cost) VALUES (1, 'audi', 52642);
INSERT INTO cars (id, name, cost) VALUES (2, "mersedes", 57127);
INSERT INTO cars (id, name, cost) VALUES (3, "skoda", 9000);
INSERT INTO cars (id, name, cost) VALUES (4, "volvo", 29000);
INSERT INTO cars (id, name, cost) VALUES (5, "Bentley", 350000);
INSERT INTO cars (id, name, cost) VALUES (6, "Citroen", 21000);
INSERT INTO cars (id, name, cost) VALUES (7, "Hummer", 41400);
INSERT INTO cars (id, name, cost) VALUES (8, "Volkswfagen", 21600);

/**
Есть таблица анализов Analysis:
an_id — ID анализа;
an_name — название анализа;
an_cost — себестоимость анализа;
an_price — розничная цена анализа;
an_group — группа анализов.
Есть таблица групп анализов Groups:
gr_id — ID группы;
gr_name — название группы;
gr_temp — температурный режим хранения.
Есть таблица заказов Orders:
ord_id — ID заказа;
ord_datetime — дата и время заказа;
ord_an — ID анализа.
**/

drop database analysis;
create database if not exists analysis;
use analysis;

create table anls
(   
	an_id int auto_increment primary key,
	an_name varchar(255) not null,
	an_cost int not null,
	an_price int not null,
	an_group int not null
);
create table grs
( 
    gr_id int auto_increment primary key,
	gr_name varchar(255) not null,
	gr_temp int not null
);
create table orders
(   
	ord_id int auto_increment primary key,
	ord_datetime datetime not null,
	ord_an int not null
);

INSERT INTO anls (an_id, an_name, an_cost, an_price, an_group) VALUES (1, "first", 1000, 1500, 2);
INSERT INTO anls (an_id, an_name, an_cost, an_price, an_group) VALUES (2, "second", 600, 950, 1);
INSERT INTO anls (an_id, an_name, an_cost, an_price, an_group) VALUES (3, "third", 2000, 3500, 2);
INSERT INTO grs (gr_id, gr_name, gr_temp) VALUES (1, "cal", 10);
INSERT INTO grs (gr_id, gr_name, gr_temp) VALUES (2, "fluid", 20);
INSERT INTO orders (ord_id, ord_datetime, ord_an) VALUES (1, "2020-01-10 15:30:00", 1);
INSERT INTO orders (ord_id, ord_datetime, ord_an) VALUES (2, "2020-02-05 09:32:30", 2);
INSERT INTO orders (ord_id, ord_datetime, ord_an) VALUES (3, "2020-02-12 12:37:30", 3);
INSERT INTO orders (ord_id, ord_datetime, ord_an) VALUES (4, "2020-04-01 12:00:10", 4);
INSERT INTO anls (an_id, an_name, an_cost, an_price, an_group) VALUES (4, "forth", 900, 1500, 1);