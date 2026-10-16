from pedido import Pedido
class PedidoBuilder:
    def __init__(self):
        self.cliente = None
        self.produto = None
        self.quantidade = None
        self.endereco = None
        self.cupom = None
        self.frete = None
        self.pagamento = None
    def set_cliente(self, cliente):
        self.cliente = cliente
        return self
    def set_produto(self, produto):
        self.produto = produto
        return self
    def set_quantidade(self, quantidade):
        self.quantidade = quantidade
        return self
    def set_endereco(self, endereco):
        self.endereco = endereco
        return self
    def set_cupom(self, cupom):
        self.cupom = cupom
        return self
    def set_frete(self, frete):
        self.frete = frete
        return self
    def set_pagamento(self, pagamento):
        self.pagamento = pagamento
        return self
    def construir(self):
        return Pedido(
            self.cliente,
            self.produto,
            self.quantidade,
            self.endereco,
            self.cupom,
            self.frete,
            self.pagamento
        )
    