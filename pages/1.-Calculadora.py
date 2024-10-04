# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:11:02 2024

@author: jperezr
"""

import streamlit as st

# Función para calcular la pensión futura
def calcular_pension(salario_actual, porcentaje_ahorro, años, tasa_interes):
    ahorro_anual = salario_actual * (porcentaje_ahorro / 100)
    total_ahorro = 0
    for _ in range(años):
        total_ahorro += ahorro_anual
        total_ahorro *= (1 + tasa_interes / 100)  # Interés compuesto
    return total_ahorro

# Interfaz de Streamlit
st.title("Simulador de Pensiones para PENSIONISSSTE")

# Entrada de datos
salario_actual = st.number_input("Salario Actual:", value=50000)
porcentaje_ahorro = st.slider("Porcentaje de Ahorro (%):", 1, 100, 10)
años = st.number_input("Años hasta la Jubilación:", value=30)
tasa_interes = st.slider("Tasa de Interés Anual (%):", 0.0, 10.0, 5.0)

# Calcular pensión
if st.button("Calcular Pensión Futura"):
    pension_futura = calcular_pension(salario_actual, porcentaje_ahorro, años, tasa_interes)
    st.success(f"Tu pensión futura estimada es: ${pension_futura:,.2f}")