
print ('=='*5 + ' QuizTech ' + '=='*5 + '\n')

#Listas de perguntas e respostas:
perguntas = [
    {
        "pergunta": "Se A = {1,2,3} e B = {2,3,4}, qual é A ∩ B?",
        "opcoes": ["1", "2,3", "3,4", "1,2,3,4"],
        "correta": 2
    },
    {
        "pergunta": "Qual é o próximo número da sequência: 2, 4, 8, 16, __?",
        "opcoes": ["20", "24", "32", "36"],
        "correta": 3
    },
    {
        "pergunta": "Qual é o valor decimal do número binário 1010?",
        "opcoes": ["5", "10", "12", "15"],
        "correta": 2
    },
    {
        "pergunta": "Quantos bits há em um byte?",
        "opcoes": ["4", "8", "16", "32"],
        "correta": 2
    },
    {
        "pergunta": "Qual é o resultado de 7! (7 fatorial)?",
        "opcoes": ["5040", "720", "120", "40320"],
        "correta": 1
    },
    {
        "pergunta": "Em lógica de programação, qual estrutura de repetição executa pelo menos uma vez?",
        "opcoes": ["for", "while", "do-while", "foreach"],
        "correta": 3
    },
    {
        "pergunta": "Se um número é divisível por 2 e por 3, ele também é divisível por?",
        "opcoes": ["4", "5", "6", "7"],
        "correta": 3
    },
    {
        "pergunta": "Qual é o operador lógico que representa 'E' (AND) na programação?",
        "opcoes": ["||", "&&", "!", "^^"],
        "correta": 2
    },
    {
        "pergunta": "O que significa SQL?",
        "opcoes": [
            "Sistema de Query Lógico",
            "Structured Query Language",
            "Software Query Language",
            "Scripted Query Language"
        ],
        "correta": 2
    },
    {
        "pergunta": "Em um banco de dados, qual comando é usado para inserir dados em uma tabela?",
        "opcoes": ["INSERT", "UPDATE", "SELECT", "DELETE"],
        "correta": 1
    }
]

#Variáveies de pontuação:
pontuacao = 0

#Loop para as perguntas:
for i, questao in enumerate(perguntas):
    print ('\n' + '=='*5 + f' Pergunta {i + 1}: ' + '=='*5)
    print(f"\n{questao['pergunta']}")

    #Mostrar opções:
    for j, opcao in enumerate(questao["opcoes"], 1):
        print(f"{j}) {opcao}")
    
    #Obter as resposta do jogador:
    while True:
        try:
            resposta = int(input("Escolha a opção correta (1-4): "))
            if 1 <= resposta <= 4:
                break
            else:
                print("Opção inválida. Escolha um número entre 1 e 4.")
        except ValueError:
            print("Por favor, insira um número válido.")

    #Verificar as respostas:
    if resposta == questao["correta"]:
        print("✅ Resposta correta!")
        pontuacao += 1
    else:
        print(f"❌ Resposta errada! A resposta correta era: {questao['opcoes'][questao['correta'] - 1]}")

#Exibir as pontuação final:
print ('=='*5 + ' FIM DO JOGO! ' + '=='*5 )
print(f"\n Você acertou {pontuacao} de {len(perguntas)} perguntas.")
print ('=='*10 )