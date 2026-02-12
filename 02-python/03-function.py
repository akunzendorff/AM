"""Carrinho de compras"""

from typing import Dict

# Type Alias
Carrinho = Dict[str, float]

def adicionar_item(carrinho: Carrinho, item: str, preco: float) -> None:
    """Adiciona um item ao carrinho de compras"""
    carrinho[item] = preco
    print(f'"{item}" => R$ {preco:.2f} - adicionado ao carrinho')

def calcular_total(carrinho: Carrinho) -> float:
    """Calcula o total dos itens"""
    total = sum(carrinho.values())
    return total

def finalizar_compra(carrinho: Carrinho) -> None:
    """Finalizar a compra e zera o carrinho"""
    finalizar = input("Digite S para finalizar a compra ou N para cancelar => ")
    if finalizar == "S":
        carrinho.clear()
        print("Compra realizada com sucesso! Volte sempre")


if __name__ == "__main__":
    print("Bem vindo(a) a amazon!")
    print("-" * 50)

    # Criação do carrinho vazio
    meu_carrinho: Carrinho = {}

    # Adicionando itens
    adicionar_item(meu_carrinho, "Camisa", 59.90)
    adicionar_item(meu_carrinho, "Calça Jeans", 129.99)
    adicionar_item(meu_carrinho, "Meia", 15.00)

    # Total do carrinho
    print("-" * 50)
    valor_total = calcular_total(meu_carrinho)
    print(f"O valor total da compra é: R$ {valor_total:.2f}")

    print("-" * 50)

    # Input do cliente
    print("Deseja finalizar a compra ?")
    finalizar_compra(meu_carrinho)