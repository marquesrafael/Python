from sqlalchemy import false, true

class JogoDaVelha:
    tabuleiro = {"7": " ", "8": " ", "9": " ",
                 "4": " ", "5": " ", "6": " ",
                 "1": " ", "2": " ", "3": " "}
    turno = None

    def __init__(self, jogador_inicial = "X"):
        self.turno = jogador_inicial

    def exibirTabuleiro(self):
        print("┌───┬───┬───┐")
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("└───┴───┴───┘")

    def verificarJogada(self, jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == " ":
                return true
            return false
    
    def verificarTabuleiro(self):
        # Verificar Vertical
        if self.tabuleiro["7"] == self.tabuleiro["4"] == self.tabuleiro["1"] != " ":
            return self.tabuleiro["7"]
        elif self.tabuleiro["8"] == self.tabuleiro["5"] == self.tabuleiro["2"] != " ":
            return self.tabuleiro["8"]
        elif self.tabuleiro["9"] == self.tabuleiro["6"] == self.tabuleiro["3"] != " ":
            return self.tabuleiro["9"]

        # Verificar Horizontal
        if self.tabuleiro["7"] == self.tabuleiro["8"] == self.tabuleiro["9"] != " ":
            return self.tabuleiro["7"]
        elif self.tabuleiro["4"] == self.tabuleiro["5"] == self.tabuleiro["6"] != " ":
            return self.tabuleiro["4"]
        elif self.tabuleiro["1"] == self.tabuleiro["2"] == self.tabuleiro["3"] != " ":
            return self.tabuleiro["1"]
        
        # Verificar Diagonal
        if self.tabuleiro["7"] == self.tabuleiro["5"] == self.tabuleiro["3"] != " ":
            return self.tabuleiro["7"]
        elif self.tabuleiro["1"] == self.tabuleiro["5"] == self.tabuleiro["9"] != " ":
            return self.tabuleiro["1"]

        # Verificar Empate
        if [*self.tabuleiro.values()].count(" ") == 0:
            return "Empate"
        else:
            return [*self.tabuleiro.values()].count(" ")

    # Para iniciar o Jogo
    def jogar(self):
        while true:
            self.exibirTabuleiro()
            print(f"Turno do {self.turno}, qual sua jogada?")

            # Enquanto não for uma jogada válida
            while true:
                jogada = input("Jogada: ")
                if self.verificarJogada(jogada): # Se for valida, finaliza
                    break
                else:
                    print(f"Jogada do {self.turno} é inválida, jogue novamente")

            self.tabuleiro[jogada] = self.turno
            estado = self.verificarTabuleiro()

            if estado == "X":
                print("X é o vencedor")
                break

            elif estado == "O":
                print("O é o vencedor")
                break

            if estado == "Empate":
                print("Empate")
                break

            # Próximo jogador
            self.turno = "X" if self.turno == "O" else "O"

        self.exibirTabuleiro()

jogo = JogoDaVelha()
jogo.jogar()