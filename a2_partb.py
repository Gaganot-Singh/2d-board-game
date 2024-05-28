
from a1_partc import Queue
from a1_partd import get_overflow_list, overflow

import random

# This function duplicates and returns the board. You may find this useful
def copy_board(board):
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board


# this function is your evaluation function for the board
def evaluate_board(board, player):
    opponentNumOfGems = 0
    playerNumOfGems = 0
    EmptyCells = 0

    for row in board:
        for cell in row:
            if cell == player:
                playerNumOfGems += 1
            elif cell == -player:
                opponentNumOfGems += 1
            else:
                EmptyCells += 1

    if opponentNumOfGems == 0 and playerNumOfGems > 0:
        return 10000
    elif playerNumOfGems == 0 and opponentNumOfGems > 0:
        return -10000

    score = 100 * playerNumOfGems - 100 * opponentNumOfGems - EmptyCells
    return score

class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height=4):
            self.player = player
            self.board = copy_board(board)
             #you will need to implement the creation of the game tree here.  After this function completes,
            # a full game tree will be created.
            # hint: as with many tree structures, you will need to define a self.root that points to the root
            # of the game tree.  To create the tree itself, a recursive function will likely be the easiest as you will
            # need to apply the minimax algorithm to its creation.

            self.depth = depth
            self.position = None
            self.player = player
            self.tree_height = tree_height
            self.children = []
            self.score = None

        def is_game_over(self):
            playerOneCount = sum(cell > 0 for row in self.board for cell in row)
            playerTwoCount = sum(cell < 0 for row in self.board for cell in row)
            return playerOneCount == 0 or playerTwoCount == 0

    def __init__(self, board, player, tree_height=4):
        self.player = player
        self.board = copy_board(board)
        self.aiBestMove = None
        self.tree_height = tree_height
        self.root = self.Node(
            self.board, 0, self.player, self.tree_height
        )
        self.build_tree(self.root, 0)

    def build_tree(self, node, current_depth):
        if current_depth == 0:
            depthPlayer = node.player
        else:
            depthPlayer = node.player * -1

        newDepth = current_depth + 1

        if current_depth >= self.tree_height:
            node.score = evaluate_board(node.board, self.player) * depthPlayer
            return

        indices = [(i, j) for i in range(len(node.board)) for j in range(len(node.board[i]))]
        random.shuffle(indices)

        for i, j in indices:
            cell = node.board[i][j]
            depthPlayer = node.player if current_depth == 0 else node.player * -1

            if cell == 0 or (cell > 0 and depthPlayer > 0) or (cell < 0 and depthPlayer < 0):
                newBoard = copy_board(node.board)
                newBoard[i][j] = newBoard[i][j] + depthPlayer

                is_overflow_possible = get_overflow_list(newBoard)
                if is_overflow_possible:
                    overflow_result = Queue()
                    overflow(newBoard, overflow_result)
                    while not overflow_result.is_empty():
                        newBoard = overflow_result.dequeue()

                newNode = self.Node(
                    newBoard, newDepth, depthPlayer, node.tree_height - 1
                )
                newNode.score = evaluate_board(newBoard, self.player)
                newNode.position = (i, j)
                node.children.append(newNode)
                if newDepth < self.tree_height - 1:
                    self.build_tree(newNode, newDepth)

    def minimax(self, node, depth, is_maximizing_player):
        if node.is_game_over():
            return node

        possible_moves = node.children
        if is_maximizing_player:
            bestMove = max(possible_moves, key=lambda node: node.score)
        else:
            bestMove = min(possible_moves, key=lambda node: node.score)
        self.aiBestMove = bestMove.position
        return bestMove

    def get_move(self):
        self.minimax(self.root, 0, True)
        return self.aiBestMove

    def clear_tree(self, node=None):
        if node is None:
            node = self.root
        if node.children == []:
            return
        for child in node.children:
            self.clear_tree(child)
        node.children = []
