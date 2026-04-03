# =========================
# CHANGEMENT DE JOUEUR
# =========================
def switchPlayer(self):
    self.currentPlayer = self.players[1] if self.currentPlayer == self.players[0] else self.players[0]


# =========================
# BOUCLE DE JEU (PLAY)
# =========================
def play(self):
    while True:
        self.board.display()
        print(f"Tour de {self.currentPlayer.name}")

        start, end = self.currentPlayer.askMove()
        piece = self.board.getPiece(start)

        # aucune pièce
        if piece is None:
            print("Aucune pièce ici")
            continue

        # verrouillage des pièces adverses
        if piece.color != self.currentPlayer.color:
            print("Ce n'est pas ta pièce !")
            continue

        # coup invalide
        if not piece.isValidMove(end, self.board):
            print("Coup invalide")
            continue

        # prise de pièce
        target = self.board.getPiece(end)
        if target:
            self.board.pieces.remove(target)

        # déplacement
        piece.position = end

        # changement de joueur
        self.switchPlayer()