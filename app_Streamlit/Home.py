"""
=============================================================================
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO (UNAM)
Facultad de Ciencias 
Materia: Inteligencia Artificial
Docente: Dra. Jessica Sarahi Méndez Rincón
Ayudante de Laboratorio: Diego Eduardo Peña Villegas
Alumno: Vega Alonso Diego Hazael
Año escolar: 2026-2
Copyright: (c) 2025 UNAM - MIT License
This software is for educational purposes.  
-----------------------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI developed at UNAM.
=============================================================================
"""
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="UNAM IA - Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Estilo personalizado para los colores UNAM (Azul y Oro)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .unam-header { color: #003b5c; font-size: 40px; font-weight: bold; }
    .unam-subheader { color: #d4af37; font-size: 25px; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Institucional
st.markdown('<p class="unam-header">Universidad Nacional Autónoma de México</p>', 
            unsafe_allow_html=True)
st.markdown('<p class="unam-subheader">IA Library: Linear Regression Toolkit</p>', 
            unsafe_allow_html=True)

st.divider()

# Cuerpo de la página
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Welcome to the AI Laboratory")
    st.write("""
    This platform integrates the **unam_fc_ai** library, a specialized toolkit 
    for Artificial Intelligence. Developed for the Faculty of Accounting 
    and Administration, this tool focuses on:
    """)
    st.markdown("""
    * **Efficiency:** Optimized OLS algorithms.
    * **Observability:** Built-in performance profiling.
    * **Scalability:** Enterprise-ready architecture.
    """)

with col2:
    st.info("**Course Information**")
    st.write("**Subject:** Artificial Intelligence")
    st.write("**Year:** 2026")
    st.write("**License:** MIT")

st.success("Select a page from the sidebar to begin exploring the data.")