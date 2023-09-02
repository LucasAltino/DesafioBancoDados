lista = []
while True:
    peixeq = float(input("Digite quantas gramas de peixe deseja comprar ou 0 para sair: "))
    if peixeq == 0:
        if len(lista) >= 1:
            QUILO = peixeq / 1000
            PRECO_QUILO_PEIXE = QUILO * peixep
            for c in lista:
                QUILO = QUILO + c
                PRECO_QUILO_PEIXE = QUILO * peixep
            print("Kilos de peixe comprado: ", QUILO, "Valor total (R$): ", PRECO_QUILO_PEIXE)
        break
    else:
        peixep = float(input("Digite o valor do KG do peixe: "))
        lista.append(peixeq)
        if peixep == 0:
            print("Compra cancelada")
            break