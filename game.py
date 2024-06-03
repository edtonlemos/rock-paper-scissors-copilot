import random

def determine_winner(player, computer):
    if player == 1:
        if computer == 1:
            return "Empate!"
        elif computer == 2:
            return "Você perdeu!"
        else:
            return "Você ganhou!"
    elif player == 2:
        if computer == 1:
            return "Você ganhou!"
        elif computer == 2:
            return "Empate!"
        else:
            return "Você perdeu!"
    elif player == 3:
        if computer == 1:
            return "Você perdeu!"
        elif computer == 2:
            return "Você ganhou!"
        else:
            return "Empate!"

def game():
    choices = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
    while True:
        print("Bem vindo ao jogo de pedra, papel e tesoura!")
        print("Escolha uma opção:")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        player = None
        while player not in choices:
            try:
                player = int(input("Digite sua escolha: "))
                if player not in choices:
                    print("Jogada inválida. Por favor, escolha 1, 2 ou 3.")
            except ValueError:
                print("Jogada inválida. Por favor, escolha 1, 2 ou 3.")
        computer = random.randint(1, 3)
        print(f"Você jogou {choices[player]} e o computador jogou {choices[computer]}")
        result = determine_winner(player, computer)
        print(result)
        
        play_again = None
        while play_again not in ["s", "n"]:
            play_again = input("Você quer jogar novamente? (s/n): ").lower()
            if play_again not in ["s", "n"]:
                print("Entrada inválida. Por favor, digite 's' para jogar novamente ou 'n' para sair.")
        if play_again == "n":
            print("Obrigado por jogar!")
            break


if __name__ == "__main__":
    game()  # Chama a função game para iniciar o jogo