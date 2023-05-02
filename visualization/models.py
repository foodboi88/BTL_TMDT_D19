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
    r"db.sqlite3", check_same_thread=False)


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

    plt.plot(days,count, "r-",marker=".")
    plt.xticks(range(len(days)), days, rotation=90)
    plt.title('Biểu đồ hiển thị số lượng hóa đơn theo ngày')
    plt.xlabel("Ngày")
    plt.ylabel("Số lượng")
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
    plt.xlabel('Tháng')
    plt.ylabel('Số lượng hóa đơn')
    plt.title("Biểu đồ thể hiện số lượng hóa đơn theo tháng trong năm")
     # Đặt số cột trên đỉnh các cột
    for i, v in enumerate(my_dict.values()):
        plt.text(i, v + 1, str(v), ha='center', fontsize=10)

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
    plt.xlabel('Năm')
    plt.ylabel('Số lượng hóa đơn')
    plt.title(f"Biểu đồ thể hiện số lượng hóa đơn theo các năm {start_year} đến {end_year}")
    for i, v in enumerate(my_dict.values()):
        plt.text(i, v + 1, str(v), ha='center', fontsize=10)

    filename = save_image()
    return filename, my_dict




def funtion4(start_date="2022-01-01", end_date="2022-01-05", flag='D'):
    query = f"SELECT 'core_order'.'id', 'core_order'.'ordered_date','core_payment'.'amount' FROM 'core_payment', 'core_order' where 'core_order'.'payment_id'='core_payment'.'id' and 'core_order'.'ordered'=1 and 'core_order'.'ordered_date'>='{start_date}' and 'core_order'.'ordered_date'<='{end_date}' order by start_date ASC"
    df = pd.read_sql_query(query, conn)
    # Chuyển đổi trường 'start_date' sang kiểu datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    # print(df)
    if flag == 'D' or flag == 'd':
        df['date'] = df['ordered_date'].dt.date
        time_amount = df.groupby('date')['amount'].sum()
    days = time_amount.keys().to_list()
    amount = time_amount.values.tolist()
    for i in range(len(days)):
        days[i] = str(days[i])
    # print(f"count: {len()}")
    plt.plot(days,amount, "r-",marker=".")
    plt.title(f"Biểu đồ thể hiện doanh thu từ hóa đơn theo ngày {start_date} đến {end_date}")
    plt.xlabel("Ngày")
    plt.ylabel("Doanh thu")
    filename = save_image()

    return filename, days, amount




def funtion5(year="2022", flag='M'):
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
    plt.title(f"Biểu đồ thể hiện doanh thu từ hóa đơn theo các tháng trong năm {year}")
    plt.xlabel('Tháng')
    plt.ylabel('Doanh thu') 


    filename = save_image()

    return filename, my_dict





def funtion6(start_year="2022", end_year="2023"):
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
    plt.title(f"BIỂU ĐỒ THÊ HIỆN DOANH THU TỪ HÓA ĐƠN THEO NĂM {start_year} đến {end_year}")
    plt.xlabel('Năm')
    plt.ylabel('Doanh thu')
    # for i, v in enumerate(my_dict.values()):
    #     plt.text(i, v + 1, str(v), ha='center', fontsize=10)


    filename = save_image()

    return filename, my_dict





def funtion7(year="2023"):
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    # print(start_date)
    query = f"select core_order.id, ordered_date,ordered, amount from core_order, core_payment where ordered_date>='{start_date}' and ordered_date<='{end_date}' and core_order.payment_id=core_payment.id"
    df = pd.read_sql(query, conn)
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    df['order_date'] = df['ordered_date'].dt.month

    # Thống kê số lượng ordered bằng 1 và 0 theo ngày
    order_summary = df.groupby(['order_date', 'ordered'])[
        'id'].count().reset_index()
    order_summary_pivot = pd.pivot_table(
        order_summary, values='id', index='order_date', columns='ordered', fill_value=0)
    # print(f"order_summary_pivot: {order_summary_pivot}")
    my_dict_0 = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0,
                 '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
    my_dict_1 = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0,
                 '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
    for o in range(len(order_summary_pivot)):
      # print(f"order_summary_pivot.index[o]: {type(str(order_summary_pivot.index[o]))}")
      my_dict_0[str(order_summary_pivot.index[o])] = order_summary_pivot[0].values[o] +order_summary_pivot[1].values[o]
      my_dict_1[str(order_summary_pivot.index[o])] = order_summary_pivot[1].values[o]

    X = my_dict_0.keys()
    order_date = my_dict_0.values()
    ordered = my_dict_1.values()
    X_axis = np.arange(len(X))
    plt.bar(X_axis - 0.2, order_date, 0.4, label='Đơn hàng')
    plt.bar(X_axis + 0.2, ordered, 0.4, label='Hóa đơn')
    plt.xticks(X_axis, X)
    plt.xlabel("Tháng")
    plt.ylabel("Số lượng")
    plt.title(f"Biểu đồ thể hiện số lượng đơn đặt hàng và hóa đơn theo các tháng trong năm {year}")
    plt.legend()
    filename = save_image()
    return filename, my_dict_0, my_dict_1





