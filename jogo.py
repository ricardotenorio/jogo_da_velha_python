def criarTabuleiro():
	return [
		"___",
		"___",
		"___"
	]

def atualizarTabuleiro(jogador, jogada, tabuleiro):
	linha = list(tabuleiro[jogada[0]])
	linha[jogada[1]] = jogador
	tabuleiro[jogada[0]] = "".join(linha)

def imprimirTabuleiro(tabuleiro):
	for linha in tabuleiro:
		for i in range(len(linha)):
			print(linha[i], end = "|" if i < 2 else "")
		print()

def checarVencedor(tabuleiro):
	for i in range(len(tabuleiro)):
		if tabuleiro[i][0] != "_" and tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2]:
			return True
		if tabuleiro[0][i] != "_" and tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i]:
			return True

	if tabuleiro[0][0] != "_" and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
		return True
	if tabuleiro[0][2] != "_" and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
		return True

	return False

def fazerJogada():
	linha = int(input("Digite o numero da linha: "))
	coluna = int(input("Digite o numero da coluna: "))

	return [linha - 1, coluna - 1]

def validarJogada(jogada, tabuleiro):
	msg = ""
	ehValida = True

	if jogada[0] > 2 or jogada[0] < 0 or jogada[1] > 2 or jogada[1] < 0:
		msg = "Jogada invalida: Posicao nao existe"
		ehValida = False
	elif tabuleiro[jogada[0]][jogada[1]] != "_":
		msg = "Jogada invalida: Posicao ocupada"
		ehValida = False
	else:
		msg = "Jogada valida"

	return [msg, ehValida]

def partida():
	jogador1 = "X"
	jogador2 = "O"
	turno = 0
	tabuleiro = criarTabuleiro()
	proximoTurno = True

	while turno < 9 and proximoTurno:
		jogador = jogador1 if turno % 2 == 0 else jogador2
		imprimirTabuleiro(tabuleiro)
		print("Jogador ", jogador)
		while True:
			try:
				jogada = fazerJogada()
			except Exception as e:
				print("Jogada invalida: Digite um numero...")
				continue
			ehValida = validarJogada(jogada, tabuleiro)

			if ehValida[1]:
				break
			print(ehValida[0])
		atualizarTabuleiro(jogador, jogada, tabuleiro)
		proximoTurno = not checarVencedor(tabuleiro)
		turno += 1

	if turno == 9 and proximoTurno:
		print("Empate")
	else:
		print(jogador + " foi o vencedor")

try:
	while True:
		partida()
except KeyboardInterrupt as e:
	print("\nSaindo...")