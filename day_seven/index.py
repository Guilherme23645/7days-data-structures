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
		else:


	def __inserir(self,produto,node):
		self.produto = produto
		self.node = node

		if produto.id < node.produto.id:
			if node.esquerda is None:
				new_node = Node(produto)
				node.esquerda = new_node
			else:
				self.__inserir(produto, node.esquerda)
		elif produto.id > node.produto.id:
			if node.direita is None:
				new_node = Node(produto)
				node.direita = new_node
			else:
				self.__inserir(produto, node.direita)
		else:
			self.node = Node(produto)


	def buscar(self,id):
		pass
