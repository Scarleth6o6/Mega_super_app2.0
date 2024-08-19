import pandas as pd
import plotly.express as px 
import streamlit as st

st.header('Aplicacion de Vehiculos')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un grafico de dispersión')

if build_histogram: # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
elif build_scatter: # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un scatter plot
    fig = px.scatter(car_data, x="odometer", y="price")

        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)