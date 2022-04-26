import pandas as pd
import pandas_datareader.data as wb
import yfinance as yf
import plotly.express as px

#En primer lugar, hacemos una función para leer el archivo en el que tenemos los tickers
def tickers_read():
    tickers = pd.read_excel("Data/Market Ticker.xls")
    return tickers

tickers = tickers_read()

#Función con la cual, introduciendo el nombre de la empresa, te saque el ticker para insertarlo en la siguiente función
def ticker():
    ticker = str(input("Introduzca el nombre de la empresa que desee buscar "))
    ticker = tickers.loc[tickers["Name"]== ticker, "Ticker"]
    return ticker

ticker = ticker()


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


total_ticker_data = total_ticker_data()

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

last_data_ticker = last_ticker_data()

#Función para sacar máximo
def last_data_max():
    data_max = last_data_ticker['High'].max()
    return data_max

data_max = last_data_max()

#Función para sacar mínimo
def last_data_min():
    data_min = last_data_ticker['Low'].min()
    return data_min

data_min = last_data_min()

#Función para sacar la media de la Rentabilidad
def last_profit_avg():
    profit_avg = last_data_ticker['Profit'].mean()
    return profit_avg

profit_avg = last_profit_avg()

#Función para sacar un plot de la media de la rentabilidad
def plot():
    plot = px.line(last_data_ticker, y="Profit")
    return plot

last_plot = plot()

#last_data_ticker
#data_max 
#data_min
#profit_avg
#last_plot

