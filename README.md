# Мой учебный проект Python

## Описание:

Проект "Homework_GH" - это учебный проект на Python, содержащий последовательность выполнения домашних задач, 
начиная с раздела "2. Разработка на Python.". Редактирование содержания проекта сторонними пользователями не предусмотрено.

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/Skurudge/skuru-rep-01.git
```

## Использование:

1. Перейдите на страницу в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.
3. На данном этапе развития проекта можно ознакомиться с разработанными функциями. 

### Разработанные функции:

- Разработана функция [get_mask_card_number](src/masks.py), 
которая принимает на вход 16-ти значный номер карты в виде числа и возвращает ее маску:
```
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
```

- Разработана функция [get_mask_account](src/masks.py), 
которая принимает на вход 20-ти значный номер счета в виде числа и возвращает его маску:
```
73654108430135874305  # входной аргумент
**4305  # выход функции
```

- Разработана функция [mask_account_card](src/widget.py), 
которая принимает на вход строку с типом и номером карты или счета и возвращает строку с замаскированным номером:
```
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```

- Разработана функция [get_date](src/widget.py), 
которая принимает строку с датой в исходном формате, возвращает строку с датой в формате ДД.ММ.ГГГГ:
```
# Пример исходного формата даты
"2024-03-11T02:26:18.671407"
 
# Пример формата даты на выходе
"11.03.2024" 
```
 
- Разработана функция [filter_by_state](src/processing.py), 
которая принимает список словарей и опционально значение для ключа 'state', возвращает новый список словарей, 
содержащий словари с опциональным значением ключа 'state'.
- Разработана функция [sort_by_date](src/processing.py), 
которая принимает список словарей и необязательный параметр, задающий порядок сортировки словарей по дате (по умолчанию - убывание), 
возвращает новый список словарей, отсортированный по дате.

Перечисленные функции будут использованы далее при развитии проекта.

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](README.md).
