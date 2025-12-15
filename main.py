from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: int):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        pass

class PagamentoCartao(Pagamento):
    def __init__(self, valor: int, numero_cartao: str):
        super().__init__(valor)
        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        print(f"Processando pagamento de R${self.valor} no cartão {self.numero_cartao}")

class PagamentoPix(Pagamento):
    def __init__(self, valor: int, chave_pix: str):
        super().__init__(valor)
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        print(f"Processando pagamento de R${self.valor} via Pix ({self.chave_pix})")

class PagamentoBoleto(Pagamento):
    def __init__(self, valor: int, codigo_boleto: str):
        super().__init__(valor)
        self.codigo_boleto = codigo_boleto

    def processar_pagamento(self):
        print(f"Processando pagamento de R${self.valor} via Boleto ({self.codigo_boleto})")

pagamentos = [
    PagamentoCartao(100, "1234-5678-9012-3456"),
    PagamentoPix(50, "email@pix.com"),
    PagamentoBoleto(200, "23793.38128 60000.000123")
]

for pagamento in pagamentos:
    pagamento.processar_pagamento()
  
