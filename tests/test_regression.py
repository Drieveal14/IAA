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


from unam_fc_ai.models.regression import linear_regression

# ejecutar   pip install -e .
#ejecutar como  python -m tests.test_regression
#a, b = linear_regression([1, 2, 3], [2, 4, 6])
#print(f"Result: a={a}, b={b}")


# test_regression.py 
def run_test():
    # Data
    X = [1.60, 1.70, 1.80, 1.90]
    Y = [60, 70, 80, 90]

    print("--- Starting Local Test ---")
    try:
        # La librería imprimirá automáticamente el Profiling Report
        a, b = linear_regression(X, Y)
        print(f"\nFinal Model: y = {a:.4f} + {b:.4f}x")
    except Exception as e:
        print(f"Test failed: {e}")


if __name__ == "__main__":
    run_test()