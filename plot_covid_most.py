#!/usr/bin/env python3
import os, sys
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
day = timedelta(1)

REPO = '/home/tom/COVID-19/csse_covid_19_data/csse_covid_19_time_series'
DEATHS = os.path.join(REPO,'time_series_19-covid-Deaths.csv')

Nmost = 10
Ndays = 10
Nhead = 4 # rows to skip at top

data = pd.read_csv(DEATHS)
ts = data.columns[Nhead:]
ts = [str(t).split('/') for t in ts]
dates = [datetime(int(t[2])+2000,int(t[0]),int(t[1])) for t in ts]

data.rename(columns={'Province/State':'state', 'Country/Region':'country'},inplace=True)
data.sort_values(data.columns[-1],ascending=False,inplace=True)

fig, ax = plt.subplots(figsize=(10,6))
plt.xticks(rotation=30)
plt.yscale('log')

for index, row in data.iloc[:Nmost].iterrows():
    cname = row.T[0] if type(row.T[0])==str else row.T[1]
    ax.plot(dates,row.T[Nhead:],'.-', label=cname)

axi = list(plt.axis())
axi[0] = dates[Ndays].toordinal()
axi[1] = dates[-1].toordinal()+0.5
axi[2] = 0.9
plt.axis(axi)

ax.set_ylabel('Number of COVID19 deaths (WHO data)')
ax.legend(loc='upper left')
ax.grid()
fig.tight_layout()
fig.text(0.72,0.945,'Source and updates: tmy.se/covid19')
fig.savefig('./plot_covid_most.png',dpi=90)
