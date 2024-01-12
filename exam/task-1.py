def date_valid(date, month, year):

    isDateValid = bool
    isMonthValid = bool
    isYearValid = bool

    if 1 <= date <= 31:
        isDateValid = True
    else:
        isDateValid = False

    if 1 <= month <= 12:
        isMonthValid = True
    else:
        isMonthValid = False

    if 1 <= year <= 10000:
        isYearValid = True
    else:
        isYearValid = False

    answer = isDateValid & isMonthValid & isYearValid

    return answer