def funtion8(year="2023"):
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    query = f"select core_order.id, ordered_date,ordered, amount from core_order, core_payment where ordered_date>='{start_date}' and ordered_date<='{end_date}' and core_order.payment_id=core_payment.id"
    df = pd.read_sql(query, conn)
    # Chuyển đổi cột "ordered_date" sang định dạng datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    df['month'] = df['ordered_date'].dt.month
    # Nhóm dữ liệu theo "year" và "ordered" và tính tổng số đơn hàng và tổng số tiền
    result = df.groupby(['month', 'ordered']).agg(
        {'ordered': 'count', 'amount': 'sum'})
    result = result.rename(columns={'ordered': 'count'})
    months = result.index.get_level_values('month').unique().tolist()
    revenues_ordered_0 = result[result.index.get_level_values(
        'ordered') == 0]['amount'].groupby('month').sum().tolist()
    revenues_ordered_1 = result[result.index.get_level_values(
        'ordered') == 1]['amount'].groupby('month').sum().tolist()
    my_dict_0 = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0,
                 '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
    my_dict_1 = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0,
                 '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}

    for i in range(len(months)):
        months[i] = str(months[i])
        my_dict_0[str(months[i])] = revenues_ordered_0[i]
        my_dict_1[str(months[i])] = revenues_ordered_1[i]
    X = my_dict_0.keys()
    order_date = my_dict_0.values()
    ordered = my_dict_1.values()

    plt.plot(my_dict_0.keys(),order_date, "r-",marker=".")
    plt.plot(my_dict_0.keys(),ordered, "b--",marker=".")
    plt.legend(["đơn hàng chưa thanh toán","hóa đơn"])
    plt.xlabel("Tháng")
    plt.ylabel("Doanh thu")
    plt.title(f"Biểu đồ thể hiện số lượng đơn hàng chưa thanh toán và hóa đơn {year}")
    filename = save_image()

    return filename, my_dict_0, my_dict_1



def funtion9(year="2021", quantity=5):
    import json
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    query = f"""SELECT core_item.title, SUM(core_orderitem.quantity) AS total_quantity
            FROM core_order_items
            INNER JOIN core_orderitem ON core_orderitem.id = core_order_items.orderitem_id
            INNER JOIN core_item ON core_orderitem.item_id = core_item.id
            INNER JOIN core_order ON core_order.id = core_order_items.order_id
            WHERE core_order.ordered_date BETWEEN '{start_date}' AND '{end_date}'
            AND core_order.ordered= '1'
            GROUP BY core_item.title
            ORDER BY total_quantity DESC
            LIMIT {quantity};
        """
    df = pd.read_sql(query, conn)
    df = df.reset_index(drop=True)
    title = df["title"].to_list()
    total_quantity = df["total_quantity"].to_list()
    my_dict = {key: value for key, value in zip(title, total_quantity)}
    title = my_dict.keys()
    total_quantity = my_dict.values()
    explode = [0.1]*len(title)

    plt.pie(total_quantity, explode=explode, labels=title,
            autopct='%1.1f%%', startangle=0,
            wedgeprops={"edgecolor": "white",
                        'linewidth': 5,
                        'antialiased': True})
    plt.title(f"Biểu đồ thể hiện top {quantity} sản phẩm bán chạy trong năm {year}")
    plt.axis('equal')

    filename = save_image()

    return filename, my_dict



