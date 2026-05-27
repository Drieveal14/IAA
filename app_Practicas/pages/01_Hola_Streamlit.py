import streamlit as st
import numpy as np
import pandas as pd

st.title("Hola Streamlit 👋")

if st.button("Generar datos"):
    st.write("Datos aleatorios:")
    size = st.slider("Tamaño de los datos", 5, 50, 10)
    df = pd.DataFrame(np.random.randn(size, 2), columns=["x", "y"])
    st.line_chart(df)