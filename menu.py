
def menu():
    print("\n=== Menu Principal ===")
    print("1. A Importância da Doação de Sangue")
    print("2. Como Doar")
    print("3. Realize uma Triagem")
    print("4. A Importância da Doação de Medula Óssea")
    print("5. Agendamento")
    print("6. Sair")
    print("======================")
    op = int(input())
    return op


def informacoes_doacao():
    print("\n=== Informações sobre Doação de Sangue ===")
    print("Qual a importância da doação de sangue?")
    print('''Doar sangue é um ato de amor, voluntário e altruísta. O sangue é essencial para atendimentos de urgências, grandes cirurgias
e tratamentos de pessoas com doenças como a falciforme e talassemias. Além disso, é vital para pacientes oncológicos que frequentemente
necessitam de transfusão. 

É muito importante manter os estoques de sangue sempre abastecidos.
Seja um doador regular: uma doação pode salvar até quatro vidas!''')
    print("============================================\n")
