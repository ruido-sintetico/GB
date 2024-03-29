// Необходимо создать html-страницу с названием 2.html, в которой подключить файл 2.js (его тоже необходимо создать
// рядом с html-файлом). В js-файле необходимо создать следующий скрипт:
// Cоздать функцию greeting, которая принимает в качестве аргумента имя человека и выводит приветствие, используя
// переданное ей имя, в консоль.
// Необходимо у пользователя запросить имя и вызвать функцию greeting, передав туда полученное от пользователя значение.

function greeting(name="Nemo") {
    console.log(`Hello, ${name}!`);
}

while (true)
    try {
        let name = prompt("Enter your name:");
        if (name.length > 0){
            greeting(name);
            break;
        }
        else throw Error("Empty string.");
    }
    catch (e) {
        alert(e);
        continue;
    }