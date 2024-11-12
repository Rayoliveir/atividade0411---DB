from app.models.usuario_model import Usuario
from app.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository
    
    def criar_usuario(self):
        try:
            print("\n - Adicionando usuário -")
            nome = input("Digite o seu nome: ")
            email = input("Digite o seu email: ")
            senha = input("Digite o seu senha: ")
            usuario = Usuario(nome=nome, email=email, senha=senha)
            
            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return
            
            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")

    
    def atualizar_usuario(self):
        try:
            email = input("informe o email do usuário: \n")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                cadastrado.nome = input("digite seu nome: \n")
                cadastrado.email = input("digite seu email: \n")
                cadastrado.senha = input("digite sua senha: \n")
                print("usuário atualizado com sucesso!")
                self.repository.salvar_usuario(cadastrado)
            print("usuário não encontrado")
            return
        
        except TypeError as erro:
            print(f"erro ao atualizar usuário: {erro}")
        except Exception as erro:
            print(f"erro inesperado: {erro}")
        

    def excluir_usuario(self):
        try:
            email = input("informe o email desse usuário: \n")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                senha = input("confirme a senha do usuário: \n")

                if senha == cadastrado.senha:
                    self.repository.excluir_usuario(cadastrado)
                    print("usuário excluído com sucesso")
                print("senha inválida!")
                return
            print("usuário não encontrado!")
            return

        except TypeError as erro:
            print(f"erro ao excluir usuário: {erro}")
        except Exception as erro:
            print(f"erro inesperado: {erro}")
    
        
    def pesquisar_usuario_unico(self):
        try:
            email = input("informe o email do usuário: \n")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                print("usuário encontrado!")
                print(f"Nome: {cadastrado.nome} \nE-mail: {cadastrado.email} \nSenha: {cadastrado.senha}")
                return
            print("usuário não encontrado")
            return
        
        except TypeError as erro:
            print(f"erro ao procurar o usuário: {erro}")
        except Exception as erro:
            print(f"erro inesperado: {erro}")
    
    
    def listar_todos_usuarios(self):
        lista_usuarios = self.repository.listar_todos_usuarios()
        print("\nListando todos os usuarios")
        for usuario in lista_usuarios:
            print(f"\nID: {usuario.id} \nNome: {usuario.nome} \nE-mail: {usuario.email} \nSenha: {usuario.senha}")