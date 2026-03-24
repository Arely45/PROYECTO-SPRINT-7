import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.title("Análisis de")
st.header('Vehiculos')

@st.cache_data
def cargar_datos():
    # cargar el dataset de vehiculos
    car_data = pd.read_csv("vehicles_us.csv")
    return car_data

car_data = cargar_datos()

st.subheader("Vista previa del dataset")
st.dataframe(car_data.head(25))

# histograma
if st.button('Construir histograma'):    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    hist.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(hist, use_container_width=True)

#grafico de dispersion
if st.button('Construir gráfico de dispersión'):
    st.write('Gráfico de dispersión de precios')
    scatter_plot = px.scatter(car_data, x="model_year", y="price", color="paint_color", symbol="condition")
    st.plotly_chart(scatter_plot, use_container_width=True)

# casillas de verificacion
cv_hist = st.checkbox('Construir un histograma')
cv_scatter = st.checkbox('Construir un gráfico de dispersión')

if cv_hist: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma de la condicion de los coches')
    hist_fig = go.Figure(data=[go.Histogram(x=car_data['condition'])])
    hist_fig.update_layout(title_text='Distribución de la condición de los coches')
    st.plotly_chart(hist_fig, use_container_width=True)

if cv_scatter:
    st.write('Gráfico de dispersión de precios')
    scatter_fig = px.scatter(car_data, x="cylinders", y="price", color="paint_color")
    st.plotly_chart(scatter_fig, use_container_width=True)
