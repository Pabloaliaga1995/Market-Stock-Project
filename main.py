import pandas as pd
import pandas_datareader.data as wb
import yfinance as yf
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components

#En primer lugar, hacemos una función para leer el archivo en el que tenemos los tickers
def tickers_read():
    tickers = pd.read_excel("Data/Market Ticker.xls")
    return tickers


#Función con la cual, introduciendo el nombre de la empresa, te saque el ticker para insertarlo en la siguiente función
def ticker():
    ticker = st.sidebar.selectbox("Seleccione una empresa", tickers["Name"])
    ticker = tickers.loc[tickers["Name"]== ticker, "Ticker"]
    return ticker


#Función para que, a través del ticker obtenido, te saque los datos totales desde 2017 y calcular parámetros
def total_ticker_data():
    ticker_data = pd.DataFrame()
    for i in ticker:
        data = wb.DataReader(ticker , "yahoo")[[ "High","Low"]]
        ticker_data["High"] = data["High"]
        ticker_data["High"] = ticker_data["High"].round(2)
        ticker_data["Low"] = data["Low"]
        ticker_data["Low"] = ticker_data["Low"].round(2)
        ticker_data["Profit"] = ((ticker_data["High"] - ticker_data["Low"])/(ticker_data["High"]))*100
        ticker_data["Profit"] = ticker_data["Profit"].round(2)
        ticker_data = ticker_data.reset_index()
        ticker_data['Date'] = pd.to_datetime(ticker_data['Date'])
        ticker_data['Date'] = ticker_data['Date'].dt.strftime('%d/%m/%Y')
        ticker_data = ticker_data.set_index("Date")
        ticker_data.to_csv("Data/Total_Ticker_info.csv")
        
    return ticker_data


#Función para que, a través del ticker obtenido, te saque los datos de las última semana y calcular parámetros
def last_ticker_data():
    ticker_data = pd.DataFrame()
    for i in ticker:
        data = wb.DataReader(ticker , "yahoo")[[ "High","Low"]]
        ticker_data["High"] = data["High"]
        ticker_data["High"] = ticker_data["High"].round(2)
        ticker_data["Low"] = data["Low"]
        ticker_data["Low"] = ticker_data["Low"].round(2)
        ticker_data["Profit"] = ((ticker_data["High"] - ticker_data["Low"])/(ticker_data["High"]))*100
        ticker_data["Profit"] = ticker_data["Profit"].round(2)
        ticker_data = ticker_data.reset_index()
        ticker_data['Date'] = pd.to_datetime(ticker_data['Date'])
        ticker_data['Date'] = ticker_data['Date'].dt.strftime('%d/%m/%Y') 
        ticker_data = ticker_data.set_index("Date")
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
    total_ticker_data1 = total_ticker_data()
    last_data_ticker = last_ticker_data()
    data_max = last_data_max()
    data_min = last_data_min()
    profit_avg = last_profit_avg()
    last_plot = plot()


    #Streamfresh
    st.title("Market Stock Project")
    st.sidebar.header('Select Company you are looking for!')
    st.image("https://frankblackhal.files.wordpress.com/2016/05/o-the-wolf-of-wall-street-facebook.jpg")
    st.header('Dataframe from the last 7 days')
    st.table(last_data_ticker)
    st.text("Guardado en CSV")
    st.header('Relevant Metrics')
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Maximum", value = data_max)
    col2.metric(label="Minimum", value= data_min)
    col3.metric(label = "Profit Average", value = profit_avg)
    st.header('Profit Plot')
    st.plotly_chart(last_plot, use_container_width=True)
    st.balloons()

    components.iframe("https://www.wsj.com/market-data?mod=Markets_MDW_MDC", height= 1000, width= 1000, scrolling = True)




