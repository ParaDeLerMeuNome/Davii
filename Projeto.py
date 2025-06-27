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
    while True:
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
        "resposta": "a"})
    perguntas.append({
        "pergunta": "2) Qual comando usamos para repetir algo até que a condição pare?\n"
                      "A) if\n"
                      "B) while\n"
                      "C) print\n"
                      "Resposta: ",
        "resposta": "b"})
    perguntas.append({
        "pergunta": "3) Qual das opções representa uma função em Python?\n"
                      "A) def minha_funcao():\n"
                      "B) minha_funcao = 10\n"
                      "C) return def\n"
                      "Resposta: ",
        "resposta": "a"})
    perguntas.append({
        "pergunta": "4) O que faz o comando 'input()'?\n"
                      "A) Repete uma frase\n"
                      "B) Pede um valor ao usuário\n"
                      "C) Cria uma variável\n"
                      "Resposta: ",
        "resposta": "b"})
    perguntas.append({
        "pergunta": "5) O que significa 'True' em Python?\n"
                      "A) Um erro\n"
                      "B) Uma condição falsa\n"
                      "C) Um valor booleano verdadeiro\n"
                      "Resposta: ",
        "resposta": "c"})
    perguntas.append({
        "pergunta": "6) Qual estrutura armazena várias perguntas no quiz?\n"
                      "A) String\n"
                      "B) Lista\n"
                      "C) Número\n"
                      "Resposta: ",
        "resposta": "b"})
    perguntas.append({
        "pergunta": "7) Qual comando é utilizado para adicionar perguntas em uma lista?\n"
                      "A) perguntas.add()\n"
                      "B) perguntas.insert()\n"
                      "C) perguntas.append()\n"
                      "Resposta: ",
        "resposta": "c"})
    perguntas.append({
        "pergunta": "8) O que acontece se o usuário digitar nada no nome?\n"
                      "A) O programa aceita vazio\n"
                      "B) O programa pede novamente até digitar algo\n"
                      "C) O programa trava\n"
                      "Resposta: ",
        "resposta": "b"})
    perguntas.append({
        "pergunta": "9) O que é uma estrutura condicional em Python?\n"
                      "A) Um número fixo\n"
                      "B) Um tipo de variável\n"
                      "C) Um bloco que executa algo se uma condição for verdadeira\n"
                      "Resposta: ",
        "resposta": "c"})
    perguntas.append({
        "pergunta": "10) Qual dessas palavras-chave usamos para criar uma função?\n"
                      "A) define\n"
                      "B) def\n"
                      "C) func\n"
                      "D) funcao\n"
                      "Resposta: ",
        "resposta": "b"})
    perguntas.append({
        "pergunta": "11) Como declaramos uma lista vazia?\n"
                      "A) lista = {}\n"
                      "B) lista = ()\n"
                      "C) lista = []\n"
                      "Resposta: ",
        "resposta": "c"})
    perguntas.append({
        "pergunta": "12) Qual é o tipo de dado retornado pela função input()?\n"
                      "A) número\n"
                      "B) string\n"
                      "C) booleano\n"
                      "Resposta: ",
        "resposta": "b"})
    perguntas.append({
        "pergunta": "13) O que significa o sinal == em uma comparação?\n"
                      "A) Atribuição de valor\n"
                      "B) Igualdade (comparação entre dois valores)\n"
                      "C) Adição entre números\n"
                      "Resposta: ",
        "resposta": "b"})
    return perguntas
inicio()
nome = pnome()
perguntas = p_perguntas()
acertos = 0
for item in perguntas:
    certo = f_pergunta(item["pergunta"], item["resposta"])
    if certo:
        print("Resposta correta!")
        acertos += 1
    else:
        print("Reposta incorreta. A resposta certa era:", item["resposta"])
resultado(nome, acertos, len(perguntas))
print("========================================================")
print("Chegou ao fim, parabéns novamente. Boa sorte na jornada!")
print("========================================================")



