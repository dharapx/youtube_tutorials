#  Date: 3/7/21, 12:28 PM
#  Author: dharapx
#  Feel free to use this code to try on your own

"""
Python added the enum module to the standard library in version 3.4 as new data type.
An enumeration is a set of symbolic names bound to unique, constant values.
Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
"""

from enum import Enum


class Jubilee(Enum):
    silver: int = 25
    golden: int = 50
    platinum: int = 70
    # ruby: int = 70  # you won't be able use this because this class will not consider ruby as a member unless
    # it has an unique value
    # platinum: str = "70" # can not have duplicate key even if you changed the type


if __name__ == "__main__":
    print(Jubilee.platinum)
    print(Jubilee.ruby)
    print(Jubilee(25))
    print(dir(Jubilee))

    # Aother way to create ENUM
    # you can use space separated string, list or tuple with Enum class without extending.
    # And value will be auto incremented starting from 1.
    ses = Enum('Season', 'summer monsoon winter')
    # ses = Enum("Season", ["summer", "winter", "monsoon"])
    # ses = Enum("Season", ("summer", "winter", "monsoon"))
    print(dir(ses))
    print(ses.__members__)
    print(ses(1))

    # Iteration
    for y in ses:
        print(y)
        # Also separate value or name can also be accessed using “name” or “value” keyword.
        print(y.name)
        print(y.value)

    # Identity :- These are checked using keywords “is” and “is not“.
    if ses(1) is not ses.monsoon:
        print(ses(1).name)

    # Equality :- Equality comparisons of “==” and “!=” types are also supported.
    if ses.summer.value == 1:
        print("It's correct")



