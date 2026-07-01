#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: loandria <loandria@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/18 23:13:54 by loandria            #+#    #+#            #
#   Updated: 2026/06/15 13:26:29 by loandria           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, messag: str = "Unknown garden error") -> None:
        super().__init__(messag)


class PlantError(GardenError):
    def __init__(self, messag: str = "Unknown plant error") -> None:
        super().__init__(messag)


class WaterError(GardenError):
    def __init__(self, messag: str = "Unknown water error") -> None:
        super().__init__(messag)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
