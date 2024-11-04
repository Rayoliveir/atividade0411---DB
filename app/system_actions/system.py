import time


session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)
    

# Create - Insert - Salvar == 1
def create():
    time.sleep(5)
    print("\n*== CADASTRO DE NOVO USUARIO ==* ")
    inserir_nome = input("Digite seu nome: ")
    inserir_sobrenome = input("Digite seu sobrenome: ")
    inserir_email = input("Digite seu email: ")
    inserir_senha = input("Digite sua senha: ")

    cliente = Cliente(nome=inserir_nome, sobrenome=inserir_sobrenome, email=inserir_email, senha=inserir_senha)
    session.add(cliente)
    session.commit()


# U - Update - UPDATE - Atualizar == 2
def update():
    time.sleep(5)
    print("\n*== ATUALIZAR DADOS DO USUARIO ==* ")
    email_cliente = input("\nDigite o e-mail do cliente que será atualizado: ")

    cliente = session.query(Cliente).filter_by(email = email_cliente).first()

    if cliente:
        cliente.nome = input("Digite seu nome: ")
        cliente.sobrenome = input("Digite seu sobrenome: ")
        cliente.email = input("Digite seu email: ")
        cliente.senha = input("Digite sua senha: ")

        session.commit()

    else:
        print("Cliente não encontrado. ")

# D - Delete - DELETE - Excluir == 3
def delete():
    time.sleep(5)
    print("\n*== EXCLUIR DADOS DO USUARIO ==*")
    email_cliente = input("\nDigite o e-mail do cliente que será excluído: ")

    cliente = session.query(Cliente).filter_by(email = email_cliente).first()

    if cliente:
        session.delete(cliente)
        session.commit()
        print(f"Cliente {cliente.nome} excluido com sucesso!")

    else:
        print("Cliente não encontrado. ")

# R - Read - Select - Consulta (UNICA) == 4
def only_read():

        print("\n*== CONSULTAR DADOS DO USUARIO ==*")
        email_cliente = input("\nDigite o e-mail do cliente: ")

        cliente = session.query(Cliente).filter_by(email = email_cliente).first()

        if cliente:
            print(f"R.A.:{cliente.ra} \nNome completo: {cliente.nome} {cliente.sobrenome} \nE-mail: {cliente.email} \nSenha: {cliente.senha}")
        else:
            print("Cliente não encontrado!")

        input("\nAperte qualquer tecla para voltar ao menu de opções! ")

# R - Read - Select - Consulta geral == 5
def all_read():
    print("\n*== EXIBINDO DADOS DE TODOS OS USUARIOS ==*")
    lista_clientes = session.query(Cliente).all()

    for cliente in lista_clientes:
        print(f"\n\nR.A.:{cliente.ra} \nNome completo: {cliente.nome} {cliente.sobrenome} \nE-mail: {cliente.email} \nSenha: {cliente.senha}")

    input("\nAperte qualquer tecla para voltar ao menu de opções!")