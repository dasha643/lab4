def cart_total(items: list[float | int], discount: float | int = 0) -> float:
    """
    обчислює підсумкову вартість товарів у кошику з урахуванням знижки
    param items: список цін товарів
    param discount: знижка у відсотках (від 0 до 100)
    return: загальна вартість після застосування знижки
    """
    if not isinstance(items, list):
        raise TypeError("товари мають бути надані у вигляді списку")

    if any(not isinstance(price, (int, float)) or price < 0 for price in items):
        raise ValueError("ціна товару не може бути від'ємною або мати нечисловий тип")

    if not (0 <= discount <= 100):
        raise ValueError("знижка повинна бути в межах від 0% до 100%")

    subtotal = sum(items)
    total = subtotal * (1 - discount / 100)
    return round(total, 2)