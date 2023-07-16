/**

Используя операторы языка SQL, создайте табличку “sales”. Заполните ее данными
Сгруппируйте значений количества в 3 сегмента — меньше 100, 100-300 и больше 300.
Создайте таблицу “orders”, заполните ее значениями. Покажите “полный” статус заказа, используя оператор CASE
Чем NULL отличается от 0?

**/

drop database trading;

create database if not exists Trading;
use Trading;
create table if not exists sales 
	(
    id int not null auto_increment primary key,
    order_date date not null, 
    bucket smallint not null
    );
insert into sales values
    (1, "2021-01-01", 103),
    (2, "2021-01-02", 205),
    (3, "2021-01-03", 100),
    (4, "2021-01-04", 288),
    (5, "2021-01-05", 599),
    (6, "2021-01-06", 600),
    (7, "2021-01-07", 301),
    (8, "2021-01-08", 89);

select order_date, bucket,
case 
	when bucket < 100
		then "Маленький заказ"
	when bucket > 300
		then "Большой заказ"
	else "Средний заказ"
end as orders_category
from sales;

create table if not exists orders 
	(
    order_id int not null auto_increment primary key,
    employee_id varchar(3) not null,
    amount float not null, 
    order_status text not null
    );
    
insert into orders values
    (1, "e07", 13.04,"open"),
    (2, "e01", 13.10, "closed"),
    (3, "e04", 98.40, "open"),
    (4, "e06", 79.17, "closed"),
    (5, "e02", 44.00, "canceled"),
    (6, "e03", 98.01, "closed"),
    (7, "e01", 41.59, "closed"),
    (8, "e06", 09.02, "open");

select *,
case 
	when order_status = "open"
		then "Order is in open state"
	when order_status = "closed"
		then "Order is closed"
	when order_status = "canceled"
		then "Order is cancelled"
	else "Unknown state"
end as order_summary
from orders;

# Чем NULL отличается от 0?
# Null - значение отсутствует, т.е. его нет
# 0 - это конкретное значение - 0
create table if not exists null_or_0 
	(
    id int not null auto_increment primary key,
    order_status char(1)
    );

insert into null_or_0 values
    (1, null ),
    (2, 0);
select * from null_or_0