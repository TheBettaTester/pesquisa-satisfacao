# Códigos de cores ANSI
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"

# Inicializando contadores
excelente = 0
bom = 0
ruim = 0

quantidade = 50  # troque para 10 para testes

for i in range(quantidade):
    print(f"\n{AZUL}Entrevistado {i+1}{RESET}")

    # Validação do nome
    while True:
        nome = input("Digite o nome: ")
        if nome.replace(" ", "").isalpha():
            break
        else:
            print(f"{VERMELHO}Nome inválido! Digite apenas letras.{RESET}")

    # Validação da idade
    while True:
        idade_input = input("Digite a idade: ")

        if not idade_input.lstrip("-").isdigit():
            print(f"{VERMELHO}Idade inválida! Digite apenas números.{RESET}")
            continue

        idade = int(idade_input)

        if idade <= 0:
            print(f"{VERMELHO}Erro: indivíduo ainda não nasceu.{RESET}")
        elif idade > 120:
            print(f"{VERMELHO}Idade inválida! Alguém chame o Guinness, temos um imortal aqui.{RESET}")
        else:
            break

    # Faixa etária
    if idade <= 12:
        faixa = "Criança"
    elif idade <= 17:
        faixa = "Adolescente"
    elif idade <= 59:
        faixa = "Adulto"
    else:
        faixa = "Idoso"

    print(f"{AMARELO}Faixa etária: {faixa}{RESET}")

    # Opinião
    print("Opinião sobre o atendimento:")
    print(f"{VERDE}1 - EXCELENTE{RESET}")
    print(f"{AMARELO}2 - BOM{RESET}")
    print(f"{VERMELHO}3 - RUIM{RESET}")

    # Validação da opinião
    while True:
        opiniao_input = input("Digite sua opinião (1, 2 ou 3): ")
        if opiniao_input in ["1", "2", "3"]:
            opiniao = int(opiniao_input)
            break
        else:
            print(f"{VERMELHO}Opção inválida! Digite 1, 2 ou 3.{RESET}")

    # Contagem
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1

# Resultado final
print(f"\n{VERDE}===== RESULTADO DA PESQUISA ====={RESET}")
print(f"{VERDE}EXCELENTE: {excelente}{RESET}")
print(f"{AMARELO}BOM: {bom}{RESET}")
print(f"{VERMELHO}RUIM: {ruim}{RESET}")

# Esperar usuário sair
while True:
    comando = input("\nDigite 'sair' para encerrar o programa: ").lower()
    if comando == "sair":
        break