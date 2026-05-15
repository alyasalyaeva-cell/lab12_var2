import re

def validate_oms_regex(policy: str) -> bool:
    """Функция валидации ОМС (16 цифр)."""
    return bool(re.match(r"^\d{16}$", policy))

if __name__ == "__main__":
    # Набор тестовых данных
    test_cases = {
        "1234567890123456": True,   # Валидный: 16 цифр
        "9999888877776666": True,   # Валидный
        "123456789012345": False,   # Невалидный: 15 цифр
        "12345678901234567": False,  # Невалидный: 17 цифр
        "1234567890abc456": False,  # Невалидный: буквы
        "                ": False,  # Невалидный: пробелы
        "": False                    # Невалидный: пусто
    }

    print("--- Тестирование регулярного выражения ОМС ---")
    for oms, expected in test_cases.items():
        result = validate_oms_regex(oms)
        status = "Пройден" if result == expected else "ОШИБКА"
        print(f"ОМС: {oms} | Ожидание: {expected} | Результат: {result} | [{status}]")