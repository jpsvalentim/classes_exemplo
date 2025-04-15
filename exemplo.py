#vamos criar uma classe para Cliente da Netflix
class cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome 
        self.email = email
        self.lista_planos = ["basic","premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano invslido")

    def mudar_plano(self, plano_atual, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("PLANO INVALIDO")


    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"ver filme{filme}")
        elif self.plano == "premium":
            print(f"ver filme: {filme}")
        elif self.plano == "basic" and plano_filme == "Premium":
            print("Faça um upgrade para ter acesso a esse conteudo!")
        else:
            print("Plano invalido")
    


cliente = cliente("joao", "pedro@edu","basic")

print(cliente.plano)
cliente.ver_filme("harry potter" , "premium")
print(cliente.plano)
cliente.ver_filme("harry potter" , "premium")
print(cliente.plano)
cliente.ver_filme("harry potter" , "premium")