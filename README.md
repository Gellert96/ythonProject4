# PythonProject4

Проект для обработки банковских операций из Excel-файла.

## Описание

Приложение читает данные из файла `data/operations.xlsx` и предоставляет функции для анализа операций.

## Структура проекта

```text
src/
    utils.py
    services.py
    main.py

tests/
    test_utils.py
    test_services.py

data/
README.md
pyproject.toml
```

## Установка

```bash
poetry install
```

## Запуск тестов

```bash
pytest
```

## Проверка стиля кода

```bash
flake8 .
```

## Используемые технологии

- Python 3.14
- Poetry
- pytest
- flake8