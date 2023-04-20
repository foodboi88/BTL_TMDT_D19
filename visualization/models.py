import time
from datetime import datetime
import plotly.graph_objects as px
import pylab
import numpy as np
from django.db import models

# Create your models here.
import sqlite3
import pandas as pd
import datetime

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg')


conn = sqlite3.connect(
    r"C:\Users\pc\Documents\GitHub\BTL_TMDT_D19\db.sqlite3", check_same_thread=False)


def draw_image():
    # Vẽ biểu đồ cột
    plt.bar(days, count)
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    # filename = save_image()


def save_image():
    # tạo đường dẫn cho file ảnh
    folder_path = 'src/image_visualization/'  # thay đổi đường dẫn cho phù hợp
    filename = int(time.time())
    filename = str(filename)+".png"
    save_path = folder_path+filename
    pylab.savefig(save_path)
    plt.close()
    return filename


def funtion1(start_date="2022-01-17", end_date="2022-04-25"):
    query = f"SELECT * FROM 'core_order' where ordered_date>='{start_date}' and ordered_date<='{end_date}' and ordered='1' order by start_date ASC"
    df = pd.read_sql_query(query, conn)
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    df = df.set_index('ordered_date')
    total_order = df.groupby(pd.Grouper(freq='D')).size()
    days = total_order.keys().to_list()
    count = total_order.values.tolist()

    for i in range(len(days)):
        days[i] = str(pd.Timestamp(days[i]))[0:10]

    # Vẽ biểu đồ cột
    plt.bar(days, count)
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    filename = save_image()

    return filename, days, count


def funtion2(year="2022"):
    start_date = year + "-01-01"
    end_date = year + "-12-31"
    query = f"SELECT * FROM 'core_order' where ordered_date>='{start_date}' and ordered_date<='{end_date}' and ordered='1' order by start_date ASC"
    df = pd.read_sql_query(query, conn)
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])

    df = df.set_index('ordered_date')
    total_order = df.groupby(pd.Grouper(freq='M')).size()
    months = total_order.keys().to_list()
    count = total_order.values.tolist()
    my_dict = {'01': 0, '02': 0, '03': 0,  '04': 0, '05': 0,
               '06': 0,  '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}
    for i in range(len(months)):
        months[i] = str(pd.Timestamp(months[i]))[5:7]
        my_dict[str(months[i])] = count[i]
    plt.bar(my_dict.keys(), my_dict.values())
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    filename = save_image()
    return filename, my_dict


def funtion3(start_year="2019", end_year="2022"):
    start_date = start_year + "-01-01"
    end_date = end_year + "-12-31"
    query = f"SELECT * FROM 'core_order' where ordered_date>='{start_date}' and ordered_date<='{end_date}' and ordered='1' order by start_date ASC"
    df = pd.read_sql_query(query, conn)
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    df = df.set_index('ordered_date')
    total_order = df.groupby(pd.Grouper(freq='Y')).size()
    my_dict = {}
    for i in range(int(start_year), int(end_year)):
        my_dict[str(i)] = 0

    years = total_order.keys().to_list()
    count = total_order.values.tolist()

    for i in range(len(years)):
        years[i] = str(pd.Timestamp(years[i]))[0:4]
        my_dict[str(years[i])] = count[i]

    plt.bar(my_dict.keys(), my_dict.values())
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    filename = save_image()
    return filename, my_dict


def funtion4(start_date="2022-01-01", end_date="2023-01-04", flag='D'):
    query = f"SELECT 'core_order'.'id', 'core_order'.'ordered_date','core_payment'.'amount' FROM 'core_payment', 'core_order' where 'core_order'.'payment_id'='core_payment'.'id' and 'core_order'.'ordered'=1 and 'core_order'.'ordered_date'>='{start_date}' and 'core_order'.'ordered_date'<='{end_date}' order by start_date ASC"
    df = pd.read_sql_query(query, conn)
    # Chuyển đổi trường 'start_date' sang kiểu datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    if flag == 'D' or flag == 'd':
        df['date'] = df['ordered_date'].dt.date
        time_amount = df.groupby('date')['amount'].sum()
    days = time_amount.keys().to_list()
    amount = time_amount.values.tolist()
    for i in range(len(days)):
        days[i] = str(days[i])
    plt.bar(days, amount)
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    filename = save_image()

    return filename, days, amount


def funtion5(year="2022", conn=conn, flag='M'):
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    query = f"SELECT 'core_order'.'id', 'core_order'.'ordered_date','core_payment'.'amount' FROM 'core_payment', 'core_order' where 'core_order'.'payment_id'='core_payment'.'id' and 'core_order'.'ordered'=1 and 'core_order'.'ordered_date'>='{start_date}' and 'core_order'.'ordered_date'<='{end_date}' order by start_date ASC"
    df = pd.read_sql_query(query, conn)
    # Chuyển đổi trường 'start_date' sang kiểu datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])

    df['month'] = df['ordered_date'].dt.month
    time_amount = df.groupby('month')['amount'].sum()

    months = time_amount.keys().to_list()
    amount = time_amount.values.tolist()
    # months=total_order.keys().to_list()
    # count= total_order.values.tolist()
    my_dict = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0,
               '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
    for i in range(len(months)):
        months[i] = str(months[i])
        my_dict[str(months[i])] = amount[i]
    plt.bar(my_dict.keys(), my_dict.values())
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    filename = save_image()

    return filename, my_dict


def funtion6(start_year="2021", end_year="2027", conn=conn):
    start_date = start_year+"-01-01"
    end_date = end_year+"-12-31"
    query = f"SELECT 'core_order'.'id', 'core_order'.'ordered_date','core_payment'.'amount' FROM 'core_payment', 'core_order' where 'core_order'.'payment_id'='core_payment'.'id' and 'core_order'.'ordered'=1 and 'core_order'.'ordered_date'>='{start_date}' and 'core_order'.'ordered_date'<='{end_date}' order by start_date ASC"

    df = pd.read_sql_query(query, conn)
    # Chuyển đổi trường 'start_date' sang kiểu datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    df['year'] = df['ordered_date'].dt.year
    time_amount = df.groupby('year')['amount'].sum()

    my_dict = {}
    for i in range(int(start_year), int(end_year)):
        my_dict[str(i)] = 0
    years = time_amount.keys().to_list()
    amount = time_amount.values.tolist()

    for i in range(len(years)):
        years[i] = str(years[i])
        my_dict[str(years[i])] = amount[i]

    plt.bar(my_dict.keys(), my_dict.values())
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    filename = save_image()

    return filename, my_dict
