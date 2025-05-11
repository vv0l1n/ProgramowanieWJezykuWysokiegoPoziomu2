import sqlite3
import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px


def get_connection():
    return sqlite3.connect("sales.db")

def add_sale(product, quantity, price, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
                   (product, quantity, price, date))
    conn.commit()
    conn.close()

def get_sales():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df

st.title("📊 Aplikacja Sprzedażowa")

st.header("➕ Dodaj nową sprzedaż")
with st.form("add_form"):
    product = st.text_input("Produkt")
    quantity = st.number_input("Ilość", min_value=1, step=1)
    price = st.number_input("Cena", min_value=0.0, step=0.1)
    date = st.date_input("Data", value=datetime.today()).strftime("%Y-%m-%d")
    submitted = st.form_submit_button("Dodaj")

    if submitted:
        if product:
            add_sale(product, quantity, price, date)
            st.success("✅ Sprzedaż dodana!")
            st.balloons()
        else:
            st.error("❌ Wprowadź nazwę produktu.")

st.header("📋 Dane sprzedaży")
sales_df = get_sales()

product_filter = st.selectbox("Filtruj po produkcie", options=["Wszystkie"] + sorted(sales_df["product"].unique()))
if product_filter != "Wszystkie":
    sales_df = sales_df[sales_df["product"] == product_filter]

st.dataframe(sales_df)

if not sales_df.empty:
    st.header("📈 Wykresy")

    # Wartość dzienna
    sales_df["date"] = pd.to_datetime(sales_df["date"])
    sales_df["total"] = sales_df["quantity"] * sales_df["price"]
    daily_sales = sales_df.groupby("date")["total"].sum().reset_index()

    fig1 = px.line(daily_sales, x="date", y="total", title="Sprzedaż dzienna (wartość)")
    st.plotly_chart(fig1)

    product_summary = sales_df.groupby("product")["quantity"].sum().reset_index()
    fig2 = px.bar(product_summary, x="product", y="quantity", title="Suma sprzedanych produktów wg typu")
    st.plotly_chart(fig2)
else:
    st.info("Brak danych do wyświetlenia wykresów.")
