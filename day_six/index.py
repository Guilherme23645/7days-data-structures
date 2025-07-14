class Jogo:
	def __init__(self):
		self.jogadores = {}

	def adicionar(self, jogador, pontos):
		self.jogadores[jogador] = pontos

	def remover(self, jogador):
		if jogador not in self.jogadores:
			print("Jogador não está na lista")
			return

		del self.jogadores[jogador]

	def atualizar(self, jogador, pontos):
		if jogador not in self.jogadores:
			print("Jogador não está na lista")
			return

		self.jogadores[jogador] = pontos

	def placar(self):
		if self.jogadores == {}:
			print("Lista vazia")
			return

		placar = sorted(self.jogadores.items(), key=lambda x: x[1], reverse=True)
		maximo = max(self.jogadores.values())

		for i in range(len(placar)):
			print(f'Jogador(a): {placar[i][0]}, Pontuação: {placar[i][1]}')

	def quem_venceu(self):
		if self.jogadores == {}:
			print("Lista vazia")
			return

		placar = sorted(self.jogadores.items(), key=lambda x: x[1], reverse=True)
		maximo = max(self.jogadores.values())
		quem_venceu = "Vencedor(es): "

		cont = 0
		for i in range(len(placar)):
			if placar[i][1] == maximo:
				if cont > 0:
					quem_venceu += ", "
				quem_venceu += placar[i][0]

				cont += 1

		quem_venceu += "."

		print(quem_venceu)

