#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: loandria <loandria@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/18 23:05:04 by loandria            #+#    #+#            #
#   Updated: 2026/06/15 13:25:49 by loandria           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "Hello" + 5
    else:
        print("Operation completed successfully")


def test_error_types(operation: int) -> None:
    try:
        garden_operations(operation)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


def test_different_errors() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while i <= 4:
        print(f"Testing operation {i}...")
        test_error_types(i)
        i += 1
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_different_errors()
