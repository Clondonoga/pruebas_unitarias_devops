import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_por_volumen,
    descuento_cumulativo,
    descuento_apilado
)

# ==========================================
# Pruebas para aplicar_descuento
# ==========================================
def test_aplicar_descuento_10_por_ciento():
    # Arrange
    precio = 100
    porcentaje = 10
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 90

def test_aplicar_descuento_negativo_lanza_error():
    with pytest.raises(ValueError):
        aplicar_descuento(100, -10)

# ==========================================
# Pruebas para calcular_precio_final (Revela BUG 1)
# ==========================================
def test_calcular_precio_final_impuesto_sobre_descuento():
    # Arrange
    precio = 100
    impuesto = 19
    descuento = 10
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    # Esperado: Descuento (90) + 19% de 90 = 90 + 17.1 = 107.1
    # El código con bug daba: 90 + 19% de 100 = 109.0
    assert resultado == pytest.approx(107.1)

# ==========================================
# Pruebas para descuento_por_volumen
# ==========================================
def test_descuento_por_volumen_menos_de_10():
    resultado = descuento_por_volumen(5, 10)
    assert resultado == 50  # 50 sin descuento

def test_descuento_por_volumen_100_unidades():
    resultado = descuento_por_volumen(100, 10)
    assert resultado == 800  # 1000 - 20% = 800

# ==========================================
# Pruebas para descuento_cumulativo
# ==========================================
def test_descuento_cumulativo_dos_descuentos():
    # Arrange
    precio = 100
    descuentos = [10, 20]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    # 100 - 10% = 90; 90 - 20% = 72
    assert resultado == 72

# ==========================================
# Pruebas para descuento_apilado (Revela BUG 2)
# ==========================================
def test_descuento_apilado_suma_menor_100():
    # Arrange
    precio = 100
    descuentos = [10, 20]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 70  # 100 - 30% = 70

def test_descuento_apilado_suma_excede_100():
    # Arrange
    precio = 100
    descuentos = [60, 50]  # Suma 110%
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    # El código con bug lanzaba ValueError. El corregido lo topa al 100% y da 0.
    assert resultado == 0
