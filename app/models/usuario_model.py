from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db


Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True)
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._verificar_nome(nome)
        self.email = self._verficar_email(email)
        self.senha = self._verficar_senha(senha)
    
    def _verificar_nome(self, valor):
        try:
            self._verificar_nome_invalido(valor)
            self._verificar_nome_vazio(valor)
        except TypeError as e:
            raise TypeError(f"erro: {e}")
        self.nome = valor
        return self.nome
    
    def _verificar_nome_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("o nome deve ser um texto")
        return valor
    
    def _verificar_nome_vazio(self, valor):
        if not valor.strip():
            raise TypeError("o nome não pode estar vazio")
        return valor
        
    def _verficar_email(self, valor):
        try:
            self._verificar_email_invalido(valor)
            self._verificar_email_vazio(valor)
        except TypeError as e:
            raise TypeError(f"erro: {e}")
        self.email = valor
        return self.email

    def _verificar_email_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("o email deve ser um texto")
        return valor
        
    def _verificar_email_vazio(self,valor):
        if not valor.strip():
            raise TypeError("o email não pode estar vazio")
        return valor
    
    def _verficar_senha(self, valor):
        try:
            self._verificar_senha_invalida(valor)
            self._verificar_senha_vazia(valor)
        except TypeError as e:
            raise TypeError(f"erro: {e}")
        self.senha = valor
        return self.senha

    def _verificar_senha_invalida(self,valor):
        if not isinstance(valor, str):
            raise TypeError("a senha deve ser um texto")
        return valor
    
    def _verificar_senha_vazia(self,valor):
        if not valor.strip():
            raise TypeError("a senha não pode estar vazia")
        return valor
    

# Criando tabela no banco de dados
Base.metadata.create_all(bind=db)