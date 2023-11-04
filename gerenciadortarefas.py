import json

# Função para carregar tarefas do arquivo JSON
def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
    return tarefas

# Função para salvar tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# Função para listar tarefas
def listar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i}. {tarefa["descricao"]} - {"Concluída" if tarefa["concluida"] else "Pendente"}')

# Função principal do aplicativo
def main():
    tarefas = carregar_tarefas()

    while True:
        print('\n=== Gerenciador de Tarefas ===')
        print('1. Listar Tarefas')
        print('2. Adicionar Tarefa')
        print('3. Marcar Tarefa como Concluída')
        print('4. Remover Tarefa')
        print('5. Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            if not tarefas:
                print('Nenhuma tarefa cadastrada.')
            else:
                listar_tarefas(tarefas)

        elif escolha == '2':
            descricao = input('Digite a descrição da tarefa: ')
            tarefa = {'descricao': descricao, 'concluida': False}
            tarefas.append(tarefa)
            salvar_tarefas(tarefas)
            print('Tarefa adicionada com sucesso.')

        elif escolha == '3':
            listar_tarefas(tarefas)
            numero = int(input('Digite o número da tarefa a ser marcada como concluída: '))
            if 1 <= numero <= len(tarefas):
                tarefas[numero - 1]['concluida'] = True
                salvar_tarefas(tarefas)
                print('Tarefa marcada como concluída.')
            else:
                print('Número de tarefa inválido.')

        elif escolha == '4':
            listar_tarefas(tarefas)
            numero = int(input('Digite o número da tarefa a ser removida: '))
            if 1 <= numero <= len(tarefas):
                tarefas.pop(numero - 1)
                salvar_tarefas(tarefas)
                print('Tarefa removida com sucesso.')
            else:
                print('Número de tarefa inválido.')

        elif escolha == '5':
            print('Obrigado por usar o Gerenciador de Tarefas. Até a próxima!')
            break

        else:
            print('Opção inválida. Escolha uma opção válida.')

if __name__ == '__main__':
    main()