import re

def f(dates):
    pattern=r'\d{4}-\d{2}-\d{2}'
    return re.findall(pattern,dates)



dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"
print(f(dates))

dates2 = "2025-01-04,2025-1-04,2025-01-4,2025-01-05"
print(f(dates2))