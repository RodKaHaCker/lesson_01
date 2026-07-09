def is_year_leap(year):
    return year % 4 == 0


year1 = 2028
result1 = is_year_leap(year1)
print(f"год {year1}: {result1}")

year2 = 2025
result2 = is_year_leap(year2)
print(f"год {year2}: {result2}")
