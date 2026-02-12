"""Classes Simples em python"""

class CarrinhoDeCompras:
    """Representa um carrinho de compras."""

    def __init__(self) -> None:
        """Inicializa um carrinho de compras vazio."""
        self.itens = {}

    def adicionar_item(self, item: str, preco: float) -> None:
        """Adiciona um item ao carrinho de compras."""
        self.itens[item] = preco
        print(f'"{item}" => R$ {preco:.2f} - adicionado ao carrinho')

    def calcular_total(self) -> float:
        """Calcula o total dos itens no carrinho."""
        total = sum(self.itens.values())
        return total
    
    
# Como usar a classe
if __name__ == "__main__":
    print("Bem vindo(a) a amazon!")
    print("-" * 50)

    # Criação do carrinho
    meu_carrinho = CarrinhoDeCompras()

    # Adicionando itens
    meu_carrinho.adicionar_item("Camisa", 59.90)
    meu_carrinho.adicionar_item("Calça Jeans", 129.99)

    # Total do carrinho
    print("-" * 50)
    valor_total = meu_carrinho.calcular_total()
    print(f"O valor total da compra é: R$ {valor_total:.2f}")