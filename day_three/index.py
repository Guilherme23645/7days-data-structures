class Produto:
	def __init__(self,nome,codigo,preco,quantidade):
		self.nome = nome
		self.codigo = codigo
		self.preco = preco
		self.quantidade = quantidade
		self.anterior = None
		self.proximo = None

class ListaDeProdutos:
	def __init__(self):
		self.head = None
		self.tail = None

	def adicionar_produto(self, nome, codigo, preco, quantidade):
		produto = Produto(nome, codigo, preco, quantidade)

		if self.head == None:
			self.head = self.tail = produto
		else:
			if self.head.proximo == None:
				self.tail = produto
				self.tail.anterior = self.head
				self.head.proximo = self.tail
			else:
				produto.anterior = self.tail
				self.tail.proximo = produto
				self.tail = produto

	def remover_produto(self):
		pass

	def atualizar_produto(self):
		pass

	def listar_produtos(self):
		pass
