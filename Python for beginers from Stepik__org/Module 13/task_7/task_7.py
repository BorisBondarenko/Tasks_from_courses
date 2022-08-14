from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_days(mon):
    date_ = datetime.strptime(f'2021.{mon}.01', '%Y.%m.%d').date()
    last_date = date_ + relativedelta(months=1)
    return (last_date - date_).days


num = int(input())
print(get_days(num))
