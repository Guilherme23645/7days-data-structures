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
			print("\t",self.itens[i],self.quantidades[i])

l = ListaDeCompras()

x = "S"

while x == "S":
	acao = input("\n\nQue ação deseja fazer?\n\n\tAdicionar items(A)\n\tRemover items(R)\n\tListar items(L)\n\n\t").strip().upper()

	while acao not in "ARL":
		print("\n\nCaractere inválido\n\n")

		acao = input("Que ação deseja fazer?\n\n\tAdicionar items(A)\n\tRemover items(R)\n\tListar items(L)").strip().upper()

	if acao == "A":
		print("\n\nAdicionando item")
		l.adicionar_item(input("\n\n\tNome do item: "), int(input("\n\tQuantidade: ")))
	elif acao == "R":
		if l.itens == []:
			print("\n\nNão há item a ser removido.")
		else:
			print("\n\nRemovendo item")
			l.remover_item(input("\n\n\tNome do item: "))
	elif acao == "L":
		print("\n\n")
		l.listar_itens()

	x = input("\n\nGostaria de fazer mais uma ação: (S/N) ").strip().upper()

	while x not in "SN":
		print("\n\nCaractere inválido")
		x = input("\n\nGostaria de fazer mais uma ação: (S/N) ").strip().upper()









