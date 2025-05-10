def gerar_projeto(tipo_site, funcionalidades):
    tecnologias = {
        "1": ["HTML", "CSS", "JavaScript"],
        "2": ["HTML", "CSS", "JavaScript", "ASP.NET", "SQL Server"],
        "3": ["HTML", "CSS", "JavaScript", "Blog CMS (ex: WordPress)"]
    }

    tech_usadas = tecnologias.get(tipo_site, [])
    return tech_usadas

print("Assistente de Criação de Sites - Davi Developer")
while True:
    nome_cliente = input("\nNome do cliente: ")

    print("\nTipo de site desejado:")
    print("1 - Site institucional")
    print("2 - Loja virtual")
    print("3 - Blog")
    tipo = input("Digite o número correspondente: ")

    funcionalidades = []
    while True:
        print("\nFuncionalidades desejadas:")
        print("1 - Formulário de contato")
        print("2 - Galeria de fotos")
        print("3 - Carrinho de compras")
        print("4 - Integração com redes sociais")
        print("0 - Finalizar")
        op = input("Escolha uma opção: ")

        if op == "0":
            break
        elif op in ["1", "2", "3", "4"]:
            funcionalidades.append(op)
        else:
            print("Opção inválida. Tente novamente.")

    tecnologias = gerar_projeto(tipo, funcionalidades)

    print("\nResumo do Projeto:")
    print(f"Cliente: {nome_cliente}")
    print(f"Tipo de site: {tipo}")
    print(f"Funcionalidades selecionadas: {len(funcionalidades)}")
    print("Tecnologias recomendadas:")
    for tech in tecnologias:
        print(f"- {tech}")

    repetir = input("\nDeseja iniciar um novo projeto? (s/n): ")
    if repetir.lower() != 's':
        print("Encerrando o assistente. Bons projetos, Davi!")
        break
