# ==========================
# SISTEMA ESCOLAR
# ==========================
from time import sleep

# ==========================
# LISTA VAZIA
# ==========================

alunos = []
professores = []
proximo_numero = 1

# ==========================
# DISCIPLINAS DO CURSO
# ==========================

nomes_disciplinas = [
    "Algoritmo e Programação",
    "Banco de Dados",
    "Engenharia de Software"
]

# ==========================
# CORES TERMINAL
# ==========================

verde = "\033[1;32m"
vermelho = "\033[1;31m"
azul = "\033[1;36m"
reset = "\033[0m"
neutro = "\033[2;37m"
laranja = "\033[1;33m"
negrito = "\033[1m"
sublinhado = "\033[4m"

# ==========================
# TEMPO DE IMPRESSÃO
# ==========================

def imprimir(texto, tempo=1):
    print(texto)
    sleep(tempo)

# ==========================
# VALIDAÇÕES E PREVENÇÃO
# ==========================

def validar_texto(mensagem="\nDigite o nome completo do aluno: "):
    nome = input(mensagem)

    while not nome.replace(" ", "").isalpha():
        print(f"{vermelho}Nome inválido! Digite apenas letras.{reset}")
        nome = input(mensagem)

    return nome


def validar_idade(mensagem="Digite a idade: "):

    while True:
        try:
            idade = int(input(mensagem))

            if idade < 5 or idade > 125:
                print(f"{vermelho}Idade inválida!{reset}")
            else:
                return idade

        except ValueError:
            print(f"{vermelho}Digite apenas números!{reset}")

def validar_nota():

    notas = []
    nomes_notas = ["1ª", "2ª", "3ª"]

    for c in range(0, 3):

        while True:
            try:
                nota = float(input(f"{nomes_notas[c]} Nota: ").replace(",", "."))

                if nota < 0 or nota > 10:
                    print(f"{vermelho}Nota inválida! Digite entre 0 e 10.{reset}")
                else:
                    notas.append(nota)
                    break

            except ValueError:
                print(f"{vermelho}Digite apenas números!{reset}")

    media = round(sum(notas) / 3, 2)

    return notas, media


def validar_matricula(mensagem="Digite a matrícula do aluno(a): "):

    while True:

        matricula = input(mensagem).strip()

        if matricula.isdigit() and len(matricula) == 5:
            return matricula

        else:
            print(f"{vermelho}Matrícula inválida! Digite os 5 números.{reset}")


def calcular_situacao(nota):

    if nota >= 7:
        return f"{verde}APROVADO{reset}"

    elif nota >= 5:
        return f"{laranja}RECUPERAÇÃO{reset}"

    else:
        return f"{vermelho}REPROVADO{reset}"


# ==========================
# EMITIR CERTIFICADO
# ==========================

def emitir_certificado(aluno):

    aprovado = True

    for disciplina in aluno["disciplinas"]:

        if disciplina["media"] < 7:
            aprovado = False

    if aprovado:
        print()
        print(f"{laranja}" + "=" * 45)
        print("          CERTIFICADO DE APROVAÇÃO")
        print("=" * 45 + f"{reset}")

        print(f"\nCertificamos, para os devidos fins, que \033[1;32m{aluno['nome']}\033[0m concluiu com sucesso as seguintes disciplinas:")

        for disciplina in aluno["disciplinas"]:

            print(f"- {disciplina['nome']} | Média: {disciplina['media']}")

        print(f"\nRESULTADO FINAL: {verde}APROVADO{reset}")

        print(f"\n{laranja}" + "=" * 45)
        print("       PARABÉNS PELA CONQUISTA!")
        print("=" * 45 + f"{reset}")

    else:

        print(f"{vermelho}Aluno não possui aprovação em todas as disciplinas.{reset}")


# ==========================
# INFORMAÇÕES ANTES DO CADASTRO
# ==========================

imprimir("-")

# ==========================
# MENU CADASTRO
# ==========================

