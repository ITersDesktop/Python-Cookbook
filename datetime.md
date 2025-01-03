
# How to increment a datetime by adding some days?

There have been several ways to do it.

## Method 1: Using `timedelta` of `datetime` package

For days

```python
from datetime import timedelta, datetime

today = datetime.today().strftime("%Y-%m-%d")
tomorrow = datetime.today() + timedelta(1)
```

For seconds, we can do:

```python
from datetime import datetime, timedelta
date = datetime.now() + timedelta(seconds=[delta_value])
```

Depending on how you import `datetime` package, it could be some variants like

```python
import datetime

datetime.datetime.now() + datetime.timedelta(days=1)
```

Reading more [timedelta](http://docs.python.org/library/datetime.html) objects in the Python docs.

## Method 2: Using `relativedelta` of `python-dateutil` package

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

dt_format = '%d/%m/%Y %H:%M:%S'
print('Today: ', datetime.now().strftime(dt_format))
date_after_month = datetime.now() + relativedelta(day=1)
print('After a day:', date_after_month.strftime(dt_format))
```

Remember: install the required package `pip install python-dateutil` for this method.

# How to extract the year from a Python datetime object?

It's straighforward.

```python
import datetime
year = datetime.date.today().year
year = datetime.datetime.today().year
year = datetime.date.today().year
```

# How to track running time of a program

```python
import time

start = time.time()
# do massive jobs
end = time.time()
print(f"It takes {end-start:.2f} seconds to complete the massive jobs.")
```
