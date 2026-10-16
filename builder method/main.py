from pedidoBuilder import PedidoBuilder
pedido = (
    PedidoBuilder()
    .set_cliente("Humbigo")
    .set_produto("CD Jar Of Flies")
    .set_quantidade(1)
    .construir()
)
pedido.mostrar()