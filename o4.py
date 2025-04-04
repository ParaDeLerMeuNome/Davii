nome = input("Digite seu nome ")
idade = int(input("Quantos anos você tem? "))
mes = int(input("Qual o número do mês que você nasceu? ex: 1,2 10: "))
if ((idade>18)) and (mes>6):
    print (f"você é maior de idade e nasceu após junho")
elif ((idade<18)) and (mes>6):
    print (f"você é menor de idade e nasceu após junho")
elif ((idade>18)) and (mes<6):
    print (f"você é maior de idade e nasceu antes de junho")
elif ((idade<18)) and (mes<6):
    print(f"você é menor de idade e nasceu depois de junho")