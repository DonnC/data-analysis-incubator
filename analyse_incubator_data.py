import pandas as pd
import numpy as np
import os
import sys
import time
import datetime
from datetime import datetime as dt


# read csv data into pandas dataframe
df = pd.read_csv("incubator_report.csv")

# save now-datetime-object
dnow = dt.now()
past3 = str(dnow - datetime.timedelta(days=3))
past7 = str(dnow - datetime.timedelta(days=7))
past30 = str(dnow - datetime.timedelta(days=30))

# if hatchRate is > 80 and < 55, lets take a look at records
# for the past 3, 7 & 30 days
# look by phone number | birdType [coz its unique] than name

'''
   # df filtering data
   df[(df.salt >= 50) & (df.eggs < 200)]
   df[(df.salt >= 50) | (df.eggs < 200)]
'''
def data3(btype, rate, contact=None, allOf=False):
    df3 = df.copy()     # make a copy to avoid messing the original
    chunk = df3[(df3['DateAdded'] <= past3) & (df3['BirdType'] == btype) & (df3['HatchRate(%)'] <= rate)]

    if len(chunk) != 0:
        if len(chunk) > 5 and allOf:
            print("[INFO] Returning all found data of the past 3 days")
            return chunk

        elif len(chunk) > 5 and allOf == False:
            print("[INFO] Returning first 5 found data of the past 3 days")
            return chunk.head()

        else:
            print("[INFO] Results found")
            return chunk

    else:
        print("[DEBUG] Could not find any data for the past 3 days")

def data7(btype, rate, contact=None, allOf=False):
    df7 = df.copy()     # make a copy to avoid messing the original
    chunk = df7[(df7['DateAdded'] <= past7) & (df7['BirdType'] == btype) & (df7['HatchRate(%)'] <= rate)]

    if len(chunk) != 0:
        if len(chunk) > 5 and allOf:
            print("[INFO] Returning all found data for the past week")
            return chunk

        elif len(chunk) > 5 and allOf == False:
            print("[INFO] Returning first 5 found data for the past week")
            return chunk.head()

        else:
            print("[INFO] Results found")
            return chunk

    else:
        print("[DEBUG] Could not find any data for the past week")

def data30(btype, rate, contact=None, allOf=False):
    df30 = df.copy()     # make a copy to avoid messing the original
    chunk = df30[(df30['DateAdded'] <= past30) & (df30['BirdType'] == btype) & (df30['HatchRate(%)'] <= rate)]

    if len(chunk) != 0:
        if len(chunk) > 5 and allOf:
            print("[INFO] Returning all found data for the past month")
            return chunk

        elif len(chunk) > 5 and allOf == False:
            print("[INFO] Returning first 5 found data for the past month")
            return chunk.head()

        else:
            print("[INFO] Results found")
            return chunk
    else:
        print("[DEBUG] Could not find any data for the past month")
        return chunk

f = data3('broiler', 80)
print(f)
