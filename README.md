# 📝 CLI To-Do List Manager

Um gerenciador de tarefas robusto e leve baseado em **Interface de Linha de Comando (CLI)**. Desenvolvido em Python, esta aplicação foca na simplicidade e eficiência, utilizando arquivos JSON para garantir a persistência segura dos dados entre as sessões.

## ✨ Funcionalidades

O sistema foi projetado para cobrir o ciclo de vida completo de gerenciamento de tarefas:

  * **➕ Adicionar Tarefas:** Criação rápida de novas entradas com descrições personalizadas e geração automática de IDs únicos.
  * **👀 Visualização Detalhada:** Listagem tabular de todas as tarefas, exibindo IDs e indicadores visuais de status (Pendente/Concluído).
  * **✅ Controle de Status:** Mecanismo para marcar tarefas como concluídas `[X]`, permitindo fácil rastreamento de progresso.
  * **🗑️ Remoção de Dados:** Funcionalidade para deletar permanentemente tarefas obsoletas ou errôneas.
  * **💾 Persistência Automática:** Sistema de *auto-save* em `todo_list.json`, garantindo que nenhum dado seja perdido ao fechar o terminal.

## 🛠️ Tecnologias Utilizadas

  * **Linguagem:** [Python 3](https://www.python.org/)
  * **Armazenamento de Dados:** JSON (JavaScript Object Notation) - Biblioteca nativa `json`.
  * **Interface:** Terminal/Console padrão do sistema operacional.

## 🚀 Como Executar

Siga as etapas abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em seu sistema.

```bash
python --version
# Ou
python3 --version
```

### Instalação e Execução

1.  **Clone o repositório ou salve o arquivo:**
    Se você tiver o código em um arquivo, salve-o como `todo_app.py`.

2.  **Navegue até o diretório do projeto:**
    Abra seu terminal e acesse a pasta onde o arquivo foi salvo.

    ```bash
    cd caminho/para/seu/arquivo
    ```

3.  **Execute a aplicação:**
    Rode o seguinte comando para iniciar o gerenciador:

    ```bash
    python todo_app.py
    # Caso seu sistema exija, use: python3 todo_app.py
    ```

## 📂 Estrutura do Projeto

A estrutura de arquivos é simples e direta:

```
/
├── todo_app.py       # Código fonte principal da aplicação
├── todo_list.json    # Arquivo de banco de dados (gerado automaticamente)
└── README.md         # Documentação do projeto
```

## 🤝 Contribuição

Contribuições são bem-vindas\! Se você tiver sugestões de melhorias, sinta-se à vontade para:

1.  Fazer um **Fork** do projeto.
2.  Criar uma **Branch** para sua feature (`git checkout -b feature/NovaFeature`).
3.  Fazer o **Commit** (`git commit -m 'Adiciona NovaFeature'`).
4.  Fazer o **Push** (`git push origin feature/NovaFeature`).
5.  Abrir um **Pull Request**.

-----

*Desenvolvido com 🐍 Python.*
