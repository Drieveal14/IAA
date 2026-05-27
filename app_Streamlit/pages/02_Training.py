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

st.set_page_config(page_title="Model Training - UNAM", page_icon="🧠")

st.title("🧠 Model Training & Coefficients")
st.write("Experiment with data to see how the OLS model adapts.")

# Opción para generar datos sintéticos
n_points = st.slider("Number of points", 5, 50, 10)
slope_val = st.slider("Real Slope", 1.0, 5.0, 2.0)

if st.button("Generate & Train"):
    # Generamos datos simples y = slope * x
    X = [float(i) for i in range(n_points)]
    Y = [slope_val * x + (x * 0.1) for x in X] # Con un poco de ruido
    #Y = [2.0 * x + (noise * (i % 5)) for i, x in enumerate(X)]
    
    # Invocamos el motor de la UNAM IA
    intercept, slope = linear_regression(X, Y)
    # Mostrar métricas
    col1, col2 = st.columns(2)
    col1.metric("Intercept (a)", f"{intercept:.4f}")
    col2.metric("Slope (b)", f"{slope:.4f}")
    
    # Mostrar tabla de predicciones
    
    df = pd.DataFrame({
        "X (Input)": X,
        "Y (Real)": Y,
        "Y (Pred)": [intercept + slope * x for x in X]
    })
    st.dataframe(df.style.highlight_max(axis=0))

    # Invocamos tu motor de IA
    a, b = linear_regression(X, Y)
    
    # Mostrar métricas
    c1, c2 = st.columns(2)
    c1.metric("Intercepto (a)", f"{a:.4f}")
    c2.metric("Pendiente (b)", f"{b:.4f}")
    
    # Gráfico simple con Streamlit
    chart_data = pd.DataFrame({
        'X': X,
        'Y Real': Y,
        'Y Predicha': [a + b * x for x in X]
    })
    st.line_chart(chart_data, x='X', y=['Y Real', 'Y Predicha'])

st.divider()
st.caption("Desarrollado por la Facultad de Contaduría y Administración - UNAM")