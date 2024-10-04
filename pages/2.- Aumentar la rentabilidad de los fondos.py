# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:21:23 2024

@author: jperezr
"""

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Tickers de empresas de energía solar, eólica y geotérmica
solar_tickers = ['ENPH', 'SEDG', 'FSLR', 'CSIQ', 'RUN']  # Solar
eolica_tickers = ['NEE', 'EDPR.LS', 'VWS.CO']  # Eólica
geotermica_tickers = ['ORA', 'PNE3.DE']  # Geotérmica

st.title("Simulación de Inversiones para PENSIONISSSTE en Energías Renovables")

# Sidebar con información sobre el código y razones de inversión
with st.sidebar:
    st.header("Ayuda")
    st.write("""
    Esta aplicación permite simular el rendimiento de las inversiones en empresas de energía renovable (solar, eólica y geotérmica).
    
    **Funcionalidades:**
    - Selección de empresas (tickers) para análisis.
    - Selección de un rango de fechas para descargar los precios históricos ajustados.
    - Visualización de rentabilidad acumulada en el tiempo.
    - Análisis de riesgo (desviación estándar) y correlación entre las inversiones.
    - Comparación de riesgo vs retorno.
    - Estimación del impacto ambiental en términos de reducción de emisiones de CO₂.
    
    **Razones para invertir:**
    - **Sostenibilidad:** Las energías renovables juegan un papel clave en la lucha contra el cambio climático, y su crecimiento sigue aumentando. 
    - **Impacto ESG:** Las inversiones en energía solar, eólica y geotérmica están alineadas con los criterios ESG (ambientales, sociales y de gobernanza), lo que es crucial para los objetivos de PENSIONISSSTE.
    - **Diversificación:** Estas fuentes de energía ofrecen diversificación en la cartera de inversiones, minimizando el riesgo financiero a través de la inversión en distintos sectores.
    - **Retornos a largo plazo:** A medida que las economías globales se descarbonizan, las empresas de energías renovables tienen un potencial significativo de crecimiento, lo que se traduce en atractivos retornos a largo plazo.
    """)

# Selección múltiple de tickers
selected_tickers = st.multiselect(
    'Selecciona los tickers de las empresas',
    options=solar_tickers + eolica_tickers + geotermica_tickers,
    default=solar_tickers
)

# Selección de fechas de inicio y fin
start_date = st.date_input("Selecciona la fecha de inicio", pd.to_datetime("2018-01-01"))
end_date = st.date_input("Selecciona la fecha de fin", pd.to_datetime("2023-01-01"))

if selected_tickers and start_date < end_date:
    # Descargar datos de Yahoo Finance dentro del rango de fechas seleccionado
    data = yf.download(selected_tickers, start=start_date, end=end_date)['Adj Close']

    st.subheader("Gráfico de Precios Ajustados")
    st.line_chart(data)

    # Rentabilidad acumulada
    st.subheader("Rentabilidad Acumulada")
    cumulative_return = (data / data.iloc[0]) - 1
    st.line_chart(cumulative_return)

    # Gráfico de comparación de rendimiento
    fig = go.Figure()
    for ticker in selected_tickers:
        fig.add_trace(go.Scatter(x=data.index, y=cumulative_return[ticker], mode='lines', name=ticker))

    fig.update_layout(title="Comparación de Rentabilidad Acumulada",
                      xaxis_title="Fecha", yaxis_title="Rentabilidad Acumulada (%)")
    st.plotly_chart(fig)

    # Riesgo (desviación estándar)
    st.subheader("Análisis de Riesgo")
    risk = data.pct_change().std()
    risk_df = pd.DataFrame(risk, columns=["Riesgo (Desviación Estándar)"])
    st.write(risk_df)

    # Análisis de correlación para diversificación
    st.subheader("Correlación de las Inversiones (Diversificación)")
    corr_matrix = data.pct_change().corr()
    st.write(corr_matrix)

    # Gráfico de comparación de riesgo vs retorno
    avg_return = cumulative_return.mean() * 100  # Retorno promedio anualizado
    fig2 = go.Figure(data=[go.Scatter(x=risk, y=avg_return, mode='markers+text', text=risk.index)])
    fig2.update_layout(title="Riesgo vs Retorno",
                       xaxis_title="Riesgo (Desviación Estándar)",
                       yaxis_title="Retorno Promedio (%)")
    st.plotly_chart(fig2)

    # Impacto ESG - Reducción de emisiones (simulación teórica)
    st.subheader("Impacto Ambiental (Reducción de Emisiones de CO₂)")
    emission_reduction = {"Solar": 50, "Eólica": 70, "Geotérmica": 60}  # Toneladas de CO₂ por MW
    sector = ["Solar", "Eólica", "Geotérmica"]
    emissions_data = pd.DataFrame(sector, columns=["Sector"])
    emissions_data["Reducción Estimada (Toneladas CO₂/MW)"] = [emission_reduction[sec] for sec in sector]
    st.write(emissions_data)

    st.info("Estas estimaciones muestran el impacto positivo en términos de sostenibilidad y reducción de emisiones, clave para cumplir los objetivos ESG de PENSIONISSSTE.")

else:
    st.error("Selecciona una fecha de inicio anterior a la fecha de fin.")