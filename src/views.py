import json
from datetime import datetime
from typing import Any


def get_greeting(date_time: str) -> str:
    """
    Возвращает приветствие в зависимости от времени суток.
    """
    hour = datetime.strptime(
        date_time,
        "%Y-%m-%d %H:%M:%S",
    ).hour

    if 6 <= hour <= 11:
        return "Доброе утро"

    elif 12 <= hour <= 17:
        return "Добрый день"

    elif 18 <= hour <= 22:
        return "Добрый вечер"

    else:
        return "Доброй ночи"


def get_top_transactions(
    data: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Возвращает топ-5 транзакций по сумме.
    """
    sorted_data = sorted(
        data,
        key=lambda x: abs(
            float(
                x.get(
                    "Сумма платежа",
                    0,
                )
            )
        ),
        reverse=True,
    )

    return sorted_data[:5]


def home_page(
    date_time: str,
    data: list[dict[str, Any]],
) -> str:
    """
    JSON для страницы Главная.
    """
    result = {
        "greeting": get_greeting(
            date_time
        ),
        "top_transactions": get_top_transactions(
            data
        ),
    }

    return json.dumps(
        result,
        ensure_ascii=False,
        indent=4,
    )
