
Описание программы:
-------------------
Программа создает временный зашифрованный архив с текстовым документом для указаного пользователя, которая позволяет
планировать автоматическое удаление этих файлов через указанное время.

Расшифровка GUI:
----------------
1. "Username": Поле для ввода имени пользователя.
2. "Password ZIP": Поле для ввода пароля для архива
3. ".txt file content": Поле для ввода пароля от TrueCrypt пользователя.
4. "ZIP File lifetime(day)": Поле для ввода время жизни ZIP файла, после указаных колличества дней, файл удалится

После ввода данных, программа создает временный файл с этой информацией, так же создает в задачу с помощью планировщика
задачи, которая удалит архив через "n" дней, которое вы указали.
"С помощью встроенного планировщика заданий можно установить автоматическое удаление этого файла через определенный
период времени."

