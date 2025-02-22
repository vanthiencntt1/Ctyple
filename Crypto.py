import streamlit as st
from vnstock import Vnstock
import pandas as pd
import time
from datetime import datetime  # Import datetime để lấy ngày hiện tại

st.set_page_config(layout="wide")  # Giao diện rộng

st.title("📊 Cập nhật dữ liệu tài chính theo thời gian thực")

# Lấy ngày hiện tại
today = datetime.today().strftime('%Y-%m-%d')

# Tạo 2 cột để hiển thị trên cùng 1 hàng
col1, col2 = st.columns(2)

while True:
    with col1:
        st.subheader("📈 Dữ liệu chứng khoán ACB (Cập nhật)")
        stock = Vnstock().stock(symbol='ACB', source='VCI')
        ck = stock.quote.history(start='2024-01-01', end=today, interval='1D')
        st.dataframe(ck.tail(10))  # Hiển thị 10 dòng mới nhất

    with col2:
        st.subheader("💰 Dữ liệu Crypto - Bitcoin (Cập nhật)")
        fx = Vnstock().crypto(symbol='BTC', source='MSN')
        cry = fx.quote.history(start='2024-02-28', end=today, interval='1D')
        st.dataframe(cry.tail(10))  # Hiển thị 10 dòng mới nhất

    time.sleep(10)  # Cập nhật mỗi 10 giây
    st.rerun()  # Làm mới giao diện
