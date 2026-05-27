"""
=============================================================================
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO (UNAM)
Facultad de Ciencias 
Materia: Inteligencia Artificial
Docente: Dra. Jessica Sarahi Méndez Rincón
Ayudante de Laboratorio: Diego Eduardo Peña Villegas
Alumno: Diego Hazael Vega Alonso
Año escolar: 2026-2
Copyright: (c) 2025 UNAM - MIT License
Version: 1.0
This software is for educational purposes.  
-----------------------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI developed at UNAM.
=============================================================================
"""

from src.unam_fc_ai.models.regression import linear_regression

a, b = linear_regression([1, 2, 3], [2, 4, 6]) 

print(f"Result: a={a}, b={b}")