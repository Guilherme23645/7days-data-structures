class Livro:
	def __init__(self, titulo, paginas):
		self.titulo = titulo
		self.paginas = paginas

class PilhaDeLivros:
	def __init__(self, capacidade):
		self.topo = -1
		self.capacidade = capacidade
		self.livros = [None] * self.capacidade

	def empilhar(self, titulo, paginas):
		if self.topo == self.capacidade - 1:
			print("Pilha cheia")
			return

		self.topo += 1
		self.livros[self.topo] = Livro(titulo, paginas)

	def desempilhar(self):
		if self.topo == -1:
			print("Pilha vazia")
			return

		self.topo -= 1

	def buscar(self):
		if self.topo == -1:
			print("Pilha vazia")
			return

		return self.livros[self.topo].titulo

	def listar_livros(self):
		if self.topo == -1:
			print("Pilha vazia")
			return

		i = self.topo
		while i > -1:
			print(f"Nome do livro: {self.livros[i].titulo}, Número de páginas: {self.livros[i].paginas}")

			i -= 1



