def inicio():
    print("=====================================================================================================")
    print("Seja bem vindo ao universo dos programadores!, este quizz foi criado para te auxiliar na aprendizagem ")
    print("=====================================================================================================")
def pnome():
    while True:
        nome = input("Digita seu nome, com o primeiro sobrenome")
        if nome != "":
            return nome
        else:
            print("Nome invalido. Tenta novamente..")
def f_pergunta(pergunta, respostac):
    while true:
        resposta = input(pergunta)
        if resposta == "a" or resposta == "b" or resposta == "c":
            if resposta == respostac:
                return True
            else:
                return False
        else:
            print("Digite apenas as letras: A, B ou C. Tente novamente")
def resultado(nome, pontos, total):
    print("=====================================================================================================")
    print(nome + ", Parabéns, mano!!!  Você acertou " + str(pontos) + " de " + str(total) + " perguntas.")
    print("=====================================================================================================")
def p_perguntas():
    perguntas = []
    perguntas.append({
        "pergunta": "1) O que é uma variável? (Em programação)\n"
                      "A) Uma caixa que pode guardar valores\n"
                      "B) algum tipo de erro\n"
                      "C) Uma repetição\n"
                      "Resposta: ",
        "resposta": "A"})
    return perguntas
inicio()
nome = pnome()
perguntas = p_perguntas()
acertos = 0
for item in perguntas:
    certo = f_pergunta(item["Pergunta"], item["Resposta"])
    if certo:
        print("Resposta correta!")
        acertos += 1
    else:
        print("Reposta incorreta. A resposta certa era:", item["resposta"])
resultado(nome, acertos, len(perguntas))
print("========================================================")
print("Chegou ao fim, parabéns novamente. Boa sorte na jornada!")
print("========================================================")
    

