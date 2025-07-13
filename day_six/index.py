class Jogo:
	def __init__(self):
		self.jogadores = {}

	def adicionar(self, jogador, pontos):
		self.jogadores[jogador] = pontos

	def remover(self, jogador):
		if jogador not in self.jogadores:
			return

		del self.jogadores[jogador]

	def atualizar(self, jogador, pontos):
		if jogador not in self.jogadores:
			return

		self.jogadores[jogador] = pontos

	def listar(self):
		placar = sorted(self.jogadores.items(), key=lambda x: x[1], reverse=True)

		for i in range(len(placar)):
			if i == 0:
				print(f'Jogador(a): {placar[i][0]}, Pontuação: {placar[i][1]} Vencedor(a)!')
			else:
				print(f'Jogador(a): {placar[i][0]}, Pontuação: {placar[i][1]}')


