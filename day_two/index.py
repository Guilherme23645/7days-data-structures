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
		remover = self.head

		while remover.nome != paciente:
			remover = remover.proximo

		remover.nome = remover.proximo.nome
		remover.id = remover.proximo.id
		remover.estado = remover.proximo.estado
		remover.proximo = remover.proximo.proximo


	def listar_pacientes(self):
		listar = self.head

		print(listar.nome, listar.id, listar.estado)

		while listar.proximo != None:
			listar = listar.proximo
			print(listar.nome, listar.id, listar.estado)
