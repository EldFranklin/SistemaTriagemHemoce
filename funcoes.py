
from Doador import Doador


# Função para verificar a pressão sanguínea
def verificar_pressao(pressao_doador):
    if pressao_doador < 9.6:
        print("Desculpe, sua pressão está muito baixa!")
        return False
    elif pressao_doador > 14.9:
        print("Sua pressão está muito alta, não é recomendado doar agora!")
        return True
    else:
        print("Sua pressão está boa, pode prosseguir!")
        return True

 # Função para verificar o peso corporal


def verificar_peso(peso_doador):
    if peso_doador < 50:
        print("Seu peso está abaixo de 50 quilos, é necessário pesar mais para doar!")
        return False
    elif peso_doador > 150:
        print("Você está acima do peso!!")
        return False
    else:
        print("Seu peso está adequado, pode prosseguir!")
        return True


# Função para verificar a temperatura corporal
def verificar_temperatura(temperatura_doador):
    if temperatura_doador > 37.5:
        print("Você está febril, não é recomendado que faça a doação hoje!")
        return False
    else:
        print("Sua temperatura está normal, pode prosseguir!")
        return True


# Função para pegar as informações para a classe doador
def pedir_dados_doador():
    nome = input("Digite o nome do doador: ")
    idade = int(input("Digite a idade do doador: ").replace(",", "."))
    peso = float(input("Digite o peso do doador (em kg): ").replace(",", "."))
    altura = float(
        input("Digite a altura do doador (em cm): ").replace(",", "."))
    temperatura = float(
        input("Digite a temperatura corporal do doador (em °C): ").replace(",", "."))
    pressao_sanguinea = float(input(
        "Digite a pressão sanguínea do doador (valor sistólico): ").replace(",", ".").replace(":", "."))

    # Retorna um objeto do tipo Doador com os dados capturados
    return Doador(nome, idade, peso, altura, temperatura, pressao_sanguinea)


# Fun
def calculaImcDoador(peso_doador, altura_doador):
    imc = peso_doador/altura_doador**2
    if (imc > 40):
        print("Seu IMC(Indíce de Massa Corporal) está alto, consulte um médico antes de prosseguir com a doação!!")
        return False
    else:
        return True


# Função para triagem completa do doador
def triagem(doador):
    print(f"Realizando triagem para o doador {doador.nome}...")

    peso_ok = verificar_peso(doador.peso)
    temperatura_ok = verificar_temperatura(doador.temperatura)
    pressao_ok = verificar_pressao(doador.pressao_sanguinea)
    imc_ok = calculaImcDoador(doador.peso, doador.altura)

    # Retorna True se todas as verificações forem ok
    return peso_ok and temperatura_ok and pressao_ok and imc_ok
