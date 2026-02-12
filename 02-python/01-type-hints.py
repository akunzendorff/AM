# Type annotations ou type hints - modulo para indicar o tipo de dado esperado
# Não é obrigatório, mas ajuda a melhorar a legibilidade e a detectar erros
# Pode ser usado com ferramentas de análise estática, como mypy, para verificar tipos em tempo de desenvolvimento
# Type são boas práticas, mas não são regras rígidas
from typing import Final

string: str = "Python"
inteiro: int = 20
ponto_flutuante: float = 3.14
booleano: bool = True
lista: list = [1, 2, 3, 4, 5, 6]
lista_numeros: list[int] = [1, 2, 3, 4, 5, 6]

#print(type(inteiro))


# Constantes - Não existem em Python
# PEP8 - Convenção para indicar uma constante é usar letras maiúsculas
# MAX_TENTATIVAS: Final[int] = 5

MAX_TENTATIVAS: Final[int] = 5
#MAX_TENTATIVAS = 10  # Isso causaria um erro, pois MAX_TENTATIVAS é uma constante
#print(MAX_TENTATIVAS)