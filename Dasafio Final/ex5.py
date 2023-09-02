import mysql.connector

class Agenda:
    def __int__(self, peso_gramas, preco_por_quilo, valor_total):
        self.peso_gramas = peso_gramas
        self.peso_por_quilo = preco_por_quilo
        self.valor_total = valor_total

    def inserir(self, peso_gramas, preco_por_quilo, valor_total):
        try:
            conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='vendas')
            cursor = conexao.cursor()
            query = "INSERT INTO vendaspeixe (peso_gramas, preco_por_quilo, valor_total) VALUES (%s, %s, %s)"
            inserir2 = (peso_gramas, preco_por_quilo, valor_total)
            cursor.execute(query, inserir2)
            conexao.commit()
            cursor.close()
        except mysql.connector.Error as erro:
            print(erro)

    def deletar(self,id):
        try:
            conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='vendas')
            cursor = conexao.cursor()
            query = "DELETE FROM vendaspeixe WHERE id = %s"
            inserir2 = (id,)
            cursor.execute(query, inserir2)
            conexao.commit()
            cursor.close()
        except mysql.connector.Error as erro:
            print(erro)

    def mostrar(self, id):
        try:
            conexao = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="vendas")
            cursor = conexao.cursor()
            inserir = f"SELECT * FROM `vendaspeixe` WHERE id = %s;"
            valores = (id,)
            cursor.execute(inserir, valores)
            for (id, peso_gramas, preco_por_quilo, valor_total) in cursor:
                print(f"id: {id} \nPeso em Grams: {peso_gramas} \n"
                f"Preço po Quilo: {preco_por_quilo} \nValor total: {valor_total}")
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            print(erro)


peixeq = float(input("Digite quantas gramas de peixe deseja comprar: "))
peixep = float(input("Digite o valor do KG do peixe: "))
total = peixep * peixeq
agenda = Agenda()
agenda.inserir(peixeq, peixep, total)
a = input("Digite se deseja consultar (S ou N): ")
if a.upper() == "S":
    id = input("Digite o id: ")
    agenda.mostrar(id)
