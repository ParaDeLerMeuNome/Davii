times = []; continuar = "s"
while continuar == "s":
    time = input("Nome do time: ")
    jogador = input("Jogador atual: ")
    fundacao = input("Ano de fundação: ")
    times.append({"time": time, "jogador": jogador, "fundacao": fundacao})
    continuar = input("Deseja adicionar outro? (s/n): ")
for t in times: print(t)
