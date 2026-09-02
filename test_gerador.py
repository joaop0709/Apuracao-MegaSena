import pytest
from gerador import gerar_aposta

def test_gerar_aposta_quantidade_padrao():
    aposta = gerar_aposta()
    assert len(aposta) == 6
    assert all(1 <= num <= 60 for num in aposta)

def test_gerar_aposta_quantidade_customizada():
    aposta = gerar_aposta(10)
    assert len(aposta) == 10

def test_gerar_aposta_invalida():
    with pytest.raises(ValueError):
        gerar_aposta(5)
    with pytest.raises(ValueError):
        gerar_aposta(16)