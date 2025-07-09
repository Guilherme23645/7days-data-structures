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
			self.head = paciente
			self.head.proximo = self.tail
		else:
			if self.tail == None:
				self.tail = paciente
			else:
				self.tail.proximo = paciente

	def remover_paciente(self):
		pass

	def listar_pacientes(self):
		pass
