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
The accuracy of the models depends strictly on the quality 
and preprocessing of the input data.
-----------------------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI developed at UNAM.
=============================================================================
"""
 
import time
import sys
import logging
from typing import List, Tuple,Any, Callable
from ..utils.profiling import log_performance




# Logger basic configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("AI_Library")

 


def trace_execution_time(func: Callable, *args: Any, **kwargs: Any) -> Any:
    """
    Measures the execution time of a function in seconds.
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    duration = end_time - start_time
    # Usamos print para visibilidad inmediata en Colab/Notebooks
    print(f"[PROFILER] Execution Time: {duration:.8f} seconds")
    return result

def trace_memory_usage(name: str, data: Any) -> None:
    """
    Calculates the approximate memory storage of an object in bytes.
    """
    # sys.getsizeof + size of elements if it's a list
    size_bytes = sys.getsizeof(data)
    if isinstance(data, list):
        size_bytes += sum(sys.getsizeof(item) for item in data)

    print(f"[PROFILER] Storage Usage ({name}): {size_bytes} bytes")




def linear_regression1(X: List[float], Y: List[float]) -> Tuple[float, float]:
    """
    Calculates OLS coefficients with built-in performance profiling.
    """
    start_time = time.perf_counter()
    
    # Storage calculation (RAM usage)
    mem_usage = sys.getsizeof(X) + sys.getsizeof(Y)
    if isinstance(X, list):
        mem_usage += sum(sys.getsizeof(i) for i in X)

    try:
        n = len(X)
        if n == 0: raise ValueError("Input lists cannot be empty.")

        x_mean = sum(X) / n
        y_mean = sum(Y) / n
        
        # Numerator and denominator using memory-efficient generators
        num = sum((X[i] - x_mean) * (Y[i] - y_mean) for i in range(n))
        den = sum((X[i] - x_mean) ** 2 for i in range(n))

        if den == 0:
            raise ZeroDivisionError("X variance is zero (vertical points).")

        b = num / den
        a = y_mean - (b * x_mean)

        # Log performance before returning
        duration = time.perf_counter() - start_time
        log_performance("Linear Regression", duration, mem_usage)
        
        return a, b

    except Exception as e:
        print(f"[ERROR] math failure: {e}")
        raise






def linear_regression(X: List[float], Y: List[float]) -> Tuple[float, float]:
    """
    Calculates the linear regression coefficients (y = a + bx).

    Uses the Ordinary Least Squares (OLS) method to find the slope (b)
    and the intercept (a) that best fit the data.

    Args:
        X: List of independent variables (e.g., height).
        Y: List of dependent variables (e.g., weight).

    Returns:
        A tuple (a, b) where 'a' is the intercept and 'b' is the slope.

    Complexity:
        Time: O(n) | Space: O(1)
    """
    logger.info("Starting linear regression calculation.")

    try:
        if len(X) != len(Y):
            raise ValueError("Arrays X and Y must have the same length.")

        n = len(X)
        if n == 0:
            raise ValueError("Input lists cannot be empty.")

        sum_x = sum(X)
        sum_y = sum(Y)
        sum_x2 = sum(x**2 for x in X)
        sum_xy = sum(x*y for x, y in zip(X, Y))

        denominator = (n * sum_x2) - (sum_x ** 2)

        if denominator == 0:
            raise ZeroDivisionError("X variance is zero (vertical points).")

        # Slope calculation (b)
        # Formula: b = [n*Σ(xy) - Σx*Σy] / [n*Σ(x²) - (Σx)²]
        b = ((n * sum_xy) - (sum_x * sum_y)) / denominator

        print("--- Calculation Process ---")
        print(f"b = ({n}*{sum_xy} - {sum_x}*{sum_y}) / "
              f"({n}*{sum_x2} - ({sum_x}^2))")
        print(f"b = {b}")

        a = (sum_y / n) - b * (sum_x / n)

        print(f"a = y_mean - b * x_mean")
        print(f"a = {Y} - {b}*{X}")
        print(f"a = {a}")
        print("---------------------------")

        logger.info(f"Model trained successfully: a={a:.4f}, b={b:.4f}")
        return a, b

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        raise
    except ZeroDivisionError as zde:
        logger.error(f"Math Error: {zde}")
        raise
    except Exception as e:
        logger.critical(f"Unexpected error in linear_regression: {e}")
        raise


def estimate_value(a: float, b: float, x_input: float) -> float:
    """
    Predicts a single value using the model (y = a + bx).

    >>> estimate_value(10.0, 2.0, 70.0)
    150.0
    """
    try:
        return a + b * x_input
    except TypeError:
        logger.error("Parameters a, b, and x_input must be numeric.")
        raise


def bulk_estimate(
    a: float,
    b: float,
    x_list: List[float]
) -> List[float]:
    """
    Performs predictions for a full list of values.

    Args:
        a: Y-intercept.
        b: Line slope.
        x_list: List of X input values.

    Returns:
        List of calculated estimates.
    """
    try:
        return [a + b * x for x in x_list]
    except TypeError:
        logger.error("Parameters a, b, and x_list must contain numeric types.")
        raise