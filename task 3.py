
from datetime import datetime

def get_date_in_format(date):

    formatted_date = date.strftime("%d.%m.%Y")
    return formatted_date

my_date = datetime(2023, 10, 23)
result = get_date_in_format(my_date)
print(result)