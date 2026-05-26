import json
from datetime import datetime, timedelta
from functools import wraps
from typing import Callable, Optional

import pandas as pd


def save_report(
    filename: str = "report.json",
) -> Callable:
    """
    Декоратор для сохранения отчета в файл.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(
            *args,
            **kwargs,
        ):
            result = func(
                *args,
                **kwargs,
            )

            if isinstance(
                result,
                pd.DataFrame,
            ):
                result.to_json(
                    filename,
                    orient="records",
                    force_ascii=False,
                    indent=4,
                )

            else:
                with open(
                    filename,
                    "w",
                    encoding="utf-8",
                ) as file:
                    json.dump(
                        result,
                        file,
                        ensure_ascii=False,
                        indent=4,
                    )

            return result

        return wrapper

    return decorator


@save_report()
def spending_by_category(
    transactions: pd.DataFrame,
    category: str,
    date: Optional[str] = None,
) -> pd.DataFrame:
    """
    Траты по категории за последние 3 месяца.
    """

    if date:
        end_date = datetime.strptime(
            date,
            "%Y-%m-%d",
        )

    else:
        end_date = datetime.now()

    start_date = end_date - timedelta(
        days=90
    )

    transactions[
        "Дата операции"
    ] = pd.to_datetime(
        transactions[
            "Дата операции"
        ]
    )

    filtered = transactions[
        (
            transactions[
                "Дата операции"
            ]
            >= start_date
        )
        & (
            transactions[
                "Дата операции"
            ]
            <= end_date
        )
        & (
            transactions[
                "Категория"
            ]
            == category
        )
    ]

    return filtered


@save_report(
    "weekday_report.json"
)
def spending_by_weekday(
    transactions: pd.DataFrame,
    date: Optional[str] = None,
) -> pd.DataFrame:
    """
    Средние траты по дням недели.
    """

    transactions[
        "Дата операции"
    ] = pd.to_datetime(
        transactions[
            "Дата операции"
        ]
    )

    transactions[
        "weekday"
    ] = transactions[
        "Дата операции"
    ].dt.day_name()

    return (
        transactions.groupby(
            "weekday"
        )[
            "Сумма платежа"
        ]
        .mean()
        .reset_index()
    )


@save_report(
    "workday_report.json"
)
def spending_by_workday(
    transactions: pd.DataFrame,
    date: Optional[str] = None,
) -> pd.DataFrame:
    """
    Средние траты в будни и выходные.
    """

    transactions[
        "Дата операции"
    ] = pd.to_datetime(
        transactions[
            "Дата операции"
        ]
    )

    transactions[
        "day_type"
    ] = transactions[
        "Дата операции"
    ].dt.weekday.apply(
        lambda x:
        "Выходной"
        if x >= 5
        else "Рабочий"
    )

    return (
        transactions.groupby(
            "day_type"
        )[
            "Сумма платежа"
        ]
        .mean()
        .reset_index()
    )
