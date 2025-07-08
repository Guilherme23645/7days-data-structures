class ListaDeCompras:
	def __init__(self):
		self.itens = []
		self.quantidades = []

	def adicionar_item(self, item, quantidade):
		self.itens.append(item)
		self.quantidades.append(quantidade)

	def remover_item(self, item):
		i = self.itens.index(item)
		self.itens.pop(i)
		self.quantidades.pop(i)

	def listar_itens(self):
		for i in range(len(self.itens)):
			print(self.itens[i],self.quantidades[i])

l = ListaDeCompras()
l.adicionar_item("Cebola",5)
l.adicionar_item("Alface",2)
l.adicionar_item("Tomate",6)
l.adicionar_item("Chocolate",1)
l.remover_item("Chocolate")
l.listar_itens()
