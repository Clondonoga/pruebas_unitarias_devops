import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_por_volumen,
    descuento_cumulativo,
    descuento_apilado
)

# --- aplicar_descuento ---
def test_aplicar_descuento_positivo():
    assert aplicar_descuento(100, 10) == 90

def test_aplicar_descuento_error_precio_negativo():
    with pytest.raises(ValueError):
        aplicar_descuento(-10, 10)

def test_aplicar_descuento_error_porcentaje_invalido():
    with pytest.raises(ValueError):
        aplicar_descuento(100, -10)
    with pytest.raises(ValueError):
        aplicar_descuento(100, 150)

# --- calcular_descuento ---
def test_calcular_descuento_positivo():
    assert calcular_descuento(200, 15) == 30

def test_calcular_descuento_error_precio_negativo():
    with pytest.raises(ValueError):
        calcular_descuento(-100, 10)

def test_calcular_descuento_error_porcentaje_invalido():
    with pytest.raises(ValueError):
        calcular_descuento(100, -5)
    with pytest.raises(ValueError):
        calcular_descuento(100, 110)

# --- calcular_precio_final (Bug 1) ---
def test_calcular_precio_final_con_impuesto_y_descuento():
    # Impuesto sobre precio con descuento: 90 + 19% de 90 = 107.1
    assert calcular_precio_final(100, 19, 10) == pytest.approx(107.1)

def test_calcular_precio_final_errores_validacion():
    with pytest.raises(ValueError):
        calcular_precio_final(-100, 19, 10)
    with pytest.raises(ValueError):
        calcular_precio_final(100, -5, 10)
    with pytest.raises(ValueError):
        calcular_precio_final(100, 19, 110)

# --- descuento_por_volumen ---
def test_descuento_por_volumen_sin_descuento():
    assert descuento_por_volumen(5, 10) == 50

def test_descuento_por_volumen_10_unidades():
    assert descuento_por_volumen(10, 10) == 95

def test_descuento_por_volumen_20_unidades():
    assert descuento_por_volumen(20, 10) == 180

def test_descuento_por_volumen_50_unidades():
    assert descuento_por_volumen(50, 10) == 425

def test_descuento_por_volumen_100_unidades():
    assert descuento_por_volumen(100, 10) == 800

def test_descuento_por_volumen_errores():
    with pytest.raises(ValueError):
        descuento_por_volumen(-1, 10)
    with pytest.raises(ValueError):
        descuento_por_volumen(10, -5)

# --- descuento_cumulativo ---
def test_descuento_cumulativo_vacio():
    assert descuento_cumulativo(100, []) == 100

def test_descuento_cumulativo_dos_descuentos():
    assert descuento_cumulativo(100, [10, 20]) == 72

def test_descuento_cumulativo_error():
    with pytest.raises(ValueError):
        descuento_cumulativo(-100, [10])
    with pytest.raises(ValueError):
        descuento_cumulativo(100, [110])

# --- descuento_apilado (Bug 2) ---
def test_descuento_apilado_vacio():
    assert descuento_apilado(100, []) == 100

def test_descuento_apilado_suma_menor_100():
    assert descuento_apilado(100, [10, 20]) == 70

def test_descuento_apilado_excede_100():
    # Bug 2 corregido: no lanza error, da 0 porque tope es 100%
    assert descuento_apilado(100, [60, 50]) == 0

def test_descuento_apilado_precio_negativo():
    with pytest.raises(ValueError):
        descuento_apilado(-100, [10, 20])
