alfabeto = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u', 'v','w','x','y','z']
def criptografa(pl, chave):
    cripto = []
    for letra in pl:
        i = alfabeto.index(letra)
        i = (i + chave) % 26
        cripto.append(alfabeto[i])
    return cripto
def descriptografa(pl, chave):
    descripto = []
    for letra in pl:
        i = alfabeto.index(letra)
        i = (i - chave) % 26
        descripto.append(alfabeto[i])
    return descripto
opcao = input("Digite (c) para criptografar ou (d) para descriptografar: ")
palavra = input("Digite uma palavra (somente letras minúsculas): ")
chave = int(input("Digite a chave (ex: 3): "))
if opcao == 'c':
    lista = criptografa(palavra, chave)
    print("Resultado:", lista)
elif opcao == 'd':
    lista = descriptografa(palavra, chave)
    print("Resultado:", lista)
else:
    print("Opção inválida.")
