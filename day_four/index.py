class Pedido:
	def __init__(self,numero,cliente,itens,valor):
		self.numero = numero
		self.cliente = cliente
		self.itens = itens
		self.valor = valor
		self.proximo = None

class FilaDePedidos:
	def __init__(self):
		self.primeiro = None

	def enfileirar(self, numero, cliente, itens, valor):
		pedido = Pedido(numero,cliente,itens,valor)

		if self.primeiro == None:
			self.primeiro = pedido
		else:
			fila = self.primeiro
			while fila.proximo != None:
				fila = fila.proximo

			fila.proximo = pedido

	def desenfileirar(self):
		self.primeiro = self.primeiro.proximo

	def listar_pedidos(self):
		fila = self.primeiro

		while fila != None:
			print(f"Número: {fila.numero}, Cliente: {fila.
cliente}, Itens: {fila.itens}, Valor: {fila.valor}")

			fila = fila.proximo
