"""Module for computing power sets."""

from typing import Any


def power(x: list[Any]) -> list[list[Any]]:
    """
    Compute the power-set of x.

 

#     Returns the power-set of x as a list of lists.
#     """
    power_set = []

    for i in range(2**len(x)):
        bits = format(i,"b").zfill(len(x))

        subset = [x[j] for j in range(len(bits)) if bits[j] == '1']

        power_set.append(subset)
    
    return power_set


# print(power(['a','b','c']))
