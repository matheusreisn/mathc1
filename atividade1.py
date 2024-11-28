import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

inventario = []

def salvar_inventario():
    with open("inventario.txt", "w") as arquivo:
        for produto in inventario:
            linha = (f"{produto[0]},{produto[1]},{produto[2]},{produto[3]},{produto[4]}")
            arquivo.write(linha)
    messagebox.showinfo("Sucesso", "Inventário salvo com sucesso!")

#adicionar produto ao inventario
def adicionar_produto():
    codigo = simpledialog.askinteger("Código do produto", "Digite o código do produto:") #codigo do produto
    if codigo is None or codigo < 0: #para nao permitir numero negativo
        messagebox.showerror("Erro", "Código inválido!")
        return
    
    categoria = simpledialog.askstring("Categoria do produto", "Digite a categoria do produto:") #categoria do produto
    if categoria is None or not categoria.isalpha(): #isalpha para ler apenas letras
        messagebox.showerror("Erro", "Categoria inválida!")
        return
    
    produto = simpledialog.askstring("Nome do produto", "Digite o nome do produto:") #nome do produto
    if produto is None or not all(c.isalpha() or c.isspace() or c == '-' for c in produto):
        messagebox.showerror("Erro", "Nome do produto inválido!")
        return
        #all (c.isalpha() para reconhecer so as letras
    #c.isspace() para ler os espaços q tava dando erro quando eu colocava alguma palavra com espaço

    #e o or c== '-' para reconhecer traço no caso da 'Coca-Cola'

    #o all eh para ver se todas as condicoes sao verdadeiras

    #e ainda nao entendi muito bem para que serve o C nesse codigo mas eh meio que uma referencia pro codigo, depois pesquiso melhor

    #se forem usar caracteres especiais ou espaços e outros inputs, copia isso ai que da certo, so mudar o '-'

    #em com IA isso tava dando certo, agora que DEU PELO AMOR DE DEUS NAO MEXA NISSO É UMA BOMBA E VAI QUEBRAR TUDO

    quantidade = simpledialog.askinteger("Quantidade do produto", "Digite a quantidade do produto:") #quantidade do produto
    if quantidade is None or quantidade < 0:
        messagebox.showerror("Erro", "Quantidade inválida!")
        return
    
    preco = simpledialog.askfloat("Preço do produto", "Digite o preço do produto:") #preco do produto
    if preco is None or preco < 0: #para incluir preco 0
        messagebox.showerror("Erro", "Preço inválido!")
        return
    
    inventario.append([codigo, categoria, produto, quantidade, preco])
    messagebox.showinfo("Sucesso", f"Produto {produto} adicionado ao inventário com sucesso!")

# excluir produto do inventario
def excluir_produto():
    codigo = simpledialog.askinteger("Código do produto", "Digite o código do produto que deseja excluir:") #por try e except aq
    if codigo is None:
        return
    for produto in inventario:
        if produto[0] == codigo: #usar o índice correto
            inventario.remove(produto) #pra por o novo nome do produto
            messagebox.showinfo("Sucesso", "Produto excluído do inventário com sucesso!") 
            return
    messagebox.showerror("Erro", "Produto não encontrado!")

# alterar produto do inventario
def alterar_produto():
    codigo = simpledialog.askinteger("Código do produto", "Digite o código do produto que deseja alterar:")
    if codigo is None:
        return
    for produto in inventario:
        if produto[0] == codigo:
            novo_produto = simpledialog.askstring("Nome do produto", "Digite o novo nome do produto:")
            nova_categoria = simpledialog.askstring("Categoria do produto", "Digite a nova categoria do produto:")
            nova_quantidade = simpledialog.askinteger("Quantidade do produto", "Digite a nova quantidade do produto:")
            novo_preco = simpledialog.askfloat("Preço do produto", "Digite o novo preço do produto:")

            if novo_produto:
                produto[2] = novo_produto
            if nova_categoria:
                produto[1] = nova_categoria
            if nova_quantidade is not None:
                produto[3] = nova_quantidade
            if novo_preco is not None:
                produto[4] = novo_preco

            messagebox.showinfo("Sucesso", "Produto alterado com sucesso!")
            return
    messagebox.showerror("Erro", "Produto não encontrado no inventário.")

