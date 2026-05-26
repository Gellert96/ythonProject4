from src.utils import read_transactions_from_excel


def test_read_transactions_from_excel():
    data = read_transactions_from_excel(
        "data/operations.xlsx"
    )

    assert isinstance(data, list)
