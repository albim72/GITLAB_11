def calculate_discount(price, percentage):
    if percentage < 0 or percentage > 50:
        raise ValueError("Discount must be between 0 and 50%")
    return price * (1 - percentage / 100)
