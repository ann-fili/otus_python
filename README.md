Курс автоматизации тестирования на python

### Примечание
Автотесты 

# Технологии
В проекте используются `python 3.9.0`, `poetry` и `pytest`.

Для работы с `python 3.9.0` можно использовать `pyenv`:
- выполните `pyenv install 3.9.0`
- в папке проекта выполните `pyenv local 3.9.0` и перезапустите терминал

### Запуск
1) один раз в папке проекта выполните `poetry install`
2) для запуска программы нужно активировать окружение `poetry shell` и после просто выполнять скрипты с помощью `pytest`;
3) Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку, например:
`pytest -s -v -m ${markers} ${test.py}`

где `${markers}`:
- smoke
- regression

`${test.py}` нужный скрипт;





