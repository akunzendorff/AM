"""Carrinho de compras - Versão Orientada a Objetos"""

from typing import Dict

class CarrinhoDeCompras:
    """Representa um carrinho de compras."""

    def __init__(self) -> None:
        """Inicializa um carrinho de compras vazio."""
        self._itens: Dict[str, float] = {}

    def adicionar_item(self, item: str, preco: float) -> None:
        """Adiciona um item ao carrinho de compras."""
        self._itens[item] = preco
        print(f'"{item}" => R$ {preco:.2f} - adicionado ao carrinho')

    def calcular_total(self) -> float:
        """Calcula o total dos itens no carrinho."""
        total = sum(self._itens.values())
        return total

    def finalizar_compra(self) -> None:
        """Finaliza a compra e esvazia o carrinho."""
        finalizar = input("Digite S para finalizar a compra ou N para cancelar => ")
        if finalizar.upper() == "S":
            self._itens.clear()
            print("Compra realizada com sucesso! Volte sempre")
        else:
            print("Compra cancelada.")

    # Métodos especiais ou métodos mágicos
    def __str__(self) -> str:
        """Retorna uma representação em string do carrinho."""
        if not self._itens:
            return "Carrinho vazio."
        itens_str = "\n".join(f"- {item}: R$ {preco:.2f}" for item, preco in self._itens.items())
        return f"Itens no carrinho:\n{itens_str}"


if __name__ == "__main__":
    print("Bem vindo(a) a amazon!")
    print("-" * 50)

    # Criação do carrinho
    meu_carrinho = CarrinhoDeCompras()

    # Adicionando itens
    meu_carrinho.adicionar_item("Camisa", 59.90)
    meu_carrinho.adicionar_item("Calça Jeans", 129.99)
    meu_carrinho.adicionar_item("Meia", 15.00)

    # Mostrando itens no carrinho
    print("-" * 50)
    print(meu_carrinho)

    # Total do carrinho
    print("-" * 50)
    valor_total = meu_carrinho.calcular_total()
    print(f"O valor total da compra é: R$ {valor_total:.2f}")

    print("-" * 50)

    # Input do cliente
    print("Deseja finalizar a compra ?")
    meu_carrinho.finalizar_compra()

    # Verificando se o carrinho está vazio
    print(meu_carrinho)