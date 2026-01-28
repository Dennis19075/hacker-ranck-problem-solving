import re

def extract_value(value):
    if "$" in value:
        return float(value.replace('$', ''))
    elif "%" in value:
        return float(value.replace('%', '')) * 0.01

def refactor_tip_to_string(tip):
    return f"${tip:.2f}"

def calculate_tips(meal_price, custom_tip):
    res = []

    first_tip = extract_value("15%")
    second_tip = extract_value("20%")
    third_tip = extract_value(custom_tip)
    meal_price_value = extract_value(meal_price)

    first_tip_price = first_tip * meal_price_value
    second_tip_price = second_tip * meal_price_value
    third_tip_price = third_tip * meal_price_value

    return [
        refactor_tip_to_string(first_tip_price), 
        refactor_tip_to_string(second_tip_price), 
        refactor_tip_to_string(third_tip_price)
    ]

print(calculate_tips("$10.00", "25%"))