def funtion10(year="2023", quantity=5):
    import json
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    query = f"""SELECT core_item.label, SUM(core_orderitem.quantity) AS total_quantity
            FROM core_order_items
            INNER JOIN core_orderitem ON core_orderitem.id = core_order_items.orderitem_id
            INNER JOIN core_item ON core_orderitem.item_id = core_item.id
            INNER JOIN core_order ON core_order.id = core_order_items.order_id
            WHERE core_order.ordered_date BETWEEN '{start_date}' AND '{end_date}'
            AND core_order.ordered= '1'
            GROUP BY core_item.title
            ORDER BY total_quantity DESC
            LIMIT {quantity};
        """
    df = pd.read_sql(query, conn)
    df = df.reset_index(drop=True)
    title = df["label"].to_list()
    total_quantity = df["total_quantity"].to_list()
    my_dict = {key: value for key, value in zip(title, total_quantity)}
    title = my_dict.keys()
    total_quantity = my_dict.values()
    print(title , total_quantity)
    explode = [0.1]*len(title)
    plt.pie(total_quantity, explode=explode, labels=title,
            autopct='%1.1f%%', startangle=0,
            wedgeprops={"edgecolor": "white",
                        'linewidth': 5,
                        'antialiased': True})
    plt.axis('equal')
    plt.title(f"Biểu đồ thể hiện top 5 thương hiệu nổi bật {year}")
    filename = save_image()
    return filename, my_dict



def funtion11(year="2021", quantity=20):
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    query = f"""
        select core_order.ordered_date, user_id, auth_user.username, auth_user.first_name, auth_user.last_name from core_order 
        inner join auth_user on core_order.user_id=auth_user.id 
        where ordered_date BETWEEN '{start_date}' and '{end_date}' and is_staff='0' and is_active='1' and ordered='1'
        """
    df = pd.read_sql(query, conn)
    # Đếm số lần xuất hiện của mỗi giá trị trong cột user_id
    top_users = df['user_id'].value_counts().head(quantity).index
    user_counts = df['user_id'].value_counts().head(quantity)
    # Lấy thông tin của 5 khách hàng xuất hiện nhiều nhất trong bảng
    result = df.loc[df['user_id'].isin(top_users), [
        'user_id', 'username', 'first_name', 'last_name']].drop_duplicates()
    result = result.reset_index(drop=True)
    dict_data = result.to_dict(orient='records')
    userid, counts, username = [], [], []
    # Thêm số lần xuất hiện của từng user vào dict_data
    for i, user in enumerate(dict_data):
        user_id = user['user_id']
        userid.append(user_id)
        counts.append(user_counts[user_id])
        username.append(user['username'])
    my_dict = {key: value for key, value in zip(username, counts)}
    from wordcloud import WordCloud
    wc = WordCloud(margin=5, width=900, height=600, background_color='white')
    wc.generate_from_frequencies(my_dict)
    plt.figure(figsize=(10, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.title(f"Biểu đồ thể hiện {quantity} khách hàng tiềm năng trong năm {year}")
    plt.axis('off')
    filename = save_image()
    return filename, my_dict





def funtion12(year="2022", quantity=10):
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    query = f"""SELECT core_payment.user_id,core_payment.amount , auth_user.username, auth_user.first_name, auth_user.last_name, core_order.ordered_date  FROM 'core_payment' 
            inner join auth_user on auth_user.id=core_payment.user_id
            inner join core_order on core_order.payment_id=core_payment.id
            where core_order.ordered_date between '{start_date}' and '{end_date}' and ordered='1';"""
    df = pd.read_sql(query, conn)
    # Nhóm các hàng cùng user_id và tính tổng amount
    grouped = df.groupby('user_id').agg({'amount': 'sum'}).reset_index()

    # Tìm ra 5 khách hàng có tổng amount lớn nhất
    top_5 = grouped.nlargest(quantity, 'amount')

    # Lấy ra thông tin user_id, username, first_name, last_name của các khách hàng đó
    result = df.loc[df['user_id'].isin(top_5['user_id'])][[
        'user_id', 'username', 'first_name', 'last_name']].drop_duplicates()
    result = result.merge(top_5, on='user_id').sort_values(
        by='amount', ascending=False)
    result = result.reset_index(drop=True)

    data_result = result[['username', 'amount']]
    username = list(data_result['username'])
    amount = list(data_result['amount'])
    my_dict = {key: value for key, value in zip(username, amount)}

    from wordcloud import WordCloud
    wc = WordCloud(margin=5, width=900, height=600, background_color='white')
    wc.generate_from_frequencies(my_dict)
    plt.figure(figsize=(10, 6))
    plt.title(f"Biểu đồ thể hiện {quantity} khách hàng chi tiêu trong năm {year}")
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    filename = save_image()
    return filename, my_dict
