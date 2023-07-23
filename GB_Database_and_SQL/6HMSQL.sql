/**
1. Создайте функцию, которая принимает кол-во сек и формат их в кол-во дней часов. Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds '
2. Выведите только четные числа от 1 до 10. Пример: 2,4,6,8,10
**/

/**
Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет" "Зачет" ставится,
если слушатель успешно выполнил 1 или 2 задачи "Незачет"
ставится, если слушатель успешно выполнил 0 задач Критерии оценивания:
1 - слушатель верно создал функцию, которая принимает кол-во сек и формат их в кол-во дней часов.
2 - слушатель выведили только четные числа от 1 до 10.
**/
use cars;
drop PROCEDURE print_time_in_row;

delimiter //
CREATE PROCEDURE print_time_in_row(seconds INT)
BEGIN
    DECLARE days INT default 0;
    DECLARE hours INT default 0;
    DECLARE minutes INT default 0;
    DECLARE required_text TEXT;

    SET days = seconds div 84600;
    SET seconds = seconds % 84600;

    SET hours = seconds div 3600;
    SET seconds = seconds % 3600;

    SET minutes = seconds div 60;
    SET seconds = seconds % 60;
    
SELECT days, hours, minutes, seconds/**required_text**/;
END //
delimiter ;

CALL print_time_in_row(17394857);

delimiter //
CREATE PROCEDURE even_numbers()
BEGIN
    DECLARE n INT default 0;
    DROP TABLE IF EXISTS nums;
    CREATE TABLE nums (n INT);

    WHILE n < 10 DO
    SET n = n + 2;
    INSERT INTO nums VALUES(n);
    END WHILE;

SELECT * FROM nums;
END //
delimiter ;

CALL even_numbers();
