#lazy initialization
from SistemaAtividade import SistemaAtividade
class ProxyVirtual:
    def __init__(self):
        self.sistema = None
    def buscar_atividade(self, id):
        if self.sistema is None:
            print("Inicializando o sistema de atividades")
            self.sistema = SistemaAtividade()
        return self.sistema.buscar_atividade(id)

proxy = ProxyVirtual()
print("proxy criado mas o sistema ainda está off")
resultado = proxy.buscar_atividade(10)
print(resultado)
resultado = proxy.buscar_atividade(5)
print(resultado)