 1 | def adicionar_tarefa(tarefas, descricao, prioridade):
 2 |     """
 3 |     Adiciona uma nova tarefa à lista com descrição e prioridade.
 4 |     """
 5 |     if descricao and prioridade:
 6 |         nova_tarefa = {
 7 |             "descricao": descricao,
 8 |             "prioridade": prioridade,
 9 |             "concluida": False
10 |         }
11 |         tarefas.append(nova_tarefa)
12 |         print(f"\n✅ Tarefa '{descricao}' adicionada com prioridade {prioridade}!")
13 |     else:
14 |         print("\n❌ A descrição e prioridade não podem estar vazias.")
15 |
16 |
17 | def listar_tarefas(tarefas):
18 |     """
19 |     Lista todas as tarefas mostrando a prioridade e o status.
20 |     """
21 |     if not tarefas:
22 |         print("\n📭 Nenhuma tarefa na lista.")
23 |         return
24 |
25 |     print("\n📋 Lista de Tarefas:")
26 |     for i, tarefa in enumerate(tarefas):
27 |         status = "✅" if tarefa["concluida"] else "❌"
28 |         print(f"{i + 1}. {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}) - {status}")
29 |
30 |
31 | def concluir_tarefa(tarefas, indice):
32 |     """
33 |     Marca uma tarefa como concluída com base no índice.
34 |     """
35 |     if 0 <= indice < len(tarefas):
36 |         tarefas[indice]["concluida"] = True
37 |         print(f"\n✔️ Tarefa '{tarefas[indice]['descricao']}' marcada como concluída!")
38 |     else:
39 |         print("\n❌ Índice inválido.")
40 |
41 |
42 | def remover_tarefa(tarefas, indice):
43 |     """
44 |     Remove uma tarefa da lista com base no índice.
45 |     """
46 |     if 0 <= indice < len(tarefas):
47 |         removida = tarefas.pop(indice)
48 |         print(f"\n🗑️ Tarefa '{removida['descricao']}' removida!")
49 |     else:
50 |         print("\n❌ Índice inválido.")
51 |
52 |
53 | def editar_descricao(tarefas, indice, nova_descricao):
54 |     """
55 |     Edita a descrição de uma tarefa existente.
56 |     """
57 |     if 0 <= indice < len(tarefas):
58 |         if nova_descricao:
59 |             tarefas[indice]["descricao"] = nova_descricao
60 |             print(f"\n✏️ Tarefa atualizada para: {nova_descricao}")
61 |         else:
62 |             print("\n❌ A nova descrição não pode ser vazia.")
63 |     else:
64 |         print("\n❌ Índice inválido.")
65 |
66 |
67 | def menu():
68 |     """
69 |     Exibe o menu principal e gerencia as operações.
70 |     """
71 |     tarefas = []
72 |     while True:
73 |         print("\n===== MENU =====")
74 |         print("1. Adicionar Tarefa")
75 |         print("2. Listar Tarefas")
76 |         print("3. Concluir Tarefa")
77 |         print("4. Remover Tarefa")
78 |         print("5. Editar Descrição da Tarefa")
79 |         print("0. Sair")
80 |
81 |         opcao = input("Escolha uma opção: ")
82 |
83 |         if opcao == "1":
84 |             descricao = input("Digite a descrição da tarefa: ")
85 |             prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
86 |             adicionar_tarefa(tarefas, descricao, prioridade)
87 |         elif opcao == "2":
88 |             listar_tarefas(tarefas)
89 |         elif opcao == "3":
90 |             listar_tarefas(tarefas)
91 |             try:
92 |                 indice = int(input("Número da tarefa a concluir: ")) - 1
93 |                 concluir_tarefa(tarefas, indice)
94 |             except ValueError:
95 |                 print("\n❌ Digite um número válido.")
96 |         elif opcao == "4":
97 |             listar_tarefas(tarefas)
98 |             try:
99 |                 indice = int(input("Número da tarefa a remover: ")) - 1
100|                 remover_tarefa(tarefas, indice)
101|             except ValueError:
102|                 print("\n❌ Digite um número válido.")
103|         elif opcao == "5":
104|             listar_tarefas(tarefas)
105|             try:
106|                 indice = int(input("Número da tarefa para editar: ")) - 1
107|                 nova_descricao = input("Digite a nova descrição: ")
108|                 editar_descricao(tarefas, indice, nova_descricao)
109|             except ValueError:
110|                 print("\n❌ Digite um número válido.")
111|         elif opcao == "0":
112|             print("\n👋 Saindo do programa. Até mais!")
113|             break
114|         else:
115|             print("\n❌ Opção inválida.")
116 |
117 |
118 | if __name__ == "__main__":
119 |     menu()
