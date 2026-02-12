# Linguagem de alto nível, interpretada
# Pensada para iniciantes, fácil e intuitiva
# Ótima para tarefas diárias e super produtiva
# Tipagem dinâmica e forte - em tempo de execução
# Multiparadigma - procedural, orientada a objetos e funcional
# Multiplataforma
# Muito usada em ciência de dados, machine learning, automação, web e muito mais
# Grande comunidade e ecossistema de bibliotecas


print("Olá, Python!")

# Variáveis e tipos de dados

# Texto
string = "Python"
mensagem = f"Bem-vindo ao {string}!"
multiplas_linhas = """Isso é um texto
com múltiplas linhas
de exemplo."""


# Números
inteiro = 20
ponto_flutuante = 3.14


# Booleano
verdadeiro = True
falso = False

# Estruturas de dados
lista = [1, 2, 3, 4, 5, 6]
lista_mista = [1, "dois", 3.0, True]

# Imutável
tupla = (10, 20)
tupla_string = ("Python", "LDW")
tupla_mista = (1, "dois", 3.0, False)

lista_mista.append("novo item")
#tupla_mista.append("novo item")  # Isso causaria um erro, tuplas são imutáveis


# Chave : valor
dicionario = {
    "nome": "Python",
    "tipo": "linguagem de programação",
    "versao": 3.14
}

# Não ordenados e mutáveis de elementos únicos
conjunto = {1, 2, 3, 4, 4, 4, 5, 6, 6, 6}
conjunto_string = {"B", "C", "D", "A"}

# Diferença entre dicionário e conjunto
# Dicionário tem chaves e valores, conjunto tem apenas elementos únicos