import os


alunos = []


def ler_quantidade_notas(): # função para ler a quantidade de notas, que deve ser entre 2 e 5.
    while True: # Loop para que o usuário digite um valor válido.
        try:
            quantidade_de_notas = int(input("Informe de 2 a 5 notas ? "))
            if 2 <= quantidade_de_notas <= 5: # Verifica se a quantidade de notas está entre 2 e 5.
                return quantidade_de_notas  # Retorna a quantidade de notas válida.
            print("Quantidade inválida. Digite um número entre 2 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_nota(indice): # função para ler uma nota, que deve ser entre 0 e 10, aqui já aceita float.
    while True: #loop para que o usuário digite um valor válido.
        try:
            nota = float(input(f"Digite a {indice}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            print("Nota inválida. A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número válido para a nota.")


def adicionar_aluno(lista_alunos):
    nome = input("Digite o nome do aluno: ").strip().title()
    while nome == "":
        print("O nome não pode ficar vazio.")
        nome = input("Digite o nome do aluno: ").strip().title()

    quantidade_notas = ler_quantidade_notas()
    notas = []

    for i in range(1, quantidade_notas + 1):
        notas.append(ler_nota(i))

    media = sum(notas) / len(notas)
    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media,
    }
    lista_alunos.append(aluno)


def ordenar_alunos(lista_alunos):
    lista_alunos.sort(key=lambda aluno: aluno["media"], reverse=True)


def salvar_em_arquivo(lista_alunos, nome_arquivo="alunos.txt"):
    if os.path.exists(nome_arquivo):
        escolha = input(
            f"O arquivo '{nome_arquivo}' já existe. Deseja sobrescrever? (s/n): "
        ).strip().lower()
        if escolha != "s":
            print("Operação de salvamento cancelada pelo usuário.")
            return

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for aluno in lista_alunos:
                arquivo.write(f"{aluno['nome']},{aluno['media']:.2f}\n")
        print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
    except OSError as erro:
        print(f"Erro ao salvar o arquivo: {erro}")


def exibir_alunos(lista_alunos):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\nAlunos ordenados por média (maior para menor):")
    for aluno in lista_alunos:
        print(f"Nome: {aluno['nome']} | Média: {aluno['media']:.2f}")


def calcular_media_turma(lista_alunos):
    if not lista_alunos:
        return 0.0
    return sum(aluno["media"] for aluno in lista_alunos) / len(lista_alunos)


def main():
    print("Sistema de Gerenciamento de Notas")

    while True:
        adicionar_aluno(alunos)
        while True:
            continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
            if continuar in ("s", "n"):
                break
            print("Entrada inválida. Digite apenas 's' para sim ou 'n' para não.")

        if continuar == "n":
            break

    ordenar_alunos(alunos)
    exibir_alunos(alunos)

    if alunos:
        media_turma = calcular_media_turma(alunos)
        print(f"\nMédia da turma: {media_turma:.2f}")
        salvar_em_arquivo(alunos)


if __name__ == "__main__":
    main()
