from typing import Any

import pandas as pd


def read_transactions_from_excel(
    file_path: str,
) -> list[dict[str, Any]]:
    """
    Считывает транзакции из Excel-файла.
    """
    df = pd.read_excel(file_path)

    records = df.to_dict(orient="records")

    return [
        {
            str(key): value
            for key, value in row.items()
        }
        for row in records
    ]
