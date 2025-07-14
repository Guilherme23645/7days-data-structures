class Produto:
	def __init__(self,id,nome,quantidade):
		self.id = id
		self.nome = nome
		self.quantidade = quantidade

class Node:
	def __init__(self,produto,esquerda=None,direita=None):
		self.produto = produto
		self.esquerda = esquerda
		self.direita = direita

class ArvoreProduto:
	def __init__(self):
		self.raiz = None

	def inserir(self,id,nome,quantidade):
		produto = Produto(id,nome,quantidade)

		if self.raiz is None:
			node = Node(produto)
			self.raiz = node
		else:
			self._inserir(produto,self.raiz)

	def _inserir(self,produto,node):
		if produto.id < node.produto.id:
			if node.esquerda is None:
				new_node = Node(produto)
				node.esquerda = new_node
			else:
				self._inserir(produto, node.esquerda)
		elif produto.id > node.produto.id:
			if node.direita is None:
				new_node = Node(produto)
				node.direita = new_node
			else:
				self._inserir(produto, node.direita)
		else:
			node.produto.nome = produto.nome
			node.produto.quantidade = produto.quantidade


	def buscar(self,id):
		return self._buscar(id,self.raiz)

	def _buscar(self,id,node):
		if node is None or id == node.produto.id:
			return node.produto.nome
		elif id < node.produto.id:
			return self._buscar(id,node.esquerda)
		else:
			return self._buscar(id,node.direita)
