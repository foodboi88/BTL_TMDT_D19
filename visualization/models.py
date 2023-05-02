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


# Hàm truy vấn cơ sở dữ liệu để lấy các đơn hàng trong khoảng thời gian từ start_date đến end_date.
# Truy vấn được sắp xếp theo thứ tự tăng dần của ordered_date.
# Hàm trả về tên file của biểu đồ, danh sách các ngày trong khoảng thời gian và danh sách các số lượng đơn hàng theo ngày.
def funtion1(start_date="2022-01-17", end_date="2022-04-25"):
    
    # Tạo câu truy vấn để lấy các đơn hàng từ cơ sở dữ liệu
    query = f"SELECT * FROM 'core_order' where ordered_date>='{start_date}' and ordered_date<='{end_date}' and ordered='1' order by start_date ASC"
    
    # Đọc dữ liệu từ câu truy vấn và lưu vào dataframe
    df = pd.read_sql_query(query, conn)
    
    # Chuyển kiểu dữ liệu của ordered_date sang kiểu datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    
    # Đặt ordered_date làm index cho dataframe
    df = df.set_index('ordered_date')
    
    # Tính tổng số lượng đơn hàng trong mỗi ngày bằng cách nhóm các đơn hàng theo ngày
    total_order = df.groupby(pd.Grouper(freq='D')).size()
    
    # Lấy danh sách các ngày và danh sách các số lượng đơn hàng theo ngày
    days = total_order.keys().to_list()
    count = total_order.values.tolist()

    # Chuyển các giá trị trong danh sách days sang định dạng chuỗi
    for i in range(len(days)):
        days[i] = str(pd.Timestamp(days[i]))[0:10]

    # Vẽ biểu đồ cột sử dụng matplotlib
    plt.bar(days, count)
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    
    # Lưu biểu đồ vào tệp hình ảnh và trả về tên file
    filename = save_image()

    return filename, days, count
	


