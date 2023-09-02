def calcular_valor_total(peso, preco_por_quilo):
    print("Valor total: ", (peso/1000) * preco_por_quilo)

def converter_gramas_para_quilo(pesogramas):
    pesokg = pesogramas / 1000
    print("Peso em Kg: ", pesokg)

peixeq = float(input("Digite quantas gramas de peixe deseja comprar: "))
peixep = float(input("Digite o valor do KG do peixe: "))

converter_gramas_para_quilo(peixeq)
calcular_valor_total(peixeq, peixep)
