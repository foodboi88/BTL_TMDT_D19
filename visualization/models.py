from django.db import models

# Create your models here.
import sqlite3
import pandas as pd
import datetime

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas as pd
import plotly.graph_objects as px

conn = sqlite3.connect("E:\BTL_TMDT_D19\db.sqlite3")


def funtion1(start_date="2022-01-17", end_date="2022-04-25", conn=conn):
    query = f"SELECT * FROM 'core_order' where ordered_date>='{start_date}' and ordered_date<='{end_date}' and ordered='1' order by start_date ASC"
    df = pd.read_sql_query(query, conn)
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    df = df.set_index('ordered_date')
    total_order = df.groupby(pd.Grouper(freq='D')).size()
    days = total_order.keys().to_list()
    count = total_order.values.tolist()

    for i in range(len(days)):
        days[i] = str(pd.Timestamp(days[i]))[0:10]
    return days, count


# days,count=funtion1()
