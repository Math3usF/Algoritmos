# QUESTÃO 1 - Sistema de Gestão de Notas de Alunos
# =====================================================

import os

# Variável global para armazenar a lista de alunos
alunos = []


def adicionar_aluno():
    """
    Adiciona um novo aluno à lista.
    Solicita nome e notas (2-5 notas entre 0 e 10).
    Calcula a média e armazena os dados em um dicionário.
    """
    try:
        nome = input("Nome do aluno: ").strip()
        
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return False
        
        notas = []
        numero_notas = 0
        
        while numero_notas < 2 or numero_notas > 5:
            try:
                numero_notas = int(input("Quantas notas deseja inserir? (2-5): "))
                if numero_notas < 2 or numero_notas > 5:
                    print("❌ Deve inserir entre 2 e 5 notas!")
                    continue
            except ValueError:
                print("❌ Digite um número válido!")
                continue
        
        # Coleta as notas com validação
        for i in range(numero_notas):
            while True:
                try:
                    nota = float(input(f"Nota {i+1}: "))
                    if nota < 0 or nota > 10:
                        print("❌ Nota deve estar entre 0 e 10!")
                        continue
                    notas.append(nota)
                    break
                except ValueError:
                    print("❌ Digite um número válido!")
        
        # Calcula a média
        media = sum(notas) / len(notas)
        
        # Cria o dicionário do aluno
        aluno = {
            "nome": nome,
            "notas": notas,
            "media": media
        }
        
        # Adiciona à lista global
        alunos.append(aluno)
        print(f"✓ Aluno '{nome}' adicionado com sucesso! Média: {media:.2f}")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao adicionar aluno: {e}")
        return False


def ordenar_alunos():
    """
    Ordena a lista de alunos por média em ordem decrescente.
    """
    global alunos
    alunos.sort(key=lambda aluno: aluno["media"], reverse=True)


def exibir_alunos():
    """
    Exibe a lista de alunos ordenados por média.
    """
    if not alunos:
        print("\n❌ Nenhum aluno cadastrado!")
        return
    
    print("\n" + "="*50)
    print("ALUNOS ORDENADOS POR MÉDIA:")
    print("="*50)
    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. {aluno['nome']} - Média: {aluno['media']:.2f}")
    print("="*50)


def salvar_em_arquivo(nome_arquivo="alunos.txt"):
    """
    Salva os dados de todos os alunos em um arquivo de texto.
    Cada linha contém: nome,média
    Trata erros de arquivo e permite sobrescrever.
    """
    if not alunos:
        print("\n❌ Nenhum aluno para salvar!")
        return False
    
    try:
        # Verifica se o arquivo já existe
        if os.path.exists(nome_arquivo):
            while True:
                opcao = input(f"\n⚠️  O arquivo '{nome_arquivo}' já existe. Deseja sobrescrever? (s/n): ").lower()
                if opcao == 's':
                    break
                elif opcao == 'n':
                    print("❌ Operação cancelada!")
                    return False
                else:
                    print("⚠️  Digite 's' para sim ou 'n' para não!")
        
        # Salva os dados no arquivo
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for aluno in alunos:
                arquivo.write(f"{aluno['nome']},{aluno['media']:.2f}\n")
        
        print(f"✓ Os dados foram salvos no arquivo '{nome_arquivo}'.")
        return True
        
    except PermissionError:
        print(f"❌ Erro: Sem permissão para salvar no arquivo '{nome_arquivo}'.")
        return False
    except OSError as e:
        print(f"❌ Erro ao salvar no arquivo: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False


def menu_principal():
    """
    Exibe o menu principal e controla o fluxo de execução.
    """
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE GESTÃO DE NOTAS")
        print("="*50)
        print("1. Adicionar aluno")
        print("2. Exibir alunos ordenados")
        print("3. Salvar em arquivo")
        print("4. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == '1':
            adicionar_aluno()
        elif opcao == '2':
            ordenar_alunos()
            exibir_alunos()
        elif opcao == '3':
            ordenar_alunos()
            salvar_em_arquivo()
        elif opcao == '4':
            print("\n✓ Programa encerrado!")
            break
        else:
            print("❌ Opção inválida! Digite um número entre 1 e 4.")


# Execução principal
if __name__ == "__main__":
    print("\n╔══════════════════════════════════════════════════╗")
    print("║    SISTEMA DE GESTÃO DE NOTAS DE ALUNOS        ║")
    print("╚══════════════════════════════════════════════════╝")
    
    menu_principal()
