from src.services import (
    cashback_categories,
    investment_bank,
    search_by_phone,
    search_person_transfers,
    simple_search,
)
from src.utils import read_transactions_from_excel


def main() -> None:
    """
    Основная логика приложения.
    """
    data = read_transactions_from_excel(
        "data/operations.xlsx"
    )

    print(
        "Добро пожаловать в анализатор банковских транзакций"
    )

    print(
        "Выберите сервис:\n"
        "1. Выгодные категории кешбэка\n"
        "2. Инвесткопилка\n"
        "3. Простой поиск\n"
        "4. Поиск по телефонам\n"
        "5. Поиск переводов физлицам"
    )

    choice = input("Введите номер сервиса: ")

    if choice == "1":
        year = int(input("Введите год: "))
        month = int(input("Введите месяц: "))

        print(
            cashback_categories(
                data,
                year,
                month,
            )
        )

    elif choice == "2":
        month_str = input(
            "Введите месяц (YYYY-MM): "
        )

        limit = int(
            input(
                "Введите шаг округления: "
            )
        )

        print(
            investment_bank(
                month_str,
                data,
                limit,
            )
        )

    elif choice == "3":
        search = input(
            "Введите строку поиска: "
        )

        print(
            simple_search(
                data,
                search,
            )
        )

    elif choice == "4":
        print(
            search_by_phone(data)
        )

    elif choice == "5":
        print(
            search_person_transfers(data)
        )

    else:
        print("Неверный выбор")


if __name__ == "__main__":
    main()
