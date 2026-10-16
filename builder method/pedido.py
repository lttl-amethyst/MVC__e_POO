class Pedido:
    def __init__(
            self,
            cliente,
            produto,
            quantidade,
            endereco=None,
            cupom=None,
            frete=None,
            pagamento=None
    ):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.endereco = endereco
        self.cupom = cupom
        self.frete = frete
        self.pagamento = pagamento

    def mostrar(self):
        print("-- PEDIDO --")
        print(f"Cliente: {self.cliente}")
        print(f"Produto: {self.produto}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Endereço: {self.endereco}")
        print(f"Cupom: {self.cupom}")
        print(f"Frete: {self.frete}")
        print(f"Pagamento: {self.pagamento}")
        