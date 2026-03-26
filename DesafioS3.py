import nltk

dicionario = {
    'beneficente': 'Que faz o bem; caritativo.',
    'cumprimento': 'Ato de cumprimentar ou realizar algo.',
    'comprimento': 'Extensão de uma ponta a outra.',
    'tráfego': 'Trânsito de veículos.',
    'tráfico': 'Comércio ilegal.',
    'iminente': 'Que está prestes a acontecer.',
    'eminente': 'Alto, elevado, ilustre.',
    'descrição': 'Ato de descrever algo.',
    'discrição': 'Qualidade de quem é discreto.'
}

def verificar(palavra_usuario):
	encontrou=False
	for p in dicionario.keys():
		distancia= nltk.edit_distance(p,palavra_usuario.lower())
		if (distancia==0):
			print(f"Palavra encontrada: {p}")
			print(f"Significado: {dicionario[p]}")
			encontrou=True
			break
		elif(distancia<=2):
			print(f"Você quis dizer '{p}'? O significado é: {dicionario[p]}")
			encontrou =True
			break
	if not encontrou:
		print("Palavra incorreta ou não encotrada no banco de dados")
#teste
busca=input("Digite a palavra para saber o significado: ")
verificar(busca)