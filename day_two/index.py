class Paciente:
	def __init__(self, nome, id, estado):
		self.nome = nome
		self.id = id
		self.estado = estado
		self.proximo = None

class ListaDePacientes:
	def __init__(self):
		self.head = None
		self.tail = None

	def adicionar_paciente(self, nome, id, estado):
		paciente = Paciente(nome, id, estado)

		if self.head == None:
			self.head = self.tail = paciente
		else:
			if self.head.proximo == None:
				self.tail = paciente
				self.head.proximo = self.tail
			else:
				self.tail.proximo = paciente
				self.tail = self.tail.proximo

	def remover_paciente(self, paciente):
		if paciente == self.head.nome:
			remover = self.head

			while remover.proximo != None:
				remover = remover.proximo
		elif paciente == self.tail.nome:
			remover = self.head

			while remover.proximo != self.tail:
				remover = remover.proximo

			self.tail = remover
			remover.proximo = None
		else:
			remover = self.head

			while remover.nome != paciente:
				remover = remover.proximo

			while remover.proximo != None:
				pass


	def listar_pacientes(self):
		listar = self.head

		print(listar.nome, listar.id, listar.estado)

		while listar.proximo != None:
			listar = listar.proximo
			print(listar.nome, listar.id, listar.estado)
