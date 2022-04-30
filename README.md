# :bar_chart: **Market Stock Project**

<img src="https://smartgridspain.org/web/wp-content/uploads/2021/05/Bolsa_mercado_valores_istockphoto-943292690.jpg"  width = 700   alt="PROJECT LOGO"/>

ENG

## :running: **OBJECTIVES**
- Get a dataframe with the relevant metrics of the choose Stock Market Value for the selected period of time. This dataframe would be saved in our folder(Data) by csv.
- Streamlit which shows our dataframe, relevant metrics and plotting the profitability.

## :computer: **ENV**
- Python 3.7 (conda install python == 3.7)
- Pandas (conda install pandas)
- Numpy (conda install numpy)
- yfinance
- Plotly (conda install Plotly)
- Streamlit (pip install Streamlit)
- Requests(conda install requests)


## CODE :chart_with_downwards_trend: :mag:
- Create a database from the tickers through Yahoo Finance API in order to obtain the required data and clean it.
- After having the data, we start working on functions.
- The first function is the one for reading the file where we have the tickers.
- After having this file, we create a function with which, by entering the name of the company, you get the ticker to insert it into the following function.
- The following 2 functions, through the ticker obtained in the previous function, provide you total data since 2017 and last week's data, as well as the relevant metrics for that value. After that, the dataframes are saved in CSV on our computer.
- After getting both dataframes, saved in CSV, we create 3 functions in order to obtain, from our data, the maximum, minimum and the average of the profitability for the chosen period of time.
- Since we have all the data prepared, we plot the profitability for the chosen period of time to show more crearly that metrics.
- With all our functions defined, we start working on streamlit.
- In Streamlit, we can see a selectbox for choosing the company.
- When we select a company, Streamlit shows us a dataframe with its metrics, relevant metrics, a weekly profit plot and a frame of Wall Street Journal to observe the main indexes of the world.
- Finally, in order to run it on Terminal, it has to be used the following command:

```
streamlit run main.py
```

CSV SAVED
--------------------------------------
- Documents/ironhack/Market-Stock-Project/Data/Last_Ticker_info.csv)
- Documents/ironhack/Market-Stock-Project/Data/Total_Ticker_info.csv)


## :file_folder: **Folder structure**
```
└── project
    ├── Api Connection
    │   └── API.ipynb
    ├── data
        ├── Last_Ticker_info.csv
        ├── Total_Ticker_info
        ├── last_10_days_data_index.csv
        ├── Last_10_days_data_cleaned.csv
        ├── Last_10_days_values.csv
        ├── Total_data_values.csv
        └── Market Ticker.xls
    ├── Data Cleaning
    │   ├── Data_cleaning.ipynb
    │   └── Prueba Data Cleaning.ipynb
    ├── Functions
    │   └── Finance_functions.ipynb
    ├── main.py
    └── README.md
```

### :incoming_envelope: **Contact info**
If you have any question, please contact me! (Pabloaliaga1995@hotmail.com)


--------------------------------------------------------------------------------------------------------------------------------------------------------
ESP

## :running: **OBJETIVOS**

- Obtener un dataframe con las métricas relevantes del valor bursátil elegido para el periodo de tiempo seleccionado. Este dataframe se guardaría en nuestra carpeta(Data) por csv.
- Streamlit que muestra nuestro dataframe, las métricas relevantes y un gráfico de la rentabilidad.

## :computer: **ENV**
- Python 3.7 (conda install python == 3.7)
- Pandas (conda install pandas)
- Numpy (conda install numpy)
- yfinance
- Plotly (conda install Plotly)
- Streamlit (pip install Streamlit)
- Requests (conda install requests)


## CODE :chart_with_downwards_trend: :mag:
- Crear una base de datos a través de la API de Yahoo Finance, para poder obtener los datos necesarios y limpiarlos.
- Una vez tenemos los datos, empezamos a trabajar en las funciones.
- La primera función es para leer fichero donde tenemos los tickers.
- Después de tener este fichero, creamos una función con la que, introduciendo el nombre de la empresa, se obtiene el ticker para insertarlo en la siguiente función.
- Las siguientes 2 funciones, a través del ticker obtenido en la función anterior, te proveen de los datos totales desde 2017 y de los datos de la última semana, así como las métricas relevantes para ese valor. Después de ello, se guardan los dataframes en CSV en nuestro ordenador.
- Tras conseguir ambos dataframes, guardados en CSV, creamos 3 funciones para obtener, a partir de nuestros datos, el máximo, el mínimo y la media de la rentabilidad para el periodo de tiempo elegido.
- Una vez tenemos todos los datos preparados, graficamos la rentabilidad para el periodo de tiempo elegido, para poder mostrar más claramente dicha métrica.
- Con todas nuestras funciones definidas, empezamos a trabajar en streamlit.
- En Streamlit, podemos ver un filtro de selección para elegir la empresa.
- Cuando seleccionamos una empresa, Streamlit nos muestra un dataframe con sus métricas, las métricas relevantes, un gráfico de rentabilidad semanal y un frame del periodico Wall Street Journal para observar los principales índices del mundo.
- Por último, para ejecutarlo en el Terminal, hay que utilizar el siguiente comando:

```
streamlit run main.py
```

CSV SAVED
--------------------------------------
- Documents/ironhack/Market-Stock-Project/Data/Last_Ticker_info.csv)
- Documents/ironhack/Market-Stock-Project/Data/Total_Ticker_info.csv)


## :file_folder: **Folder structure**
```
└── project
    ├── Api Connection
    │   └── API.ipynb
    ├── data
        ├── Last_Ticker_info.csv
        ├── Total_Ticker_info
        ├── last_10_days_data_index.csv
        ├── Last_10_days_data_cleaned.csv
        ├── Last_10_days_values.csv
        ├── Total_data_values.csv
        └── Market Ticker.xls
    ├── Data Cleaning
    │   ├── Data_cleaning.ipynb
    │   └── Prueba Data Cleaning.ipynb
    ├── Functions
    │   └── Finance_functions.ipynb
    ├── main.py
    └── README.md
    ```

### :incoming_envelope: **Contact info**
If you have any question, please contact me! (Pabloaliaga1995@hotmail.com)
