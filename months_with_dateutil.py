import datetime as dt
from dateutil.relativedelta import relativedelta
# for another language configure locale.
#import locale
#locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


meses0 = [(dt.datetime(2020,1,1)+relativedelta(months=+x)).strftime("%Y-%m") for x in range(12)]

meses1 = [(dt.datetime.now()+relativedelta(months=+x)).strftime("%B") for x in range(12)]

meses2 = [(dt.datetime.now()+relativedelta(months=+x)).strftime("%b") for x in range(12)]

meses3 = [(dt.datetime.now()+relativedelta(months=+x)).strftime("%Y-%b") for x in range(12)]

print(f'''\n\n========\n With dateutil\n
{meses0}\n
{meses1}\n
{meses2}\n
{meses3} ''')