while True:

    print(f"\n{azul}-=-=-=-=-=- SISTEMA ESCOLAR -=-=-=-=-=-{reset}")
    print("\n1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Pesquisar Aluno")
    print("4 - Editar Aluno")
    print("5 - Remover Aluno")
    print("6 - Cadastrar Professor")
    print("7 - Listar Professores")
    print("8 - Editar Professor")
    print("9 - Remover Professor")
    print("10 - Emitir Certificado")
    print("11 - Sair")

    opcao = input("\nEscolha uma opção: ")
    print()
    imprimir("-" * 40)

    # ==========================
    # CADASTRAR ALUNO
    # ==========================

    if opcao == "1":

        print()
        print("Este módulo é destinado ao cadastro de")
        print("estudantes da área de Tecnologia da")
        imprimir("Informação (TI).")

        nome = validar_texto()
        idade = validar_idade()
        curso = validar_texto("Digite o nome do curso: ")
        
        numero = f"{proximo_numero:05d}"

        print()
        print(f"{laranja}ATENÇÃO!{reset}")
        print("Cada disciplina possui 3 avaliações.")
        print("As notas devem ser informadas de 0 a 10.")
        

        disciplinas = []

        for c in range(0, 3):

            print(f"\n{'-' * 10} {c+1}ª DISCIPLINA {'-' * 10}")
            print()
            imprimir(nomes_disciplinas[c])

            notas, media = validar_nota()

            situacao = calcular_situacao(media)

            disciplinas.append({
                "nome": nomes_disciplinas[c],
                "notas": notas,
                "media": media,
                "situacao": situacao
            })

        aluno = {
            "Numero de Matricula": numero,
            "nome": nome,
            "idade": idade,
            "curso": curso,
            "disciplinas": disciplinas
        }

        alunos.append(aluno)
        proximo_numero += 1

        imprimir(f"\n{verde}Aluno cadastrado com sucesso!{reset}")
        imprimir(f"{verde}Número de matrícula: {numero}{reset}")

    # ==========================
    # LISTAR ALUNOS
    # ==========================

    elif opcao == "2":

        if len(alunos) == 0:

            print(f"{vermelho}\nNenhum aluno cadastrado.{reset}")

        else:

            imprimir("\n=== ALUNOS CADASTRADOS ===")

            for aluno in alunos:

                print()
                print("=" * 40)
                print(f"Matrícula: {negrito}{aluno['Numero de Matricula']}{reset}")
                print(f"Nome: {negrito}{aluno['nome']}{reset}")
                print(f"Idade: {negrito}{aluno['idade']}{reset}")
                print(f"Curso: {aluno['curso']}")

                for disciplina in aluno["disciplinas"]:

                    notas_formatadas = " | ".join(f"{n:.1f}" for n in disciplina["notas"])
                    print()
                    print(f"  Disciplina: {sublinhado}{disciplina['nome']}{reset}")
                    print(f"  Notas: {negrito}{notas_formatadas}{reset}")
                    print(f"  Média: {negrito}{disciplina['media']:.2f}{reset}")
                    print(f"  Situação: {disciplina['situacao']}")

                print()

        imprimir("-" * 40)

    # ==========================
    # PESQUISAR ALUNO
    # ==========================

    elif opcao == "3":

        matricula_busca = validar_matricula()

        encontrado = False

        for aluno in alunos:

            if matricula_busca == aluno["Numero de Matricula"]:

                print(f"\n{verde}=== ALUNO ENCONTRADO ==={reset}")
                print(f"Matrícula: {aluno['Numero de Matricula']}")
                print(f"Nome: {aluno['nome']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Curso: {aluno['curso']}")

                for disciplina in aluno["disciplinas"]:

                    notas_formatadas = " | ".join(f"{n:.1f}" for n in disciplina["notas"])
                    print()
                    print(f"Disciplina: {disciplina['nome']}")
                    print(f"Notas: {notas_formatadas}")
                    print(f"Média: {disciplina['media']:.2f}")
                    print(f"Situação: {disciplina['situacao']}")

                encontrado = True
                break

        if not encontrado:
            print(f"{vermelho}Aluno não encontrado!{reset}")
        imprimir("-" * 40)

    # ==========================
    # EDITAR ALUNO
    # ==========================

    elif opcao == "4":

        matricula_busca = validar_matricula()

        encontrado = False

        for aluno in alunos:

            if matricula_busca == aluno["Numero de Matricula"]:

                encontrado = True

                print(f"\nAluno encontrado: {aluno['nome']}")

                while True:

                    print("\n===== EDITAR ALUNO =====")
                    print("1 - Alterar nome")
                    print("2 - Alterar idade")
                    print("3 - Alterar curso")
                    print("4 - Alterar as notas das disciplinas")
                    print("5 - Alterar todas as Informações")
                    print("6 - Voltar ao menu principal")

                    edicao = input("\nEscolher uma opção: ")

                    if edicao == "1":

                        aluno["nome"] = validar_texto("Novo nome: ")
                        print(f"{verde}Nome atualizado com sucesso!{reset}")

                    elif edicao == "2":

                        aluno["idade"] = validar_idade("Nova idade: ")
                        print(f"{verde}Idade atualizada com sucesso!{reset}")

                    elif edicao == "3":

                        aluno["curso"] = validar_texto("Novo curso: ")
                        print(f"{verde}Curso atualizado com sucesso!{reset}")

                    elif edicao == "4":

                        print("\n===== ALTERAR NOTAS =====")

                        for c in range(len(aluno["disciplinas"])):
                            print(f"{c+1} - {aluno['disciplinas'][c]['nome']}")

                        print(f"{len(aluno['disciplinas'])+1} - Voltar")

                        escolha = input("\nEscolha a disciplina: ")

                        if escolha.isdigit():

                            escolha = int(escolha)

                            if 1 <= escolha <= len(aluno["disciplinas"]):

                                disciplina = aluno["disciplinas"][escolha - 1]

                                print(f"\nDisciplina: {disciplina['nome']}")
                                print("informe as nova notas:")

                                notas, media = validar_nota()

                                disciplina["notas"] = notas
                                disciplina["media"] = media
                                disciplina["situacao"] = calcular_situacao(media)

                                print(f"\n{verde}Notas atualizadas!{reset}")

                            elif escolha == len(aluno["disciplinas"]) + 1:

                                print("\nVolta ao menu.")

                            else:
                                print(f"{vermelho}Disciplina inválida!{reset}")

                        else:

                            print(f"{vermelho}Digite uma opção válida{reset}")

                    elif edicao == "5":

                        aluno["nome"] = validar_texto("Novo nome: ")
                        aluno["idade"]= validar_idade("Nova idade: ")
                        aluno["curso"]= validar_texto("Novo curso: ")

                        for diciplina in aluno["disciplinas"]:

                            print(f"\nDisciplina: {disciplina['nome']}")

                            notas, media = validar_nota()

                            disciplina["notas"]= notas
                            disciplina["media"]= media
                            disciplina["situacao"]= calcular_situacao(media)

                        print(f"{verde}Informações atualizadas{reset}")

                    elif edicao =="6":

                        imprimir("\nVoltar ao menu principal...")
                        break

                    else:
                        print(f"{vermelho}Opção inválida!{reset}")

                break
            if not encontrado:

                print(f"\n{vermelho}Aluno não encontrado!{reset}")

                imprimir("-"*40)
                
    # ==========================
    # REMOVER ALUNO
    # ==========================

    elif opcao == "5":

        if len(alunos) == 0:

            print(f"{vermelho}Nenhum aluno cadastrado.{reset}")

        else:

            matricula_busca = validar_matricula()

            removido = False

            for aluno in alunos:

                if matricula_busca == aluno["Numero de Matricula"]:

                    confirmar = input(f"Confirma remover {aluno['nome']}? (S/N): ").upper()

                    if confirmar == "S":

                        alunos.remove(aluno)

                        print(f"{verde}\nAluno removido com sucesso!{reset}")
                        print()
                        imprimir("-" * 40)

                    else:
                        print(f"{vermelho}Operação cancelada.{reset}")
                        print()
                        imprimir("-" * 40)

                    removido = True
                    break

            if not removido:
                print("\nAluno não encontrado.")
                print()
                imprimir("-" * 40)

    # ==========================
    # CADASTRAR PROFESSOR
    # ==========================

    elif opcao == "6":

        professor = validar_texto("Digite o nome completo do professor: ")
        
        idade = validar_idade("Digite a idade: ")

        disciplina = validar_texto("Digite a disciplina: ")

        professor = {
            "nome": professor,
            "idade": idade,
            "disciplina": disciplina
        }

        professores.append(professor)

        print(f"{verde}\nProfessor cadastrado com sucesso!{reset}")
        print()
        imprimir("-" * 40)

    # ==========================
    # LISTAR PROFESSORES
    # ==========================

    elif opcao == "7":

        if len(professores) == 0:
            print(f"{vermelho}\nNenhum professor cadastrado.{reset}")

        else:
            print("\n=== PROFESSORES CADASTRADOS ===")

            for professor in professores:

                print(f"Nome: {verde}{professor['nome']}{reset}")
                print(f"Idade: {verde}{professor['idade']} anos{reset}")
                print(f"Disciplina: {verde}{professor['disciplina']}{reset}")
                print("-" * 30)

                

    # ==========================
    # EDITAR PROFESSOR
    # ==========================

    elif opcao == "8":

        matricula_busca = validar_texto("Digite o nome completo do professor para editar: ").lower()

        encontrado = False

        for professor in professores:

            if professor["nome"].lower() == matricula_busca:

                professor["nome"] = validar_texto(f"Novo nome ({professor['nome']}): ")
                
                professor["idade"] = validar_idade(f"Nova idade ({professor['idade']}): ")

                professor["disciplina"] = validar_texto(f"Nova disciplina ({professor['disciplina']}): ")

                print(f"{verde}\nProfessor atualizado com sucesso!{reset}")
                print()
                imprimir("-" * 40)

                encontrado = True
                break

        if not encontrado:
            print(f"{vermelho}Professor não encontrado.{reset}")
            print()
            imprimir("-" * 40)

    # ==========================
    # REMOVER PROFESSOR
    # ==========================

    elif opcao == "9":

        if len(professores) == 0:
            print("Nenhum professor cadastrado.")

        else:
            matricula_busca = input("Digite o nome completo do professor para remover: ").lower()

            removido = False

            for professor in professores:

                if professor["nome"].lower() == matricula_busca:

                    confirmar = input(f"Confirma remover {professor['nome']}? (S/N): ").upper()

                    if confirmar == "S":
                        professores.remove(professor)
                        print(f"{verde}\nProfessor removido com sucesso!{reset}")

                    else:
                        print("Operação cancelada.")

                    removido = True
                    break

            if not removido:
                print("\nProfessor não encontrado.")
                print()
                imprimir("-" * 40)

    # ==========================
    # EMITIR CERTIFICADO
    # ==========================

    elif opcao == "10":

        if len(alunos) == 0:

            print(f"{vermelho}Nenhum aluno cadastrado.{reset}")

        else:

            matricula_busca = validar_matricula("Digite a matrícula do aluno(a) para a emissão do certificado: ")

            encontrado = False

            for aluno in alunos:

                if matricula_busca == aluno["Numero de Matricula"]:

                    emitir_certificado(aluno)
                    encontrado = True
                    break

            if not encontrado:
                print(f"{vermelho}Aluno não encontrado.{reset}")

    # ==========================
    # SAIR
    # ==========================

    elif opcao == "11":

        print(f"{verde}\nSistema encerrado. 0brigado!{reset}")
        break

    # ==========================
    # OPÇÃO INVÁLIDA
    # ==========================

    else:

        print("\nOpção inválida.")
        print()
        imprimir("-" * 40)