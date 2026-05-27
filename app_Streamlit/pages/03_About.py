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

st.set_page_config(page_title="About - UNAM", page_icon="🏫")

st.image("https://www.unam.mx/sites/default/files/unam_logo.png", width=100) # O ruta local
st.title("Acerca del Proyecto")

st.markdown("""
### 🎓 Institución
**Universidad Nacional Autónoma de México** Facultad de Contaduría y Administración  
*Licenciatura en Ciencia de Datos*

### 🔬 Laboratorio de IA
Este sistema fue desarrollado como parte de las buenas prácticas de 
ingeniería de software para IA. 

**Características técnicas:**
* **Arquitectura:** Modular (Basada en paquetes de Python).
* **Profiling:** Monitoreo activo de RAM y Tiempo.
* **Interfaz:** Streamlit Multipage.

**Docente:** [Nombre del Docente]  
**Alumno:** [Nombre del Alumno]  
**Año:** 2026
""")

st.info("Copyright © 2026 UNAM. Licencia MIT para fines educativos.")