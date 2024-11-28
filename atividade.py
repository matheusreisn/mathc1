alunos = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    matricula = int(input('Ano de matricula: '))
    salario = float(input('Digite o salario: '))
    
    alunos.append (f'{nome, matricula, salario}')
    
    continuar = input('Deseja adicionar mais alunos? [S/N] ').lower()
    
    if continuar == 'n':
        break
    elif continuar != 's':
        print("Opção inválida. Por favor, digite S ou N.")
        continue
while True:
    opcao = int(input('''Escolha uma opção:
[1] Inclusão
[2] Alteração de dados da matrícula
[3] Exclusão baseada na matrícula
[4] Relatório geral
[5] Pesquisa por nome
[6] Saida
'''))
    if opcao == 1:
        print (f'Parabens! Os alunos {alunos} estão matriculados na universidade!')
    elif opcao == 2:
        alteracao = input('Deseja alterar dados inseridos: [S/N] ').lower()
        if alteracao == 's':
            nome = str(input('Nome do aluno: '))
            matricula = int(input('Ano de matricula: '))
            salario = float(input('Digite o salario: '))
            print("Dados da matrícula alterados com sucesso. ")
            break
        elif alteracao == 'n':
            print (f'Matricula do aluno {nome} sem alteração. ')
        else:
            print("Opção inválida. Tente novamente.")
    elif opcao == 3:
                exluir = input('Deseja exluir qual nome: ')
                print ('Nome excluido com sucesso')
    elif opcao == 4:
        print (f'O {alunos} é aluno da universidade desde {matricula} e recebe R${salario :.2f} ')
    elif opcao == 5:
        print (f'O {nome} se encontra no sistema dos alunos desde {matricula}.')
    elif opcao == 6:
        print ('Programa encerrado!')
        break