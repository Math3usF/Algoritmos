import os

produtos = [] #Lista global para armazenar os produtos
def ler_float_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))  
            if valor <= 0:
                print("Digite um valor positivo!")
                continue    #continua o loop para pedir a entrada novamente
            return valor    #retorna o valor se for valido, ou seja, um numero positivo
        except ValueError:
            print("Digite um numero valido!")

def ler_int_valido(mensagem):   #fun~çao para ler inteiro positivo.
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Digite um inteiro nao positivo!")
                continue
            return valor
        except ValueError:
            print("Digite um numero inteiro valido!")

def adicionar_produto():
    nome = input("Nome do produto: ").strip().title()
    categoria = input("Categoria: ").strip().title()

    if not nome or not categoria:   #verifica se nome ou categoria estão vazios.
        print("Nome e categoria nao podem estar vazios!")
        return False

    preco = ler_float_positivo("Preco (R$): ")    
    quantidade = ler_int_valido("Quantidade:")  
    produto = { "nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade,}
    produtos.append(produto)
    print("Produto adicionado com sucesso!")
    return True

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado!")
        return

    print("\nProdutos cadastrados:")
    for i, produto in enumerate(produtos, start=1): #enumerate retorna o indice startando de 1.
            print(
                f"{i}. {produto['nome']} | Categoria: {produto['categoria']} | "
                f"Preco: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']}"
            )

def atualizar_quantidade():
    if not produtos:
        print("Nenhum produto cadastrado para atualizar!")
        return False #retorna falso para indicar que a operação não foi realizada devido à falta de produtos.
    listar_produtos()
    while True:
        try:
            indice = int(input("Escolha o numero do produto para atualizar: "))
            if indice < 1 or indice > len(produtos):
                print("Numero invalido!")
                continue
            break
        except ValueError:
            print("Digite um numero inteiro valido!")
    produto = produtos[indice - 1]
    operacao = input("Deseja aumentar ou reduzir? (A/R): ").strip().upper()
    if operacao not in ("A", "R"):  #verifica se a operação é válida, A para aumentar ou R para reduzir.
        print("Opcao invalida! Use A para aumentar ou R para reduzir.")
        return False
    valor = ler_int_valido("Informe a quantidade para alterar: ")
    if operacao == "A":
        produto["quantidade"] += valor
    else:
        if valor > produto["quantidade"]:
            print("Nao e possivel reduzir mais do que a quantidade atual.")
            return False
        produto["quantidade"] -= valor

    print("Quantidade atualizada com sucesso!")
    return True

def ordenar_produtos():
    if not produtos:
        print("Nenhum produto para ordenar!")
        return False
    print("Ordenar por:")
    print("1. Preco")
    print("2. Quantidade")
    criterio = input("Escolha (1-2): ")
    if criterio == "1":
        chave = "preco"
    elif criterio == "2":
        chave = "quantidade"
    else:
        print("Opcao invalida!")
        return False
    ordem = input("Ordem crescente ou decrescente? (C/D): ").upper()
    if ordem not in ("C", "D"):
        print("Opcao invalida! Use C para crescente ou D para decrescente.")
        return False
    reverso = ordem == "D"  #variavel booleana para indicar se a ordenação deve ser feita em ordem decrescente.
    produtos.sort(key=lambda produto: produto[chave], reverse=reverso) #sort ordena a lista de produtos com base na chave escolhida, lambda para acessar o valor da chave em cada produto. Reverse é usado para determinar se a ordenação deve ser crescente ou decrescente.
    print("Produtos ordenados com sucesso!")
    return True


def salvar_estoque(nome_arquivo="estoque.txt"):
    if not produtos:
        print("Nenhum produto para salvar!")
        return False

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("NOME,CATEGORIA,PRECO,QUANTIDADE\n")
            for produto in produtos:
                linha = (
                    f"{produto['nome']},{produto['categoria']},"
                    f"{produto['preco']:.2f},{produto['quantidade']}\n"
                )
                arquivo.write(linha)
        print(f"Os dados foram salvos no arquivo '{nome_arquivo}'")
        return True
    except PermissionError:
        print(f"Erro: sem permissao para escrever em '{nome_arquivo}'.")
        return False
    except OSError as erro:
        print(f"Erro de leitura ou gravacao: {erro}")
        return False


def carregar_estoque(nome_arquivo="estoque.txt"):
    if not os.path.exists(nome_arquivo):        #se o arquivo não existe exibe msg de error e retorna falso para indicar que a operação de carregamento não foi realizada.
        print(f"Arquivo '{nome_arquivo}' nao encontrado.")
        return False
    try:
        produtos_carregados = []
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):  #enumerate para obter o número da linha, começando em 1 
                linha = linha.strip()
                if not linha:
                    continue
                partes = [parte.strip() for parte in linha.split(",")] #divide a linha em partes usando a vírgula como separador e remove espaços em branco extras.
                if len(partes) != 4:
                    print(f"Linha {numero_linha} ignorada: formato invalido.")
                    continue

                if numero_linha == 1 and [p.upper() for p in partes] == ["NOME", "CATEGORIA", "PRECO", "QUANTIDADE"]:
                    continue

                nome, categoria, preco_texto, quantidade_texto = partes

                try:
                    preco = float(preco_texto)
                    quantidade = int(quantidade_texto)
                    if preco <= 0 or quantidade < 0:
                        raise ValueError
                except ValueError:
                    print(f"Linha {numero_linha} ignorada: preco/quantidade invalidos.")
                    continue

                produtos_carregados.append(
                    {
                        "nome": nome,
                        "categoria": categoria,
                        "preco": preco,
                        "quantidade": quantidade,
                    }
                )
        produtos.clear()
        produtos.extend(produtos_carregados)
        print("Estoque carregado com sucesso!")
        return True
    except PermissionError: 
        print(f"Erro: sem permissao para ler '{nome_arquivo}'.")
        return False
    except OSError as erro:
        print(f"Erro de leitura ou gravacao: {erro}")
        return False

def menu_principal():
    print("Bem-vindo ao Sistema de Gestao de Estoque!")

    while True:
        print("\nEscolha uma opcao:")
        print("1. Adicionar produto")
        print("2. Atualizar quantidade")
        print("3. Listar produtos")
        print("4. Ordenar produtos")
        print("5. Salvar dados em arquivo")
        print("6. Carregar dados do arquivo")
        print("7. Sair")

        opcao = input("> ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_quantidade()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            ordenar_produtos()
        elif opcao == "5":
            salvar_estoque()
        elif opcao == "6":
            carregar_estoque()
        elif opcao == "7":
            salvar = input("Deseja salvar o estoque antes de sair? (S/N): ").strip().upper()
            if salvar == "S":
                salvar_estoque()
            print("Programa encerrado!")
            break
        else:
            print("Opcao invalida! Escolha entre 1 e 7.")


if __name__ == "__main__":
    menu_principal()
