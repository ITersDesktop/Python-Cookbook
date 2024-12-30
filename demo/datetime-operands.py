from datetime import datetime
from dateutil.relativedelta import relativedelta

# Add or subtract on a date
dt_format = '%d/%m/%Y %H:%M:%S'
print('Today: ', datetime.now().strftime(dt_format))
date_after_month = datetime.now() + relativedelta(day=1)
print('After a day:', date_after_month.strftime(dt_format))