# relatorio geral dos produtos
def relatorio_geral():
    relatorio = "Relatório geral do inventário:\n\n"
    for produto in inventario:
        relatorio += (f"Nome: {produto[2]}, Categoria: {produto[1]}, Código: {produto[0]}, Quantidade: {produto[3]}, Preço: {produto[4]}")
    messagebox.showinfo("Relatório Geral", relatorio)

# relatorio pela categoria
def relatorio_categoria():
    categoria = simpledialog.askstring("Categoria", "Digite a categoria dos produtos que deseja ver:") #por correcao
    if categoria is None:
        return
    relatorio = (f"Relatório dos produtos da categoria: {categoria}")
    for produto in inventario: 
        if produto[1].lower() == categoria.lower(): #usar o índice correto
            relatorio += (f"Nome: {produto[2]}, Código: {produto[0]}, Quantidade: {produto[3]}, Preço: {produto[4]}")
    messagebox.showinfo("Relatório por Categoria", relatorio)

# relatorio por preço
def relatorio_preco():
    preco = simpledialog.askfloat("Preço", "Digite o preço dos produtos que deseja ver:")
    if preco is None:
        return
    relatorio = (f"Relatório dos produtos com preço menor que: {preco}")
    for produto in inventario:
        if produto[4] < preco: # para incluir produtos igual ao do preço digitado
            relatorio += (f"Nome: {produto[2]}, Código: {produto[0]}, Quantidade: {produto[3]}, Preço: {produto[4]}")
    messagebox.showinfo("Relatório por Preço", relatorio)

# menu principal do inventário
def menu():
    root = tk.Tk()
    root.title("𝙼𝙼𝙷𝚉 𝙰𝚃𝙰𝙲𝙰𝙳𝙸𝚂𝚃𝙰")
    style = ttk.Style(root)
    style.theme_use("clam")

    root.configure(background="#f0f0f0")

    title = tk.Label(root, text="MMHZ ATACADISTA", font=("Helvetica", 16, "bold"), background="#f0f0f0", foreground="#333333")
    title.pack(pady=10)

    subtitle = tk.Label(root, text="Olá, seja bem-vindo ao menu do inventário:", background="#f0f0f0", foreground="#333333")
    subtitle.pack()

    btn_style = {"fill": tk.X, "padx": 5, "pady": 5}

    ttk.Button(root, text="Adicionar produto", command=adicionar_produto).pack(**btn_style)
    ttk.Button(root, text="Excluir produto", command=excluir_produto).pack(**btn_style)
    ttk.Button(root, text="Alterar produto", command=alterar_produto).pack(**btn_style)
    ttk.Button(root, text="Relatório geral", command=relatorio_geral).pack(**btn_style)
    ttk.Button(root, text="Relatório por categoria", command=relatorio_categoria).pack(**btn_style)
    ttk.Button(root, text="Relatório por preço", command=relatorio_preco).pack(**btn_style)
    ttk.Button(root, text="Sair", command=lambda: [salvar_inventario(), root.quit()]).pack(**btn_style)

    footer = tk.Label(root, text="𝘊𝘰𝘱𝘺𝘳𝘪𝘨𝘩𝘵 © 2024. 𝘈𝘭𝘭 𝘳𝘪𝘨𝘩𝘵𝘴 𝘳𝘦𝘴𝘦𝘳𝘷𝘦𝘥 𝘣𝘺 𝘔𝘔𝘏𝘡 𝘈𝘵𝘢𝘤𝘢𝘥𝘪𝘴𝘵𝘢.", font=("Helvetica", 8), background="#f0f0f0", foreground="#333333")
    footer.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()


#quando fazer o arquivo .txt colocar pra carregar os dados armazenados primeiro, antes de chamar o menu

# chamar o menu
menu()
