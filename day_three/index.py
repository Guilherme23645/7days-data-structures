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

	def remover_produto(self, produto):
		remover = self.head

		while remover.nome != produto:
			remover = remover.proximo

		remover.nome = remover.proximo.nome
		remover.codigo = remover.proximo.codigo
		remover.preco = remover.proximo.preco
		remover.quantidade = remover.proximo.quantidade
		remover.proximo = remover.proximo.proximo

	def atualizar_produto(self, produto, nome, codigo, preco, quantidade):
		remover = self.head

		while remover.nome != produto:
			remover = remover.proximo

		remover.nome = nome
		remover.codigo = codigo
		remover.preco = preco
		remover.quantidade = quantidade
		# git checkout 851669c para versão com argumentos palavra-chave

	def listar_produtos(self):
		produto = self.head

		while produto != None:
			print(f"Nome: {produto.nome}, Código: {produto.codigo}, Preço: R${produto.preco:.2f}, Quantidade: {produto.quantidade}")
			produto = produto.proximo
