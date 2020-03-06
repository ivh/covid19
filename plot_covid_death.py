#!/usr/bin/env python3
import os, sys
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
day = timedelta(1)

REPO = '2019-nCoV/csse_covid_19_data/csse_covid_19_time_series'
CASES = os.path.join(REPO,'time_series_19-covid-Deaths.csv')

cases = pd.read_csv(CASES)
ts = cases.columns[4:]
ts = [str(t).split('/') for t in ts]
dates = [datetime(int(t[2])+2000,int(t[0]),int(t[1])) for t in ts]

cases.rename(columns={'Province/State':'state', 'Country/Region':'country'},inplace=True)

SK=cases[cases.country=='South Korea'].T[4:]
F=cases[cases.country=='France'].T[4:]
G=cases[cases.country=='Germany'].T[4:]
S=cases[cases.country=='Sweden'].T[4:]
I=cases[cases.country=='Italy'].T[4:]


deltaF = 12
deltaG = 12
deltaS = 16
deltaI = 4

fig = plt.Figure(figsize=(10,6))
#fig.autofmt_xdate(rotation=30)
plt.xticks(rotation=30)
plt.yscale('log')
plt.plot(dates,SK,'-o', label='S.Korea')
plt.plot([date-deltaI*day for date in dates],I,'-o', label='Italy -%d days'%deltaI)
plt.plot([date-deltaF*day for date in dates],F,'-o', label='France -%d days'%deltaF)
plt.plot([date-deltaG*day for date in dates],G,'-o', label='Germany -%d days'%deltaG)
plt.plot([date-deltaS*day for date in dates],S,'-o', label='Sweden -%d days'%deltaS)

ax = list(plt.axis())
ax[0] = dates[20].toordinal()
plt.axis(ax)

plt.ylabel('Number of COVID19 cases (WHO data)')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
