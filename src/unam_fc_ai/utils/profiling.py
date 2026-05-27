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


import time
import sys
from typing import Any

def log_performance(func_name: str, duration: float, memory_bytes: int):
    """Prints a professional performance report for the UNAM AI Library."""
    print("\n" + "="*40)
    print(f"📊 UNAM AI PERFORMANCE REPORT: {func_name}")
    print("-" * 40)
    print(f"⏱️ Execution Time: {duration:.8f} sec")
    print(f"💾 RAM Storage:    {memory_bytes} bytes")
    print("="*40 + "\n")