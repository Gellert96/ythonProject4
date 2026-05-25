import json
import re
from collections import defaultdict
from math import ceil
from typing import Any


def cashback_categories(
    data: list[dict[str, Any]],
    year: int,
    month: int,
) -> str:
    """
    Анализ выгодных категорий кешбэка.
    """
    result: dict[str, float] = defaultdict(float)

    for item in data:
        date = str(item.get("Дата операции", ""))

        if f"{year}-{month:02}" in date:
            category = str(
                item.get("Категория", "Другое")
            )

            cashback = float(
                item.get("Кешбэк", 0)
            )

            result[category] += cashback

    return json.dumps(
        result,
        ensure_ascii=False,
        indent=4,
    )


def investment_bank(
    month: str,
    transactions: list[dict[str, Any]],
    limit: int,
) -> float:
    """
    Расчёт суммы инвесткопилки.
    """
    total = 0.0

    for item in transactions:
        date = str(item.get("Дата операции", ""))

        if month in date:
            amount = float(
                item.get("Сумма платежа", 0)
            )

            rounded = ceil(
                amount / limit
            ) * limit

            total += rounded - amount

    return round(total, 2)


def simple_search(
    data: list[dict[str, Any]],
    search: str,
) -> str:
    """
    Простой поиск по описанию и категории.
    """
    result = [
        item
        for item in data
        if search.lower()
        in str(
            item.get("Описание", "")
        ).lower()
        or search.lower()
        in str(
            item.get("Категория", "")
        ).lower()
    ]

    return json.dumps(
        result,
        ensure_ascii=False,
        indent=4,
    )


def search_by_phone(
    data: list[dict[str, Any]],
) -> str:
    """
    Поиск транзакций по номеру телефона.
    """
    pattern = re.compile(
        r"(\+7|8)[\s\-()]?\d{3}[\s\-()]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"
    )

    result = [
        item
        for item in data
        if pattern.search(
            str(item.get("Описание", ""))
        )
    ]

    return json.dumps(
        result,
        ensure_ascii=False,
        indent=4,
    )


def search_person_transfers(
    data: list[dict[str, Any]],
) -> str:
    """
    Поиск переводов физическим лицам.
    """
    pattern = re.compile(
        r"[А-ЯЁ][а-яё]+\s[А-ЯЁ]\."
    )

    result = [
        item
        for item in data
        if item.get("Категория") == "Переводы"
        and pattern.search(
            str(item.get("Описание", ""))
        )
    ]

    return json.dumps(
        result,
        ensure_ascii=False,
        indent=4,
    )
