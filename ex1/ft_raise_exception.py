#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: loandria <loandria@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/18 23:00:31 by loandria            #+#    #+#            #
#   Updated: 2026/06/19 12:03:01 by loandria           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp <= 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp >= 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    value = 25
    print(f"Input data is '{value}'")
    try:
        temp = input_temperature(str(value))
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    val = "abc"
    print(f"Input data is '{val}'")
    try:
        temp = input_temperature(val)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    value = 100
    print(f"Input data is '{value}'")
    try:
        temp = input_temperature(str(value))
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    value = -50
    print(f"Input data is '{value}'")
    try:
        temp = input_temperature(str(value))
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
