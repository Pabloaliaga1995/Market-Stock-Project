import pandas as pd
import pandas_datareader.data as wb
import yfinance as yf
import plotly.express as px
import streamlit as st

#En primer lugar, hacemos una función para leer el archivo en el que tenemos los tickers
def tickers_read():
    tickers = pd.read_excel("Data/Market Ticker.xls")
    return tickers


#Función con la cual, introduciendo el nombre de la empresa, te saque el ticker para insertarlo en la siguiente función
def ticker():
    ticker = st.sidebar.selectbox("Seleccione una empresa", tickers["Name"])
    ticker = tickers.loc[tickers["Name"]== ticker, "Ticker"]
    return ticker



#Función para que, a través del ticker obtenido, te saque los datos totales desde 2017
def total_ticker_data():
    ticker_data = pd.DataFrame()
    for i in ticker:
        data = wb.DataReader(ticker , "yahoo")[[ "High","Low"]]
        ticker_data["High"] = data["High"]
        ticker_data["Low"] = data["Low"]
        ticker_data["Profit"] = ((ticker_data["High"] - ticker_data["Low"])/(ticker_data["High"]))*100
        last_data_ticker = ticker_data.tail(7)
        ticker_data.to_csv("Data/Total_Ticker_info.csv")
        
    return ticker_data


#Función para que, a través del ticker obtenido, te saque los datos de las última semana y calcular parámetros
def last_ticker_data():
    ticker_data = pd.DataFrame()
    for i in ticker:
        data = wb.DataReader(ticker , "yahoo")[[ "High","Low"]]
        ticker_data["High"] = data["High"]
        ticker_data["Low"] = data["Low"]
        ticker_data["Profit"] = ((ticker_data["High"] - ticker_data["Low"])/(ticker_data["High"]))*100
        last_data_ticker = ticker_data.tail(7)
        last_data_ticker.to_csv("Data/Last_Ticker_info.csv")
    
    return last_data_ticker

#Función para sacar máximo
def last_data_max():
    data_max = last_data_ticker['High'].max()
    data_max = round(data_max,2)
    return data_max

#Función para sacar mínimo
def last_data_min():
    data_min = last_data_ticker['Low'].min()
    data_min = round(data_min,2)
    return data_min


#Función para sacar la media de la Rentabilidad
def last_profit_avg():
    profit_avg = last_data_ticker['Profit'].mean()
    profit_avg= round(profit_avg, 2)
    return profit_avg


#Función para sacar un plot de la media de la rentabilidad
def plot():
    plot = px.line(last_data_ticker, y="Profit")
    return plot


if __name__ == "__main__":
    tickers = tickers_read()
    ticker = ticker()
    total_ticker_data = total_ticker_data()
    last_data_ticker = last_ticker_data()
    data_max = last_data_max()
    data_min = last_data_min()
    profit_avg = last_profit_avg()
    last_plot = plot()


    #Streamfresh
    st.title("Market Stock Project")
    st.sidebar.header('Select Company you are looking for!')
    keys = tickers["Name"]
    st.image("https://static1.diariosur.es/www/pre2017/multimedia/RC/201412/29/media/cortadas/lobo-wall-street--320x378.jpg")
    st.dataframe(last_data_ticker)
    st.metric(label="Maximum", value = data_max)
    st.metric(label="Minimum", value= data_min)
    st.metric(label = "Profit Average", value = profit_avg)
    st.plotly_chart(last_plot, use_container_width=True)


