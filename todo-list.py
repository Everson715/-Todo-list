import json
import os

# Define the file path for storing the to-do list
NAME_FILE = "todo_list.json"

def load_todo_list():
    """Load the to-do list from the JSON file."""
    if not os.path.exists(NAME_FILE):
        return []
    try:
        with open(NAME_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If the file is corrupted or empty, return an empty list
        print(f"⚠️ Aviso: O arquivo '{NAME_FILE}' está vazio ou corrompido. Criando uma nova lista.")
        return []

# Save the to-do list to the JSON file
def save_todo_list(todo_list):
    """Save the todo list to the JSON file."""
    with open(NAME_FILE, 'w', encoding='utf8') as f:
        # CORREÇÃO original: ensure_ascii=False
        json.dump(todo_list, f, ensure_ascii=False, indent=4)

# create a new to-do item
def add_todo_item(todo_list):
    """ Create a new to-do item and add it to the list."""
    item = input("Digite a descrição da nova tarefa: ").strip()
    if item:
        # O ID deve ser baseado no ID máximo existente para evitar colisões
        if todo_list:
            next_id = max(t['id'] for t in todo_list) + 1
        else:
            next_id = 1
            
        tarefa = {
            'id': next_id, # Usando o ID sequencial correto
            'item': item,
            'concluida': False
        }
        todo_list.append(tarefa)
        save_todo_list(todo_list)
        print(f"\n✅ Tarefa '{item}' adicionada com sucesso!")
    else:
        print("\n❌ A descrição da tarefa não pode ser vazia.")

# View all to-do items
def view_todo_list(todo_list):
    """Exibe todas as tarefas com seus status."""
    if not todo_list:
        print("\nSua lista de tarefas está vazia!")
        return

    print("\n--- SUAS TAREFAS ---")
    for tarefa in todo_list:
        status = "[X]" if tarefa['concluida'] else "[ ]"
        print(f"{tarefa['id']}. {status} {tarefa['item']}") 
    print("--------------------")

# Delete a to-do item
def delete_todo_item(todo_list):
    """Delete a to-do item by its ID."""
    view_todo_list(todo_list)
    if not todo_list:
        return
    
    try:
        item_id = int(input("Digite o ID da tarefa que deseja deletar: "))
    except ValueError:
        print("\n❌ ID inválido. Por favor, insira um número válido.")
        return
    
    # Cria uma nova lista excluindo a tarefa com o ID fornecido
    tarefas_mantidas = [t for t in todo_list if t['id'] != item_id]
    
    if len(tarefas_mantidas) < len(todo_list):
        # Encontrada e removida: Atualiza os IDs das tarefas restantes para manter a ordem
        for i, t in enumerate(tarefas_mantidas, 1):
            t['id'] = i # Reindexa
            
        # Atualiza a lista original com os dados reindexados
        todo_list[:] = tarefas_mantidas
        save_todo_list(todo_list)
        print(f"\n🗑️ Tarefa com ID {item_id} removida e lista reordenada com sucesso!")
    else:
        print(f"\n❌ Tarefa com ID {item_id} não encontrada.")
# Mark a to-do item as completed
def mark_todo_completed(todo_list):
    """Mark a to-do item as completed by its ID."""
    view_todo_list(todo_list)
    if not todo_list:
        return
    
    try:
        item_id = int(input("Digite o ID da tarefa que deseja marcar como concluída: "))
    except ValueError:
        print("\n❌ ID inválido. Por favor, insira um número válido.")
        return
    
    for tarefa in todo_list:
        if tarefa['id'] == item_id:
            tarefa['concluida'] = True
            save_todo_list(todo_list)
            print(f"\n✅ Tarefa com ID {item_id} marcada como concluída!")
            return
    
    print(f"\n❌ Tarefa com ID {item_id} não encontrada.")

# Main program loop
def main():
    todo_list = load_todo_list()
    
    while True:
        print("\n--- MENU DE TAREFAS ---")
        print("1. Adicionar nova tarefa")
        print("2. Ver todas as tarefas")
        print("3. Deletar uma tarefa")
        print("4. Marcar tarefa como concluída")
        print("5. Sair")
        
        choice = input("Escolha uma opção (1-5): ").strip()
        
        if choice == '1':
            add_todo_item(todo_list)
        elif choice == '2':
            view_todo_list(todo_list)
        elif choice == '3':
            delete_todo_item(todo_list)
        elif choice == '4':
            mark_todo_completed(todo_list)
        elif choice == '5':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("\n❌ Opção inválida. Por favor, escolha uma opção entre 1 e 5.")
if __name__ == "__main__":
    main()