# Định nghĩa hàm function2 với tham số year mặc định là 2022
def funtion2(year="2022"):
    # Khởi tạo start_date và end_date từ year được truyền vào
    start_date = year + "-01-01"
    end_date = year + "-12-31"

    # Xây dựng câu lệnh SQL để lấy dữ liệu các đơn hàng trong năm được chỉ định
    query = f"SELECT * FROM 'core_order' where ordered_date>='{start_date}' and ordered_date<='{end_date}' and ordered='1' order by start_date ASC"

    # Thực hiện truy vấn và đưa kết quả vào dataframe df
    df = pd.read_sql_query(query, conn)

    # Chuyển cột ordered_date sang định dạng datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])

    # Đặt cột ordered_date làm index và nhóm các đơn hàng theo tháng
    df = df.set_index('ordered_date')
    total_order = df.groupby(pd.Grouper(freq='M')).size()

    # Tạo danh sách các tháng và số lượng đơn hàng tương ứng
    months = total_order.keys().to_list()
    count = total_order.values.tolist()

    # Tạo dictionary my_dict để lưu số lượng đơn hàng của mỗi tháng
    my_dict = {'01': 0, '02': 0, '03': 0,  '04': 0, '05': 0,
               '06': 0,  '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

    # Duyệt qua danh sách các tháng và lưu số lượng đơn hàng vào my_dict
    for i in range(len(months)):
        months[i] = str(pd.Timestamp(months[i]))[5:7]
        my_dict[str(months[i])] = count[i]

    # Vẽ biểu đồ cột với số liệu trong my_dict
    plt.bar(my_dict.keys(), my_dict.values())

    # Đặt nhãn cho trục x và trục y
    plt.xlabel('X Label')
    plt.ylabel('Y Label')

    # Lưu hình ảnh và trả về tên file và my_dict
    filename = save_image()
    return filename, my_dict



def funtion3(start_year="2019", end_year="2022"):
    # Tạo chuỗi ngày bắt đầu và kết thúc từ năm bắt đầu và kết thúc được truyền vào
    start_date = start_year + "-01-01"
    end_date = end_year + "-12-31"
    
    # Tạo câu truy vấn để lấy dữ liệu từ bảng 'core_order'
    # Lấy các bản ghi trong khoảng thời gian từ start_date đến end_date
    # Trả về các bản ghi có trạng thái 'ordered' là 1 và sắp xếp theo thứ tự tăng dần của ordered_date
    query = f"SELECT * FROM 'core_order' where ordered_date>='{start_date}' and ordered_date<='{end_date}' and ordered='1' order by start_date ASC"
    
    # Thực hiện truy vấn và tạo DataFrame từ kết quả trả về
    df = pd.read_sql_query(query, conn)
    
    # Chuyển ordered_date sang định dạng datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    
    # Đặt ordered_date làm cột chính của DataFrame
    df = df.set_index('ordered_date')
    
    # Tính tổng số đơn hàng được đặt theo từng năm
    total_order = df.groupby(pd.Grouper(freq='Y')).size()
    
    # Khởi tạo một dictionary với các khóa là năm và các giá trị là 0
    my_dict = {}
    for i in range(int(start_year), int(end_year)):
        my_dict[str(i)] = 0
    
    # Lấy danh sách các năm và số đơn hàng tương ứng
    years = total_order.keys().to_list()
    count = total_order.values.tolist()
    
    # Cập nhật giá trị của từng năm trong my_dict với số đơn hàng tương ứng
    for i in range(len(years)):
        years[i] = str(pd.Timestamp(years[i]))[0:4]
        my_dict[str(years[i])] = count[i]
    
    # Tạo biểu đồ cột với trục x là năm và trục y là số đơn hàng
    plt.bar(my_dict.keys(), my_dict.values())
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    
    # Lưu biểu đồ với tên file được trả về từ hàm save_image()
    filename = save_image()
    
    # Trả về tên file và dictionary chứa thông tin về số đơn hàng của từng năm
    return filename, my_dict


def funtion4(start_date="2022-01-01", end_date="2023-01-04", flag='D'):
    # Tạo câu truy vấn SQL để lấy dữ liệu từ cơ sở dữ liệu
    query = f"SELECT 'core_order'.'id', 'core_order'.'ordered_date','core_payment'.'amount' FROM 'core_payment', 'core_order' where 'core_order'.'payment_id'='core_payment'.'id' and 'core_order'.'ordered'=1 and 'core_order'.'ordered_date'>='{start_date}' and 'core_order'.'ordered_date'<='{end_date}' order by start_date ASC"
    # Đọc dữ liệu vào dataframe
    df = pd.read_sql_query(query, conn)
    # Chuyển đổi trường 'ordered_date' sang kiểu datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    # Nếu flag là 'D' hoặc 'd', thì nhóm dữ liệu theo ngày
    if flag == 'D' or flag == 'd':
        df['date'] = df['ordered_date'].dt.date
        time_amount = df.groupby('date')['amount'].sum()
    # Lấy danh sách các ngày và tổng số tiền
    days = time_amount.keys().to_list()
    amount = time_amount.values.tolist()
    # Chuyển đổi các ngày thành chuỗi để có thể hiển thị trên trục X của biểu đồ
    for i in range(len(days)):
        days[i] = str(days[i])
    # Vẽ biểu đồ cột và lưu vào file ảnh
    plt.bar(days, amount)
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    filename = save_image()
    # Trả về tên file ảnh, danh sách các ngày và tổng số tiền
    return filename, days, amount



def funtion5(year="2022", conn=conn, flag='M'):
    # Tạo ngày bắt đầu và kết thúc theo năm được truyền vào
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    # Tạo câu truy vấn dữ liệu từ bảng 'core_order' và 'core_payment' với điều kiện ordered=1 và ordered_date trong khoảng từ start_date đến end_date
    query = f"SELECT 'core_order'.'id', 'core_order'.'ordered_date','core_payment'.'amount' FROM 'core_payment', 'core_order' where 'core_order'.'payment_id'='core_payment'.'id' and 'core_order'.'ordered'=1 and 'core_order'.'ordered_date'>='{start_date}' and 'core_order'.'ordered_date'<='{end_date}' order by start_date ASC"
    # Đọc dữ liệu từ query vào DataFrame
    df = pd.read_sql_query(query, conn)
    # Chuyển đổi trường 'start_date' sang kiểu datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    # Nếu flag='M' hoặc flag='m', tạo trường 'month' từ trường 'ordered_date'
    if flag == 'M' or flag == 'm':
        df['month'] = df['ordered_date'].dt.month
        # Tính tổng số tiền thanh toán theo từng tháng
        time_amount = df.groupby('month')['amount'].sum()
        # Lấy danh sách các tháng và tổng số tiền thanh toán
        months = time_amount.keys().to_list()
        amount = time_amount.values.tolist()
        # Khởi tạo một dictionary lưu trữ các giá trị số đơn hàng trong từng tháng
        my_dict = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0,
                   '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        # Gán giá trị số đơn hàng vào từng tháng trong dictionary
        for i in range(len(months)):
            months[i] = str(months[i])
            my_dict[str(months[i])] = amount[i]
        # Vẽ biểu đồ cột từ dictionary đã tạo
        plt.bar(my_dict.keys(), my_dict.values())
        plt.xlabel('X Label')
        plt.ylabel('Y Label')
        # Lưu hình ảnh và trả về tên file và dictionary với số lượng đơn hàng theo từng tháng
        filename = save_image()
        return filename, my_dict



def funtion6(start_year="2021", end_year="2027", conn=conn):
    # Tạo ngày bắt đầu và ngày kết thúc từ năm bắt đầu và kết thúc
    start_date = start_year+"-01-01"
    end_date = end_year+"-12-31"

    # Tạo câu truy vấn để lấy dữ liệu từ bảng 'core_order' và 'core_payment'
    query = f"SELECT 'core_order'.'id', 'core_order'.'ordered_date','core_payment'.'amount' FROM 'core_payment', 'core_order' where 'core_order'.'payment_id'='core_payment'.'id' and 'core_order'.'ordered'=1 and 'core_order'.'ordered_date'>='{start_date}' and 'core_order'.'ordered_date'<='{end_date}' order by start_date ASC"

    # Đọc dữ liệu vào pandas DataFrame
    df = pd.read_sql_query(query, conn)

    # Chuyển đổi trường 'ordered_date' sang định dạng datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])

    # Tạo cột mới để lưu giá trị năm của 'ordered_date'
    df['year'] = df['ordered_date'].dt.year

    # Tính tổng số tiền được đặt hàng theo từng năm
    time_amount = df.groupby('year')['amount'].sum()

    # Tạo dictionary để lưu trữ giá trị của từng năm
    my_dict = {}
    for i in range(int(start_year), int(end_year)):
        my_dict[str(i)] = 0

    # Lưu giá trị của các năm và tổng số tiền được đặt hàng tương ứng
    years = time_amount.keys().to_list()
    amount = time_amount.values.tolist()

    for i in range(len(years)):
        years[i] = str(years[i])
        my_dict[str(years[i])] = amount[i]

    # Vẽ biểu đồ cột với trục X là năm và trục Y là tổng số tiền được đặt hàng
    plt.bar(my_dict.keys(), my_dict.values())
    plt.xlabel('X Label')
    plt.ylabel('Y Label')

    # Lưu hình ảnh vào một file và trả về tên file cùng với dictionary chứa giá trị của các năm
    filename = save_image()
    return filename, my_dict



def funtion7(year="2022"):
    start_date = year+"-01-01"
    end_date = year+"-12-31"

    # Truy vấn cơ sở dữ liệu để lấy thông tin về đơn hàng và thanh toán trong khoảng thời gian đã chỉ định
    query = f"select core_order.id, ordered_date,ordered, amount from core_order, core_payment where ordered_date>='{start_date}' and ordered_date<='{end_date}' and core_order.payment_id=core_payment.id"
    df = pd.read_sql(query, conn)

    # Chuyển đổi trường 'ordered_date' sang kiểu datetime
    df['ordered_date'] = pd.to_datetime(df['ordered_date'])
    df['order_date'] = df['ordered_date'].dt.month

    # Thống kê số lượng ordered bằng 1 và 0 theo ngày
    order_summary = df.groupby(['order_date', 'ordered'])['id'].count().reset_index()
    order_summary_pivot = pd.pivot_table(order_summary, values='id', index='order_date', columns='ordered', fill_value=0)

    # Tạo từ điển lưu số lượng đơn hàng (0) và hóa đơn (1) theo tháng
    my_dict_0 = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
    my_dict_1 = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}

    # Lưu số lượng đơn hàng (0) và hóa đơn (1) vào từ điển theo tháng
    for o in range(len(order_summary_pivot)):
        my_dict_0[str(order_summary_pivot.index[o])] = order_summary_pivot[0].values[o]
        my_dict_1[str(order_summary_pivot.index[o])] = order_summary_pivot[1].values[o]

    # Tạo biểu đồ cột cho số lượng đơn hàng và hóa đơn theo tháng
    X = my_dict_0.keys()
    order_date = my_dict_0.values()
    ordered = my_dict_1.values()
    X_axis = np.arange(len(X))
    plt.bar(X_axis - 0.2, order_date, 0.4, label='Đơn hàng')
    plt.bar(X_axis + 0.2, ordered, 0.4, label='Hóa đơn')
    plt.xticks(X_axis, X)
    plt.xlabel("Tháng")
    plt.ylabel("Số lượng")
    plt.title("BẢng thống kê")
    plt.legend()
    filename = save_image()

    return filename, my_dict_0, my_dict_1



