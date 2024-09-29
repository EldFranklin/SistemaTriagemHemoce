
def menu():
    print("\n=== Menu Principal ===")
    print("1. Informações sobre Doação de Sangue")
    print("2. Realizar Triagem")
    print("3. Sair")
    print("======================")
    op = int(input())
    return op


def informacoes_doacao():
    print("\n=== Informações sobre Doação de Sangue ===")
    print("A doação de sangue é um ato voluntário que pode salvar vidas.")
    print("Critérios básicos para doar sangue:")
    print("- Ter entre 16 e 69 anos (com autorização para menores de idade)")
    print("- Pesar acima de 50 kg")
    print("- Estar em boas condições de saúde")
    print("- Não estar com febre, gripe ou resfriado")
    print("============================================\n")
