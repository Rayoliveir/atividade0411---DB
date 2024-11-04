from service.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

# Cores de texto
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
ORANGE = "\033[38;5;214m"
CIANO = "\033[96m"
PINK = "\033[35m"
RESET = "\033[0m"

def limpa_tela():
    os.system("cls || clear")
    print(f" {CIANO}*==== BEM VINDO A BANQUETOLA ====*{RESET}\n")


def menu():
    limpa_tela()
    print(f"{CIANO} |================================|{RESET}")
    print(f"{CIANO} |       MENU DE OPÇÕES           |{RESET}")
    print(f"{CIANO} |================================|{RESET}")
    print(f"{GREEN} | 1 | CREATE - Salvar            |{RESET}")
    print(f"{BLUE} | 2 | UPDATE  - Atualizar        |{RESET}")
    print(f"{RED} | 3 | DELETE - Deletar           |{RESET}")
    print(f"{ORANGE} | 4 | ONLY READ - Consulta única |{RESET}")
    print(f"{YELLOW} | 5 | ALL READ - Consulta geral  |{RESET}")
    print(f"{CIANO} |================================|{RESET}")
    print(f"{PINK} | 6 |     PARAR O PROGRAMA       |{RESET}")
    print(f"{CIANO} |================================|{RESET}")

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)
    
    # Solicitando dados para o usuário
    while True:
        menu()
        opcao = int(input("\nDigite a opção desejada: "))

        match(opcao):
            case 1:
                print("\n - Adicionando usuário -")
                nome = input("Digite o seu nome: ")
                email = input("Digite o seu email: ")
                senha = input("Digite o seu senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)
                break

            case 2:
                print("\n - Pesquisa por email -")
                email = input("Digite o email desejado: ")
                lista_email = repository.pesquisar_usuario_por_email(email=email)
                for usuario in lista_email:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                break

            case 3:
                print("\n - Atualização de dados -")
                break

            case 4:
                print("\n - Excluir usuário -")
                nome = input("Digite o nome: ")
                email = input("Digite o email: ")
                senha = input("Digite o senha: ")

                repository.excluir_usuario()
                break

            case 5:
                print("\n - Exibir todos os usuários cadastrados -")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                break

            case 0:
                break

if __name__ == "__main__":
    os.system("cls || clear")
    main()