



# Projeto tem a tematica de doação de sangue, onde posso criar um sistema com qualquer funcionalidade dentro da tematica.

# Começando com uma apresentação sobre o que é e a importancia de doar sangue
# Ideia vai ser uma triagem inicial para saber se a pessoa pode doar sangue, onde primeiro ela passa por
# uma verificação de peso, temperatura corporal e pressão sanguinia para seguir para doação.
import webbrowser
from time import sleep
from Doador import Doador
from funcoes import triagem, pedir_dados_doador
from menu import menu, informacoes_doacao, como_doar, medula
loop = True  # variavel controladora do loop

##################################################################################################################################################################

while loop:
    escolha = menu()
    match escolha:
        case 1:
            informacoes_doacao()  # informações sobre doação de sangue
        case 2:
            como_doar() # informações sobre como doar
        case 4:
            medula() # informações sobbre a doação de medula
        case 3:
            doador = pedir_dados_doador()  # Pede os dados do doador
            apto = triagem(doador)  # Realiza a triagem e verifica se ta apto
            if apto:
                print(
                    "Parabéns, você está apto para doar sangue! No menu aperta 5 para realizar seu agendamento!!")

            else:
                
                print("Infelizmente, você não está apto para doar sangue no momento.")
        case 5:
            print('''Para agendar sua doação, vamos te redirecionar para a pagina do hemoce, nela você pode veririficar 
                  O centro de coleta mais próximo de você! Até logo!''')
            for i in range(5, 0, -1):
                print(f"Redirecionando em {i}")
                sleep(1)

            # redicionando o doador para a pagina de reserva do hemoce
            webbrowser.open("https://hemoce.reservio.com/ ", new=2)
        case 6:
            print("Até logo!! Espero que volte novamente!!")
            loop = False  # Sai do loop e encerra o programa
        case _:
            print("Opção inválida! Por favor, selecione uma opção válida.")
