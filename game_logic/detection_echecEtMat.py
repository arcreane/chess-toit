# =========================
# TROUVER LE ROI
# =========================
def getKing(self, color):
    for piece in self.board.pieces:
        if isinstance(piece, King) and piece.color == color:
            return piece
    return None


# =========================
# DETECTION ECHEC
# =========================
def isCheck(self, color):
    king = self.getKing(color)

    for piece in self.board.pieces:
        if piece.color != color:
            if piece.isValidMove(king.position, self.board):
                return True
    return False


# =========================
# SIMULER UN COUP
# =========================
def simulateMove(self, piece, newPosition):
    oldPosition = piece.position
    target = self.board.getPiece(newPosition)

    piece.position = newPosition
    if target:
        self.board.pieces.remove(target)

    return oldPosition, target


# =========================
# ANNULER UN COUP
# =========================
def undoMove(self, piece, oldPosition, target):
    piece.position = oldPosition
    if target:
        self.board.pieces.append(target)


# =========================
# VERIFIER SI COUP AUTORISE
# =========================
def isMoveSafe(self, piece, newPosition):
    oldPosition, target = self.simulateMove(piece, newPosition)

    check = self.isCheck(piece.color)

    self.undoMove(piece, oldPosition, target)

    return not check


# =========================
# DETECTION ECHEC ET MAT
# =========================
def isCheckMate(self, color):
    if not self.isCheck(color):
        return False

    for piece in self.board.pieces:
        if piece.color == color:
            for x in range(8):
                for y in range(8):
                    newPos = Position(x, y)
                    if piece.isValidMove(newPos, self.board):
                        if self.isMoveSafe(piece, newPos):
                            return False
    return True