import random
option = ["pedra", "papel", "tesoura"]
ponto_bot = 0
ponto_player = 0

print("#"*50)
print("             --- Online Jokenpô ---")
print("#"*50,"\n")

while True:

    
        player = input("Diga a sua opcao ou 'stop' para parar: ")
        bot = random.choice(option)

        if (player == "pedra") and (bot == "tesoura"):
            print("Droga, eu escolhi tesoura e voce pedra. Voce ganhou.\n")
            ponto_player += 1
        elif (player == "pedra") and (bot == "pedra"):
            print("Temos um empate, eu e voce escolhemos pedra.\n")
        elif (player == "pedra") and (bot == "papel"):
            print("Haha, eu ganhei, prendi sua pedra com meu papel!!\n")
            ponto_bot += 1

        elif (player == "papel") and (bot == "tesoura"):
            print("Haha, eu ganhei, cortei seu papel com minha tesoura.\n")
            ponto_bot += 1
        elif (player == "papel") and (bot == "pedra"):
            print("Droga, eu escolhi pedra e voce papel. Voce ganhou.\n")
            ponto_player += 1
        elif (player == "papel") and (bot == "papel"):
            print("Temos um empate, eu e voce escolhemos papel.\n")

        elif (player == "tesoura") and (bot == "tesoura"):
            print("Temos um empate, eu e voce escolhemos tesoura.\n")
        elif (player == "tesoura") and (bot == "pedra"):
            print("Haha, eu ganhei, destrui sua tesoura com minha pedra.\n")
            ponto_bot += 1
        elif (player == "tesoura") and (bot == "papel"):
            print("Droga, eu escolhi papel e voce tesoura. Voce ganhou.\n")
            ponto_player += 1

        elif player == "stop":
            print("Jogo encerrado.\n")
            break

        else:
            print("Opcao invalida jogador.\n")
print("<","-"*50,">")
print("Contando os pontos...\n")

if ponto_player > ponto_bot:
    print(f"Voce ganhou com {ponto_player} pontos e eu com apenas {ponto_bot} pontos. Droga.\n")
elif ponto_bot > ponto_player:
    print(f"HAHA, eu ganhei com {ponto_bot} pontos, e voce com apenas {ponto_player}. Chore humano.\n")
elif ponto_bot == ponto_player:
    print(f"Parece que acabou em um empate. Nossa pontuacao foi de {ponto_player} pontos.\n")