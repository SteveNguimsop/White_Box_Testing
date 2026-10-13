
def Leap_Year(year):
    if year % 4 != 0:
        return False

    if year % 100 == 0:
        if year % 400 != 0:
            return False
    else:
        return True

    return True
