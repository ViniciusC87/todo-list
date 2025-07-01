# todo.py

# Lista para armazenar as tarefas
tasks = []
next_id = 1

def add_task(tasks, next_id):
    """Adiciona uma nova tarefa à lista com descrição, status e prioridade."""
    description = input("Digite a descrição da tarefa: ")
    
    # Solicita a prioridade e valida a entrada
    priority_input = input("Digite a prioridade (Alta, Média, Baixa): ").strip().lower()
    if priority_input == 'alta':
        priority = 'Alta'
    elif priority_input == 'media':
        priority = 'Média'
    elif priority_input == 'baixa':
        priority = 'Baixa'
    else:
        print("Prioridade inválida. Definindo como 'Baixa' por padrão.")
        priority = 'Baixa'

    task = {
        'id': next_id,
        'description': description,
        'status': 'pendente',
        'priority': priority # Adicionado campo de prioridade
    }
    tasks.append(task)
    print(f"Tarefa '{description}' (ID: {next_id}) adicionada com prioridade '{priority}'.")
    return next_id + 1

def view_tasks(tasks):
    """Visualiza todas as tarefas na lista."""
    if not tasks:
        print("Nenhuma tarefa na lista.")
        return

    print("\n--- Suas Tarefas ---")
    for task in tasks:
        # Exibe a prioridade junto com as outras informações
        print(f"ID: {task['id']} | Descrição: {task['description']} | Status: {task['status']} | Prioridade: {task['priority']}")
    print("--------------------")

def mark_completed(tasks):
    """Marca uma tarefa como concluída."""
    view_tasks(tasks) # Mostra as tarefas para o usuário escolher
    if not tasks:
        return

    try:
        task_id = int(input("Digite o ID da tarefa para marcar como concluída: "))
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return

    found = False
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'concluída'
            print(f"Tarefa '{task['description']}' (ID: {task_id}) marcada como concluída.")
            found = True
            break
    if not found:
        print(f"Tarefa com ID {task_id} não encontrada.")

def remove_task(tasks):
    """Remove uma tarefa da lista."""
    view_tasks(tasks) # Mostra as tarefas para o usuário escolher
    if not tasks:
        return

    try:
        task_id = int(input("Digite o ID da tarefa para remover: "))
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return

    original_len = len(tasks)
    tasks[:] = [task for task in tasks if task['id'] != task_id] # Remove a tarefa
    if len(tasks) < original_len:
        print(f"Tarefa com ID {task_id} removida.")
    else:
        print(f"Tarefa com ID {task_id} não encontrada.")

def edit_task_description(tasks):
    """Permite ao usuário editar a descrição de uma tarefa existente."""
    if not tasks:
        print("Não há tarefas para editar.")
        return

    view_tasks(tasks) # Mostra as tarefas para o usuário escolher
    try:
        task_id_to_edit = int(input("Digite o ID da tarefa que deseja editar: "))
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return

    found_task = None
    for task in tasks:
        if task['id'] == task_id_to_edit:
            found_task = task
            break

    if found_task:
        print(f"Descrição atual da tarefa {found_task['id']}: {found_task['description']}")
        new_description = input("Digite a nova descrição para a tarefa: ")
        
        if new_description.strip(): # Garante que a nova descrição não seja vazia
            found_task['description'] = new_description.strip()
            print(f"Descrição da tarefa {found_task['id']} atualizada com sucesso!")
        else:
            print("A nova descrição não pode ser vazia. Nenhuma alteração feita.")
    else:
        print(f"Erro: Tarefa com ID {task_id_to_edit} não encontrada.")

def display_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Editar Descrição da Tarefa") # Nova opção
    print("6. Sair")
    print("------------------------------")

def main():
    """Função principal que executa o programa."""
    global next_id # Permite modificar a variável global next_id
    
    while True:
        display_menu()
        choice = input("Escolha uma opção: ").strip()

        if choice == '1':
            next_id = add_task(tasks, next_id)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5': # Nova opção para editar descrição
            edit_task_description(tasks)
        elif choice == '6':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida do menu.")

if __name__ == "__main__":
    main()
