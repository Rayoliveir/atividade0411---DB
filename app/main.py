import sys
import os
import time

#Adiciona o diretório 'app' como diretório padrão
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from app.service.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository
from app.config.database import Session

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
    print(f"{PINK} | 0 |     PARAR O PROGRAMA       |{RESET}")
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
                service.criar_usuario()
                input("Aperte qualquer tecla para continuar!")
            
            case 2:
                service.atualizar_usuario()
                input("Aperte qualquer tecla para continuar!")

            case 3:
                service.excluir_usuario()
                input("Aperte qualquer tecla para continuar!")

            case 4:
                service.pesquisar_usuario_unico()
                input("Aperte qualquer tecla para continuar!")

            case 5:
                service.listar_todos_usuarios()
                input("Aperte qualquer tecla para continuar!")

            case 0:
                input("Aperte qualquer tecla para continuar!")
                time.sleep(5)
                print("Programa encerrado!")

            case _:
                print("Opção selecionada inválida!")
                break

if __name__ == "__main__":
    os.system("cls || clear")
    main()
