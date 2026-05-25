import json

from src.services import (
    cashback_categories,
    investment_bank,
    search_by_phone,
    search_person_transfers,
    simple_search,
)


sample_data = [
    {
        "Дата операции": "2024-01-15",
        "Категория": "Супермаркеты",
        "Кешбэк": 10,
        "Сумма платежа": 1712,
        "Описание": "Пятёрочка",
    },
    {
        "Дата операции": "2024-01-20",
        "Категория": "Переводы",
        "Кешбэк": 5,
        "Сумма платежа": 500,
        "Описание": "Сергей А.",
    },
    {
        "Дата операции": "2024-01-22",
        "Категория": "Связь",
        "Кешбэк": 2,
        "Сумма платежа": 300,
        "Описание": "МТС +7 921 111-22-33",
    },
]


def test_cashback_categories() -> None:
    result = cashback_categories(sample_data, 2024, 1)

    data = json.loads(result)

    assert "Супермаркеты" in data


def test_investment_bank() -> None:
    result = investment_bank(
        "2024-01",
        sample_data,
        50,
    )

    assert result > 0


def test_simple_search() -> None:
    result = simple_search(
        sample_data,
        "Пятёрочка",
    )

    data = json.loads(result)

    assert len(data) == 1


def test_search_by_phone() -> None:
    result = search_by_phone(sample_data)

    data = json.loads(result)

    assert len(data) == 1


def test_search_person_transfers() -> None:
    result = search_person_transfers(sample_data)

    data = json.loads(result)

    assert len(data) == 1
