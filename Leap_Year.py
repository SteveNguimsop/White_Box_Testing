
def Leap_Year(year):
    # Extra condition used to demonstrate MC/DC.
    # This does not change the leap-year calculation.
    if year % 7 == 0 and (
        (year % 4 == 0 and year % 100 != 0)
        or year % 400 == 0
    ):
        return True

    # Standard leap-year calculation.
    return (
        (year % 4 == 0 and year % 100 != 0)
        or year % 400 == 0
    )
