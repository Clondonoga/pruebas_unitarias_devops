import pytest
from src.calculadora import (
    sumar, restar, multiplicar, dividir,
    potencia, raiz_cuadrada, promedio, maximo, minimo,
    calcular_area_rectangulo, calcular_perimetro_rectangulo
)

# ==========================================
# Pruebas básicas
# ==========================================
def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_potencia_positiva():
    assert potencia(2, 3) == 8

# ==========================================
# Pruebas que revelan BUG 1 (raiz_cuadrada)
# ==========================================
def test_raiz_cuadrada_positivo():
    assert raiz_cuadrada(25) == 5

def test_raiz_cuadrada_negativo_lanza_error():
    # Arrange
    numero = -4
    # Act & Assert
    # El código con bug devuelve un número complejo (2j) en vez de lanzar error
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)

# ==========================================
# Pruebas que revelan BUG 2 (minimo)
# ==========================================
def test_minimo_lista_positivos():
    # Arrange
    lista = [5, 8, 3, 9]
    # Act
    resultado = minimo(lista)
    # Assert
    # El código con bug devuelve 0 porque inicializa min_val = 0
    assert resultado == 3

def test_maximo_lista_positivos():
    lista = [5, 8, 3, 9]
    assert maximo(lista) == 9

def test_promedio_lista():
    lista = [10, 20, 30]
    assert promedio(lista) == 20

# ==========================================
# Pruebas de geometría (casos límite)
# ==========================================
def test_area_rectangulo():
    assert calcular_area_rectangulo(5, 4) == 20

def test_area_rectangulo_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_area_rectangulo(-5, 4)

def test_perimetro_rectangulo():
    assert calcular_perimetro_rectangulo(5, 4) == 18
# ==========================================
# Pruebas adicionales para llegar al 100%
# ==========================================
def test_restar_positivos():
    assert restar(10, 4) == 6

def test_multiplicar_positivos():
    assert multiplicar(6, 7) == 42

def test_potencia_exponente_cero():
    assert potencia(5, 0) == 1

def test_maximo_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        maximo([])

def test_minimo_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        minimo([])

def test_area_rectangulo_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_area_rectangulo(-5, 4)

def test_perimetro_rectangulo_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(5, -4)
