import re
PENSIONER_DISCOUNT = 0.2

def calculate_appointment_price(base_price: float, has_discount: bool) -> float:
    if base_price < 0: raise ValueError("Price < 0")
    m = (1 - PENSIONER_DISCOUNT) if has_discount else 1.0
    return round(base_price * m, 2)

def validate_oms_regex(policy: str) -> bool:
    return bool(re.match(r"^\d{16}$", policy))