class ContaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0
        print(f"Conta de {self.titular} criada. Saldo R${self.saldo}")

    def depositar(self, valor: float):
        if valor <= 0:
            print("Erro... Não é possível depositar um valor menor ou igual a zero.")
        else:
            self.saldo += valor
            print(f"Valor de R${valor: .2f} depositado com sucesso na conta de {self.titular}.\nNovo saldo: R${self.saldo: .2f}")
        
    def sacar(self, valor:float):
        if valor <= 0:
            print("Erro... Não é possível sacar um valor menor ou igual a zero.")
        elif valor > self.saldo:
            print("Erro... Saldo insuficiente para a operação.")
        else:
            self.saldo -= valor
            print(f"Valor de R${valor: .2f} sacado com sucesso na conta de {self.titular}.\nNovo saldo: R${self.saldo: .2f}")
    
    def ver_saldo(self):
        print(f"O saldo da conta de {self.titular} é de R$ {self.saldo: .2f}.")

conta_caua = ContaBancaria("Cauã")
conta_caua.depositar(500)
conta_caua.depositar(-900)
conta_caua.sacar(-600)
conta_caua.sacar(400)
conta_caua.ver_saldo()
