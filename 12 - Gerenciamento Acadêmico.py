''' SISTEMA DE GESTÃO ACADÊMICA que permite realizar 
    - cadastro de alunos
    - cálculo de médias e situação
    - frequência escolar
    - ranking de notas
    - histórico e CRA
'''

# LISTAS GLOBAIS

alunos = []
historico = []


# GERENCIAMENTO DE ALUNOS

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    matricula = input("Digite a matrícula do aluno: ").strip()
    curso = input("Digite o curso do aluno: ").strip()
    
    return {
        "nome": nome, 
        "matricula": matricula, 
        "curso": curso
    }

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    print("\n--- Lista de Alunos ---")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}")

def buscar_por_matricula(matricula):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None


# MÉDIAS 

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    return "Reprovado"

def modulo_calcular_media():
    nome = input("Digite o nome do aluno: ")
    notas = []
    
    for i in range(1, 4):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)
        
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    
    print("\n--- Resultado ---")
    print(f"Nome do aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


# FREQUÊNCIA ESCOLAR

def calcular_percentual_presenca(frequencias):
    # Tratando maiúsculas e minúsculas com segurança
    presencas = frequencias.count("p") + frequencias.count("P")
    if len(frequencias) == 0:
        return 0
    return (presencas / len(frequencias)) * 100

def modulo_frequencia():
    frequencias = []
    quantidade_aulas = int(input("Digite a quantidade de aulas: "))
    
    for i in range(1, quantidade_aulas + 1):
        frequencia = input(f"Digite a presença da aula {i} (P para presente ou F para falta): ").lower()
        while frequencia not in ["p", "f"]:
            frequencia = input("Valor inválido. Digite apenas p ou f: ").lower()
        frequencias.append(frequencia)
        
    percentual = calcular_percentual_presenca(frequencias)
    
    print("\n=== Frequência Escolar ===")
    print(f"Frequências registradas: {frequencias}")
    print(f"Percentual de presença: {percentual:.2f}%")


# RANKING DE NOTAS

def mostrar_ranking(dicionario_alunos):
    ranking = sorted(dicionario_alunos.items(), key=lambda item: item[1], reverse=True)
    
    print("\n=== Ranking Final ===")
    for posicao, (nome, media) in enumerate(ranking, start=1):
        print(f"{posicao}º lugar - {nome}: {media:.2f}")

def modulo_ranking():
    dicionario_alunos = {}
    
    # Validação para garantir que o usuário digite um número inteiro
    while True:
        try:
            quantidade = int(input("Digite a quantidade de alunos para o ranking: "))
            if quantidade <= 0:
                print("Por favor, digite um número maior que zero.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
    
    for i in range(1, quantidade + 1):
        # 1. Pede o nome primeiro
        nome = input(f"Digite o nome do aluno {i}: ").strip()
        
        # 2. Pede a média usando o nome do aluno e faz a validação
        while True:
            try:
                media = float(input(f"Digite a média de {nome}: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número para a média (ex: 8.5).")
                
        dicionario_alunos[nome] = media
        
    mostrar_ranking(dicionario_alunos)


# HISTÓRICO E CRA

def adicionar_disciplina():
    disciplina = input("Digite o nome da disciplina: ").strip()
    
    for item in historico:
        if item["disciplina"] == disciplina:
            print("Essa disciplina já foi adicionada.")
            return
            
    historico.append({"disciplina": disciplina, "nota": None})
    print("Disciplina adicionada com sucesso!")

def adicionar_nota():
    disciplina = input("Digite o nome da disciplina: ").strip()
    
    for item in historico:
        if item["disciplina"] == disciplina:
            item["nota"] = float(input(f"Digite a nota da disciplina {disciplina}: "))
            print("Nota adicionada com sucesso!")
            return
            
    print("Disciplina não encontrada.")

def consultar_historico():
    if not historico:
        print("Nenhuma disciplina cadastrada.")
        return
        
    print("\n=== Histórico Acadêmico ===")
    for item in historico:
        nota = item["nota"]
        if nota is None:
            print(f"Disciplina: {item['disciplina']} | Nota: Sem nota cadastrada")
        else:
            print(f"Disciplina: {item['disciplina']} | Nota: {nota:.2f}")

def calcular_cra():
    notas_validas = []
    
    for item in historico:
        if item["nota"] is not None:
            notas_validas.append(item["nota"])
            
    if not notas_validas:
        print("Não há notas para calcular o CRA.")
        return
        
    cra = sum(notas_validas) / len(notas_validas)
    print(f"\nCRA Calculado: {cra:.2f}")


# MENU PRINCIPAL INTEGRADO

def main():
    while True:
        print("\n" + "="*40)
        print("        SISTEMA DE GESTÃO ACADÊMICA")
        print("="*40)
        print("  1 - Cadastrar aluno")
        print("  2 - Listar alunos")
        print("  3 - Buscar aluno por matrícula")
        print("  4 - Calcular Média e Situação")
        print("  5 - Frequência Escolar")
        print("  6 - Ranking de Notas")
        print("  7 - Adicionar disciplina ao Histórico")
        print("  8 - Adicionar nota ao Histórico")
        print("  9 - Consultar Histórico")
        print(" 10 - Calcular CRA")
        print("  0 - Sair")
        print("="*40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            aluno_novo = cadastrar_aluno()
            alunos.append(aluno_novo)
            print("Aluno cadastrado com sucesso!")
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            matricula = input("Digite a matrícula para busca: ").strip()
            aluno = buscar_por_matricula(matricula)
            if aluno:
                print(f"Aluno Encontrado: {aluno}")
            else:
                print("Aluno não encontrado.")
        elif opcao == "4":
            modulo_calcular_media()
        elif opcao == "5":
            modulo_frequencia()
        elif opcao == "6":
            modulo_ranking()
        elif opcao == "7":
            adicionar_disciplina()
        elif opcao == "8":
            adicionar_nota()
        elif opcao == "9":
            consultar_historico()
        elif opcao == "10":
            calcular_cra()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


# Inicializa o programa
if __name__ == "__main__":
    main()
