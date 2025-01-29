class ControleRemoto:
    def __init__(self, cor, altura,profundidade,largura):
        self.cor = cor 
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumenta o canal")

        elif botao == "-":
            print("Diminuir o canal")



controle_remoto01 = ControleRemoto("preto", "10","3","5")
print(controle_remoto01.cor)

controle_remoto01.passar_canal("+")