# Crie uma classe chamada Venda com as propriedades peso (em gramas),
# preço por quilo e valor total. Permita que Zé Pescador registre uma
# venda utilizando um objeto dessa classe. Em seguida, salve os detalhes
# da venda em um arquivo de texto chamado "registro_vendas.txt".

class Venda:
    def __init__(self, peso, preco_por_quilo, valor_total):
        self.peso = peso
        self.preco_por_quilo = preco_por_quilo
        self.valor_total = valor_total

Zé = Venda("1000","2", "2000")

arquivo = open('registro_vendas.txt', 'w')
arquivo.write("Peso: ")
arquivo.write(Zé.peso)
arquivo.write("\n")
arquivo.write("Preço por Quilo: ")
arquivo.write(Zé.preco_por_quilo)
arquivo.write("\n")
arquivo.write("Valor Total: ")
arquivo.write(Zé.valor_total)
arquivo.close()