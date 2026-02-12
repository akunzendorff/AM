# Importante: Identação é fundamental em Python, ela define o escopo do código
def adicionar_item(carrinho: dict[str, float], item: str, preco: float) -> None:
    carrinho[item] = preco
    print(f'"{item}" => {preco} - adicionado ao carrinho')

    if (preco > 100):
        print("Cupom de desconto disponível")

meu_carrinho: dict[str, float] = {}
adicionar_item(meu_carrinho, "Notebook", 1500)
adicionar_item(meu_carrinho, "Mouse", 50)
adicionar_item(meu_carrinho, "Teclado", 200)

print(meu_carrinho)