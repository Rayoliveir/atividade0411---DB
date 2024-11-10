import pytest
from app.models.usuario_model import Usuario
from app.config.database import db

@pytest.fixture
def usuario_valido():
    usuario = Usuario("Marta", "marta@gmail.com", "1234")
    return usuario

def test_validar_nome(usuario_valido):
    assert usuario_valido.nome == "Marta"

def test_validar_email(usuario_valido):
    assert usuario_valido.email == "marta@gmail.com"

def test_validar_senha(usuario_valido):
    assert usuario_valido.senha == "1234"

def test_nome_invalido(usuario_valido):
    with pytest.raises(TypeError, match="O nome deve ser um texto"):
        Usuario(999, "marta@gmail.com", "1234")