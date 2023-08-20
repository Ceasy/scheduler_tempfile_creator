
# Проект по созданию временных файлов

Программа создает временный зашифрованный архив с текстовым документом для указаного пользователя, которая позволяет планировать автоматическое удаление этих файлов через указанное время.

## Основные компоненты:
- **gui.py**: Графический интерфейс на базе `tkinter` для ввода данных пользователя.
- **main.py**: Основная точка входа. Проверяет права пользователя и запускает GUI.
- **scheduler.py**: Инструменты для создания задач в планировщике заданий Windows.
- **constants.py**: Константы, используемые в проекте.

## Как использовать:
1. Запустите `main.py` для отображения графического интерфейса.
2. Введите необходимые данные и нажмите "Start".

## Лицензия:

Copyright (c) 2023 Alex Fedotov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Автор:

Alex Fedotov
