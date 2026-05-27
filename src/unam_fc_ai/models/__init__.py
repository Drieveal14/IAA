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


#from .models.regression import estimate_value

# Solo un punto, porque ya estás dentro de la carpeta 'models'
from .regression import linear_regression

__all__ = ["linear_regression"]

__all__ = ["linear_regression", "estimate_value"]
__version__ = "1.0.0"