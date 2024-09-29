

# Projeto tem a tematica de doação de sangue, onde posso criar um sistema com qualquer funcionalidade dentro da tematica.
# Falta decidir qual parte do processo de doação de sangue vai ser implementada.
# Começando com uma apresentação sobre o que é e a importancia de doar sangue
# Ideia vai ser uma triagem inicial para saber se a pessoa pode doar sangue, onde primeiro ela passa por
# uma verificação de peso, temperatura corporal e pressão sanguinia para seguir para doação.
import webbrowser
from Doador import Doador
from funcoes import triagem, pedir_dados_doador
from menu import menu, informacoes_doacao
loop = True  # variavel controladora do loop

##################################################################################################################################################################

while loop:
    escolha = menu() 
    match escolha:
        case 2:
            doador = pedir_dados_doador()  # Pede os dados do doador
            apto = triagem(doador)  # Realiza a triagem e verifica se ta apto
            
            if apto:
                print("Parabéns, você está apto para doar sangue! segue o link para realizar seu agendamento!!")
                # Abre o site de agendamento do Hemoce
                webbrowser.open("https://www.hemoce.ce.gov.br/agende-sua-doacao/", new=2)
            else:
                print("Infelizmente, você não está apto para doar sangue no momento.")

        case 1:
            informacoes_doacao()  #informações sobre doação de sangue
        case 3:
            print("Até logo!! Espero que volte novamente!!")
            loop = False  # Sai do loop e encerra o programa
        case _:
            print("Opção inválida! Por favor, selecione uma opção válida.")