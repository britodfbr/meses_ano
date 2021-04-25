import numpy as np
import datetime as dt


#DataRanger
dr = np.arange('1979-01', '1980-01', dtype='datetime64[M]')

meses0 = dr
meses1 = [dt.datetime.strptime(x, '%Y-%m').strftime("%b") for x in np.datetime_as_string(dr, timezone='UTC')]
meses2 = [dt.datetime.strptime(x, '%Y-%m').strftime("%B") for x in np.datetime_as_string(dr, timezone='UTC')]
meses3 = [dt.datetime.strptime(x, '%Y-%m').strftime("%Y-%b") for x in np.datetime_as_string(dr, timezone='UTC')]


print(f'''\n\n========\n With numpy\n
{meses0}\n
{meses1}\n
{meses2}\n
{meses3} ''')

a = np.arange('2009-01', '2010-01', dtype='datetime64[M]').astype(dt.datetime)


print(f"""\n\n========\n Forma #2\n
 {[x for x in a]}\n
 {[x.strftime('%F') for x in a]}
 {[x.strftime('%Y-%m') for x in a]}
 {[x.strftime('%Y-%b') for x in a]}
 {[x.strftime('%b') for x in a]}
 {[x.strftime('%B') for x in a]}
  """)


b = np.arange(np.datetime64('2011-01-01'), np.datetime64('2012-01-01'), dtype='datetime64[M]').astype(dt.datetime)
print(f"""\n\n========\n Forma #3\n
 {[x for x in b]}\n
 {[x.strftime('%F') for x in b]}
 {[x.strftime('%Y-%m') for x in b]}
 {[x.strftime('%Y-%b') for x in b]}
 {[x.strftime('%b') for x in b]}
 {[x.strftime('%B') for x in b]}
  """)