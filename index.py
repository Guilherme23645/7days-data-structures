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
			print(f"\t{self.itens[i]}: {self.quantidades[i]}")

l = ListaDeCompras()

x = "S"

while x == "S":
	acao = input("\n\nQue ação deseja fazer?\n\n\tAdicionar items(A)\n\tRemover items(R)\n\tListar items(L)\n\n\t").strip().upper()

	while acao not in "ARL":
		print("\n\nCaractere inválido\n\n")

		acao = input("Que ação deseja fazer?\n\n\tAdicionar items(A)\n\tRemover items(R)\n\tListar items(L)").strip().upper()

	if acao == "A":
		print("\n\nAdicionando item")

		item = input("\n\n\tNome do item: ").strip()

		while not item.isalpha():
			print("\n\n\tFormato inválido")

			item = input("\n\n\tNome do item: ").strip()

		quantidade = int(input("\n\n\tQuantidade: ").strip())

		while quantidade <= 0:
			print("\n\n\tQuantidade deve ser maior ou igual a 1")

			quantidade = int(input("\n\n\tQuantidade: ").strip())

		l.adicionar_item(item, quantidade)
	elif acao == "R":
		if l.itens == []:
			print("\n\n\tNão há item a ser removido.")
		else:
			print("\n\nRemovendo item")

			item = input("\n\n\tNome do item: ").strip()

			while item.upper() not in list(map(lambda x: x.upper(), l.itens)):
				print("\n\n\tItem não se encontra na lista")

				item = input("\n\n\tNome do item: ").strip()

			for i in l.itens:
				if item.upper() == i.upper():
					item = i

			l.remover_item(item)
	elif acao == "L":
		print("\n\n")
		l.listar_itens()

	x = input("\n\nGostaria de fazer mais uma ação: (S/N) ").strip().upper()

	while x not in "SN":
		print("\n\nCaractere inválido")
		x = input("\n\nGostaria de fazer mais uma ação: (S/N) ").strip().upper()