def funtion8(year="2022"):
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
    revenues_ordered_0 = result[result.index.get_level_values('ordered') == 0]['amount'].groupby('month').sum().tolist()
    revenues_ordered_1 = result[result.index.get_level_values('ordered') == 1]['amount'].groupby('month').sum().tolist()
    
    my_dict_0 = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
    my_dict_1 = {'1': 0, '2': 0, '3': 0,  '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}

    # Chuyển đổi list sang dictionary
    for i in range(len(months)):
        months[i] = str(months[i])
        my_dict_0[str(months[i])] = revenues_ordered_0[i]
        my_dict_1[str(months[i])] = revenues_ordered_1[i]
    
    X = my_dict_0.keys()
    order_date = my_dict_0.values()
    ordered = my_dict_1.values()
    X_axis = np.arange(len(X))
    
    # Vẽ biểu đồ cột
    plt.bar(X_axis - 0.2, order_date, 0.4, label='Đơn hàng')
    plt.bar(X_axis + 0.2, ordered, 0.4, label='Hóa đơn')
    plt.xticks(X_axis, X)
    plt.xlabel("Tháng")
    plt.ylabel("Doanh thu")
    plt.title("Bảng thống kê")
    plt.legend()
    
    filename = save_image()  # Lưu biểu đồ thành hình ảnh
    
    return filename, my_dict_0, my_dict_1



def funtion9(year="2022", quantity=5):
    import json
    
    # Tạo chuỗi ngày bắt đầu và kết thúc dựa trên năm đầu vào
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    
    # Tạo câu truy vấn SQL để lấy thông tin đơn hàng và số lượng sản phẩm đã bán được
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
    
    # Đọc dữ liệu từ câu truy vấn SQL và chuyển đổi thành dataframe
    df = pd.read_sql(query, conn)
    
    # Đặt lại chỉ số của dataframe
    df = df.reset_index(drop=True)
    
    # Tạo 2 list lưu trữ tiêu đề sản phẩm và số lượng sản phẩm đã bán được
    title = df["title"].to_list()
    total_quantity = df["total_quantity"].to_list()
    
    # Tạo dictionary lưu trữ thông tin của sản phẩm
    my_dict = {key: value for key, value in zip(title, total_quantity)}
    
    # Tạo 2 list chứa thông tin của các sản phẩm để vẽ biểu đồ pie chart
    title = my_dict.keys()
    total_quantity = my_dict.values()
    
    # Tạo list chứa tỷ lệ phần trăm của từng sản phẩm
    explode = [0.1]*len(title)
    
    # Vẽ biểu đồ pie chart dựa trên thông tin của các sản phẩm
    plt.pie(total_quantity, explode=explode, labels=title,
            autopct='%1.1f%%', startangle=0,
            wedgeprops={"edgecolor": "white",
                        'linewidth': 5,
                        'antialiased': True})
    plt.axis('equal')
    
    # Lưu biểu đồ pie chart dưới dạng file ảnh và trả về tên file ảnh cùng với dictionary chứa thông tin của các sản phẩm
    filename = save_image()
    return filename, my_dict



def funtion10(year="2022", quantity=5):
    import json

    # Tạo chuỗi ngày bắt đầu và kết thúc năm dựa vào năm được truyền vào
    start_date = year + "-01-01"
    end_date = year + "-12-31"

    # Truy vấn CSDL để lấy thông tin các sản phẩm có số lượng bán nhiều nhất
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

    # Chuyển đổi dataframe thành 2 danh sách riêng biệt chứa tên sản phẩm và tổng số lượng
    df = df.reset_index(drop=True)
    title = df["label"].to_list()
    total_quantity = df["total_quantity"].to_list()

    # Tạo dictionary để lưu trữ thông tin sản phẩm và tổng số lượng tương ứng
    my_dict = {key: value for key, value in zip(title, total_quantity)}

    # Chuyển đổi lại title và total_quantity từ dictionary để sử dụng cho việc vẽ biểu đồ pie chart
    title = my_dict.keys()
    total_quantity = my_dict.values()

    # Tạo list explode chứa giá trị 0.1 lặp lại số lần bằng độ dài của danh sách sản phẩm
    explode = [0.1]*len(title)

    # Vẽ biểu đồ pie chart dựa trên danh sách sản phẩm và tổng số lượng
    plt.pie(total_quantity, explode=explode, labels=title,
            autopct='%1.1f%%', startangle=0,
            wedgeprops={"edgecolor": "white",
                        'linewidth': 5,
                        'antialiased': True})
    plt.axis('equal')

    # Lưu biểu đồ vào file ảnh và trả về tên file ảnh cùng với dictionary chứa thông tin sản phẩm và tổng số lượng tương ứng
    filename = save_image()
    return filename, my_dict



def funtion11(year="2022", quantity=20):
    """
    Lấy thông tin các khách hàng có số lần đặt hàng nhiều nhất trong năm được chỉ định.
    Tạo Wordcloud với từng khách hàng và số lần đặt hàng tương ứng.
    
    :param year: str, năm cần tìm kiếm thông tin khách hàng đặt hàng nhiều nhất.
    :param quantity: int, số lượng khách hàng xuất hiện nhiều nhất muốn lấy thông tin.
    
    :return: tuple, chứa tên file hình ảnh và từ điển số lần đặt hàng tương ứng của từng khách hàng.
    """
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
    plt.axis('off')
    filename = save_image()
    
    return filename, my_dict



# Hàm funtion12 lấy dữ liệu từ các bảng core_payment, auth_user và core_order trong database
# và tạo ra một wordcloud dựa trên tổng số tiền thanh toán của 5 khách hàng có tổng số tiền lớn nhất trong năm nào đó.

def funtion12(year="2022", quantity=10):
    # Đặt ngày bắt đầu và ngày kết thúc trong năm.
    start_date = year+"-01-01"
    end_date = year+"-12-31"
    
    # Tạo câu truy vấn SQL để lấy các thông tin cần thiết từ database.
    query = f"""SELECT core_payment.user_id,core_payment.amount , auth_user.username, auth_user.first_name, auth_user.last_name, core_order.ordered_date  FROM 'core_payment' 
            inner join auth_user on auth_user.id=core_payment.user_id
            inner join core_order on core_order.payment_id=core_payment.id
            where core_order.ordered_date between '{start_date}' and '{end_date}' and ordered='1';"""
    
    # Lấy dữ liệu từ database và đưa vào pandas dataframe.
    df = pd.read_sql(query, conn)
    
    # Nhóm các hàng theo user_id và tính tổng số tiền thanh toán.
    grouped = df.groupby('user_id').agg({'amount': 'sum'}).reset_index()

    # Lấy ra 5 khách hàng có tổng số tiền thanh toán lớn nhất.
    top_5 = grouped.nlargest(quantity, 'amount')

    # Lấy thông tin user_id, username, first_name, last_name của các khách hàng đó.
    result = df.loc[df['user_id'].isin(top_5['user_id'])][[        'user_id', 'username', 'first_name', 'last_name']].drop_duplicates()
    
    # Ghép các thông tin của khách hàng với tổng số tiền thanh toán của họ, sắp xếp giảm dần theo số tiền.
    result = result.merge(top_5, on='user_id').sort_values(
        by='amount', ascending=False)
    
    # Reset lại index của dataframe.
    result = result.reset_index(drop=True)

    # Tạo dictionary với key là tên của khách hàng, value là tổng số tiền thanh toán của họ.
    data_result = result[['username', 'amount']]
    username = list(data_result['username'])
    amount = list(data_result['amount'])
    my_dict = {key: value for key, value in zip(username, amount)}

    # Tạo wordcloud dựa trên dictionary vừa tạo.
    from wordcloud import WordCloud
    wc = WordCloud(margin=5, width=900, height=600, background_color='white')
    wc.generate_from_frequencies(my_dict)
    
    # Vẽ wordcloud lên màn hình.
    plt.figure(figsize=(10, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    
    # Lưu wordcloud thành file ảnh và trả về tên file cùng với dictionary.
    filename = save_image()
    return filename, my_dict
