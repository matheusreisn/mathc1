import os
import time

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

inventario = []

# Função para salvar os dados no .txt
def salvar_inventario():
    with open("inventario.txt", "w") as arquivo:
        for produto in inventario:
            linha = f"{produto[0]},{produto[1]},{produto[2]},{produto[3]},{produto[4]}\n"
            arquivo.write(linha)

# Função para carregar os dados do .txt
def carregar_inventario():
    try:
        with open("inventario.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                produto = [int(dados[0]), dados[1], dados[2], int(dados[3]), float(dados[4])]
                inventario.append(produto)
    except FileNotFoundError:
        pass

# Função para adicionar produto ao inventário
def adicionar_produto():
    def obter_codigo():
        while True:
            try:
                codigo = int(input("Digite o código do produto: "))
                if codigo < 0:
                    print("Erro! Digite um número válido.")
                elif any(produto[0] == codigo for produto in inventario): 
                    print("Erro! Código já existente no inventário.")
                else:
                    return codigo
            except ValueError:
                print("Erro! Digite apenas numeros.")

    def obter_categoria():
        while True:
            categoria = input("Digite a categoria do produto: ").strip()
            if categoria.isalpha():
                return categoria
            else:
                print("Erro! Digite uma categoria válida (Apenas letras).")

    def obter_produto():
        while True:
            produto = input("Digite o nome do produto: ").strip()
            if produto and all(c.isalpha() or c.isspace() or c == '-' for c in produto):
                return produto
            else:
                print("Erro! Digite um nome válido (Apenas letras).")

    def obter_quantidade():
        while True:
            try:
                quantidade = int(input("Digite a quantidade do produto: "))
                if quantidade < 0:
                    print("Erro! Digite um número válido.")
                else:
                    return quantidade
            except ValueError:
                print("Erro! Digite apenas numeros.")

    def obter_preco():
        while True:
            try:
                preco = float(input("Digite o preço do produto: "))
                if preco < 0:
                    print("Erro! Digite um número válido.")
                else:
                    return preco
            except ValueError:
                print("Erro! Digite um número válido.")

    codigo = obter_codigo()
    categoria = obter_categoria()
    produto = obter_produto()
    quantidade = obter_quantidade()
    preco = obter_preco()
    
    inventario.append([codigo, categoria, produto, quantidade, preco])
    print('''Produto adicionado ao inventário com sucesso!
    ''')
    salvar_inventario()
# Função para excluir produto do inventário
def excluir_produto():
    try:
        codigo = int(input("Digite o código do produto que deseja excluir: "))
    except ValueError:
        print("Erro! Digite um número válido.")
        return

    for produto in inventario:
        if produto[0] == codigo:
            inventario.remove(produto)
            print("Produto excluído do inventário com sucesso!")
            return
    print("Produto não encontrado!")
    salvar_inventario()

# Função para alterar produto do inventário
def alterar_produto():
    try:
        codigo = int(input("Digite o código do produto que deseja alterar: "))
    except ValueError:
        print("Erro! Digite um número válido.")
        return

    for produto in inventario:
        if produto[0] == codigo:
            novo_produto = input("Digite o novo nome do produto: ")
            nova_categoria = input("Digite a nova categoria do produto: ")
            try:
                nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                novo_preco = float(input("Digite o novo preço do produto: "))
            except ValueError:
                print("Erro! Digite valores numéricos válidos.")
                return

            produto[2] = novo_produto
            produto[1] = nova_categoria
            produto[3] = nova_quantidade
            produto[4] = novo_preco
            print("Produto alterado com sucesso!")
            return
    print("Produto não encontrado no inventário.")
    salvar_inventario()

# Função de relatório geral dos produtos
def relatorio_geral():
    print("Relatório geral do inventário: ")
    for produto in inventario:
        print(f"Nome: {produto[2]}, Categoria: {produto[1]}, Código: {produto[0]}, Quantidade: {produto[3]}, Preço: {produto[4]}")
    print("Fim do relatório.")

# Função de relatório pela categoria
def relatorio_categoria():
    categoria = input("Digite a categoria dos produtos que deseja ver: ")
    print("Relatório dos produtos da categoria: ", categoria)
    for produto in inventario:
        if produto[1].lower() == categoria.lower() and categoria.isalpha():
            print(f"Nome: {produto[2]}, Código: {produto[0]}, Quantidade: {produto[3]}, Preço: {produto[4]}")
    print("Fim do relatório.")

# Função de relatório por preço
def relatorio_preco():
    try:
        preco = float(input("Digite o preço dos produtos que deseja ver: "))
    except ValueError:
        print("Erro! Digite um valor numérico válido.")
        return

    print("Relatório dos produtos com preço menor que: ", preco)
    for produto in inventario:
        if produto[4] < preco:
            print(f"Nome: {produto[2]}, Código: {produto[0]}, Quantidade: {produto[3]}, Preço: {produto[4]}")
    print("Fim do relatório.")

# Menu principal do inventário
def menu():
    while True:
        input("Pressione para acessar o menu.")
        print ('')
        limpar_tela()
        print(''' 
███╗░░░███╗███╗░░░███╗██╗░░██╗███████╗  ░█████╗░████████╗░█████╗░░█████╗░░█████╗░██████╗░██╗░██████╗████████╗░█████╗░
████╗░████║████╗░████║██║░░██║╚════██║  ██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗
██╔████╔██║██╔████╔██║███████║░░███╔═╝  ███████║░░░██║░░░███████║██║░░╚═╝███████║██║░░██║██║╚█████╗░░░░██║░░░███████║
██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══╝░░  ██╔══██║░░░██║░░░██╔══██║██║░░██╗██╔══██║██║░░██║██║░╚═══██╗░░░██║░░░██╔══██║
██║░╚═╝░██║██║░╚═╝░██║██║░░██║███████╗  ██║░░██║░░░██║░░░██║░░██║╚█████╔╝██║░░██║██████╔╝██║██████╔╝░░░██║░░░██║░░██║
╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝

Olá, seja bem-vindo ao menu do inventário:
1. Adicionar produto
2. Excluir produto
3. Alterar produto
4. Relatório geral
5. Relatório por categoria
6. Relatório por preço
7. Sair''')
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                adicionar_produto()
            elif opcao == 2:
                excluir_produto()
            elif opcao == 3:
                alterar_produto()
            elif opcao == 4:
                relatorio_geral()
            elif opcao == 5:
                relatorio_categoria()
            elif opcao == 6:
                relatorio_preco()
            elif opcao == 7:
                print("Saindo do inventário...")
                salvar_inventario()
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida, digite um número.")


# Carregar os dados armazenados primeiro e iniciar o menu
carregar_inventario()
menu()
limpar_tela()
