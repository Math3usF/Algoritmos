import os


ARQUIVO_BIBLIOTECA = "biblioteca.txt"


def ler_inteiro_positivo(mensagem): #mensagem é a lista de mensagens que serão exibidas para o usuário.
	#Lê e valida um inteiro positivo digitado pelo usuário.
	while True:
		entrada = input(mensagem).strip()
		try:
			valor = int(entrada)
			if valor <= 0:
				raise ValueError
			return valor
		except ValueError:
			print("Valor inválido. Digite um número inteiro positivo.")


def adicionar_livro(livros): #livros é a lista onde os livros serão armazenados.
	titulo = input("Título do livro: ").strip().title()
	autor = input("Autor: ").strip().title()
	ano = ler_inteiro_positivo("Ano de publicação: ")
	paginas = ler_inteiro_positivo("Número de páginas: ")

	livro = { "titulo": titulo,	"autor": autor,	"ano": ano,	"paginas": paginas,	} #criçaõ do dicionário livro, que precisa ter as chaves dentro do colchete.
	livros.append(livro)
	print("Livro adicionado com sucesso!")


def listar_livros(livros):
	if not livros: #se não tiver livros na lista exibe a mensagem 
		print("Nenhum livro cadastrado.")
		return

	print("\nLivros cadastrados:")
	for i, livro in enumerate(livros, start=1): #enumerate retorna o indice e valor do item na lista, start=1 faz com que o indice comece a contar a partir de 1.
		print(
			f"{i}. Título: {livro['titulo']} | Autor: {livro['autor']} | " #formata a saida e usa as chaves para acessar as
			f"Ano: {livro['ano']} | Páginas: {livro['paginas']}"
		)


def ordenar_livros(livros):
	if not livros:
		print("Não há livros para ordenar.")
		return

	print("Ordenar por:")
	print("1. Ano de publicação")
	print("2. Número de páginas")
	criterio_opcao = input("> ").strip()

	if opcao_1 == "1":
		criterio = "ano"
	elif opcao_2 == "2":
		criterio = "paginas"
	else:
		print("Opção de critério inválida.")
		return

	print("Ordem:")
	print("1. Crescente")
	print("2. Decrescente")
	ordem = input("> ").strip()

	if ordem == "1":
		reverso = False
	elif ordem == "2":
		reverso = True
	else:
		print("Opção de ordem inválida.")
		return

	livros.sort(key=lambda livro: livro[criterio], reverse=reverso) #sort ordena a lista de livros com base no critério escolhido pela função lambda para acessar o valor. O parâmetro reverse é usado para determinar se a ordenação deve ser crescente ou decrescente.
	print("Livros ordenados com sucesso!")


def salvar_livros(livros, arquivo=ARQUIVO_BIBLIOTECA):
	try:
		with open(arquivo, "w", encoding="utf-8") as f:
			for livro in livros:
				linha = (
					f"{livro['titulo']},{livro['autor']},"
					f"{livro['ano']},{livro['paginas']}"
				)
				f.write(linha)
		print(f"Os dados foram salvos no arquivo '{arquivo}'.")
	except PermissionError:
		print("Erro de permissão ao salvar o arquivo.")
	except OSError as erro:
		print(f"Erro de entrada/saída ao salvar dados: {erro}")


def carregar_livros(livros, arquivo=ARQUIVO_BIBLIOTECA):
	if not os.path.exists(arquivo):
		print(f"Arquivo '{arquivo}' não encontrado.")
		return

	try:
		novos_livros = [] #lista para armazenar os livros do arquivo.
		with open(arquivo, "r", encoding="utf-8") as f: #abre o arquivo para leitura,
			for numero_linha, linha in enumerate(f, start=1):
				linha = linha.strip()
				if not linha:
					continue

				partes = linha.split(",") #divide a linha usando , com separador.
				if len(partes) != 4: #vrf se tem 4 partes.
					print(
						f"Linha {numero_linha} ignorada: formato inválido no arquivo."
					)
					continue

				titulo, autor, ano_str, paginas_str = partes
				try:
					ano = int(ano_str)
					paginas = int(paginas_str)
					if ano <= 0 or paginas <= 0:
						raise ValueError
				except ValueError:
					print(
						f"Linha {numero_linha} ignorada: ano/páginas inválidos."
					)
					continue

				novos_livros.append(
					{
						"titulo": titulo,
						"autor": autor,
						"ano": ano,
						"paginas": paginas,
					}
				)

		livros.clear()
		livros.extend(novos_livros)
		print("Dados carregados com sucesso!")
	except PermissionError: #PermissionError o programa não tem permissão para acessar o arquivo
		print("Erro de permissão ao ler o arquivo.")
	except OSError as erro: #OSError erros relacionados ao sistema operacional, incluindo erros de arquivo.
		print(f"Erro de entrada/saída ao carregar dados: {erro}")


def menu():
	livros = []

	print("Bem-vindo à Biblioteca Digital!")

	while True:
		print("Escolha uma opção:")
		print("1. Adicionar livro")
		print("2. Listar livros")
		print("3. Ordenar livros")
		print("4. Salvar dados em arquivo")
		print("5. Carregar dados do arquivo")
		print("6. Sair")

		opcao = input("> ").strip()

		if opcao == "1":
			adicionar_livro(livros)
		elif opcao == "2":
			listar_livros(livros)
		elif opcao == "3":
			ordenar_livros(livros)
		elif opcao == "4":
			salvar_livros(livros)
		elif opcao == "5":
			carregar_livros(livros)
		elif opcao == "6":
			while True:
				salvar = input("Deseja salvar os dados antes de sair? (S/N): ").strip().upper()
				if salvar == "S":
					salvar_livros(livros)
					print("Encerrando o programa.")
					break
				if salvar == "N":
					print("Encerrando o programa.")
					break
				print("Entrada inválida. Digite apenas S ou N.")
			break
		else:
			print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
	menu()
