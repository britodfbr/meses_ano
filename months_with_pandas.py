import pandas as pd
import datetime


dRan = pd.date_range(start ='2021-01-01', end ='2021-12-31', periods = 12)   

res0 = dRan.strftime('%F')
res1 = dRan.strftime('%Y-%m')
res2 = dRan.strftime('%b')
res3 = dRan.strftime('%B')

print(f'''\n\n========\n With pandas\n
{res0}\n
{res1}\n
{dRan.strftime('%Y-%b')}\n
{res2}\n
{res3} ''')