def is_leap_year(year):

    is_leap_year = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
	    
    return is_leap_year
    
print(is_leap_year(2024))
print(is_leap_year(2025))
