def convert_from_celsius_to_fahrenheit(value):
    return (value * 1.8) + 32

def get_diff(diff_current_f_and_target_c_converted):
    if diff_current_f_and_target_c_converted == 0:
        return "Hold"
    elif diff_current_f_and_target_c_converted < 0:
        diff_current_f_and_target_c_converted *= -1
        return f"Cool: {diff_current_f_and_target_c_converted:.1f} degrees Fahrenheit"
    elif diff_current_f_and_target_c_converted > 0:
        return f"Heat: {diff_current_f_and_target_c_converted:.1f} degrees Fahrenheit"


def adjust_thermostat(current_f, target_c):

    target_c_converted = convert_from_celsius_to_fahrenheit(target_c)

    res = get_diff(target_c_converted - current_f)

    return res


print(adjust_thermostat(72, 18))