class Livro:
	def __init__(self, titulo, paginas):
		self.titulo = titulo
		self.paginas = paginas

class PilhaDeLivros:
	def __init__(self):
		self.livros = []
		self.topo = 0

	def empilhar(self, titulo, paginas):
		self.livros[self.topo] = Livro(titulo, paginas)
		self.topo += 1

	def desempilhar(self):
		if self.livros == []:
			print("Pilha vazia")
			return

		self.topo -= 1

	def buscar(self):
		if self.livros == []:
			print("Pilha vazia")
			return

		return self.livros[self.topo]

	def listar_livros(self):
		if self.livros == []:
			print("Pilha vazia")
			return

		i = 0
		while i <= self.topo:
			print(f"Nome do livro: {self.titulo}, Número de páginas: {self.paginas}")

			i += 1



