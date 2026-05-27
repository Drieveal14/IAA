"""
=============================================================================
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO (UNAM)
Facultad de Ciencias 
Materia: Inteligencia Artificial
Docente: Dra. Jessica Sarahi Méndez Rincón
Ayudante de Laboratorio: Diego Eduardo Peña Villegas
Alumno: [Nombre del Alumno]
Año escolar: 2026-2
Copyright: (c) 2025 UNAM - MIT License
This software is for educational purposes.  
-----------------------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI developed at UNAM.
=============================================================================
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Importamos desde tu librería profesional
import sys
import os
# Agrega la carpeta 'src' al path de Python para que Streamlit la vea
# 1. Obtenemos la ruta de la carpeta donde está este archivo (pages/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Subimos dos niveles para llegar a la raíz (UNAM_FC_JSMR_Laboratorio)
#    y luego entramos a 'src'
project_root = os.path.join(current_dir, "..", "..", "src")

# 3. Lo agregamos al sistema para que Python encuentre 'unam_fc_ai'
if project_root not in sys.path:
    sys.path.append(os.path.abspath(project_root))

# 4. Ahora sí, importamos tu librería
from unam_fc_ai.models.regression import linear_regression

st.title("📊 Data Analysis Dashboard")

# Simulación de carga de datos
st.subheader("1. Input Data")
data_input = st.text_area("Enter X values (comma separated)", "1.60, 1.65, 1.70, 1.80")
target_input = st.text_area("Enter Y values (comma separated)", "60, 65, 72, 80")

if st.button("Calculate Regression"):
    try:
        # Limpieza de datos
        X = [float(x.strip()) for x in data_input.split(",")]
        Y = [float(y.strip()) for y in target_input.split(",")]
        
        # Invocación del Motor de IA
        intercept, slope = linear_regression(X, Y)
        
        # Resultados con estilo UNAM
        st.success(f"Model trained: y = {intercept:.4f} + {slope:.4f}x")
        
        # Tabla comparativa
        df = pd.DataFrame({"Feature (X)": X, "Target (Y)": Y})
        st.table(df)
        
    except Exception as e:
        st.error(f"Error in calculation: {e}")

st.info("Note: This dashboard uses the unam_fc_ai core library.")


# Entrada de datos dinámica
st.subheader("2. Configuración de Datos")
col_a, col_b = st.columns(2)
with col_a:
    x_input = st.text_input("Valores X (separados por coma)", "1, 2, 3, 4, 5")
with col_b:
    y_input = st.text_input("Valores Y (separados por coma)", "2.1, 3.9, 6.2, 8.1, 10.5")

if st.button("📈 Generar Modelo"):
    try:
        X = [float(i.strip()) for i in x_input.split(",")]
        Y = [float(i.strip()) for i in y_input.split(",")]
        
        # Invocamos el motor de IA
        a, b = linear_regression(X, Y)
        
        st.success(f"Modelo: y = {a:.4f} + {b:.4f}x")
        
        # --- Generación de Gráfica ---
        fig, ax = plt.subplots()
        ax.scatter(X, Y, color='#003b5c', label='Datos Reales (UNAM)')
        y_pred = [a + b * x for x in X]
        ax.plot(X, y_pred, color='#d4af37', label='Línea de Regresión')
        ax.set_xlabel("Variable Independiente (X)")
        ax.set_ylabel("Variable Dependiente (Y)")
        ax.legend()
        
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error: {e}")