import player

class Gameboard:
    '''
    A class that represents the game board.
    '''

    def __init__(self):
        '''
        Initializes a new Tic-Tac-Toe game board.
        '''
        self.__board = ['', '', '',
                        '', '', '',
                        '', '', '']
        self.__round = 1

    def mark_gameboard(self, player: player.Player, position: int) -> None:
        '''
        Marks the gameboard on behalf of one player.

        :param player: A Player object representing the player making the move.
        :param position: An integer representing the position on the board where the player is making the move.
        :return: None
        '''
        if (player.get_character() == 'x' and self.__board[position] == ''):
            self.__board[position] = 'x'
        elif (player.get_character() == 'o' and self.__board[position] == ''):
            self.__board[position] = 'o'

    def next_round(self) -> None:
        '''
        Increments the round counter and clears the game board.
        '''
        self.__round += 1
        self.clear_board()

    def get_round(self) -> int:
        '''
        Returns the current round number.
        '''
        return self.__round

    def clear_board(self) -> None:
        '''
        Clears the Tic-Tac-Toe game board.
        '''
        self.__board = ['', '', '',
                        '', '', '',
                        '', '', '']

    def get_board_state(self) -> list:
        '''
        Returns a list representing the current state of the game.
        '''
        return self.__board

    def get_board_position(self, position: int) -> str:
        '''
        Returns the character ('x', 'o', or '') at the specified position on the Tic-Tac-Toe game board.

        :param position: An integer representing the position on the board to get the character from.
        :return: A string representing the character at the specified position on the board.
        '''
        return self.__board[position]

    def check_victory(self) -> str:
        '''
        Checks if either player has won the game or if the game has ended in a tie.

        :return: Returns "X" if player X has won, "O" if player O has won, "TIE" if the game has ended in a tie, or "NO VICTORY" if the game is not yet over.
        '''
        # Check rows
        for i in range(0, 9, 3):
            if self.__board[i] == self.__board[i+1] == self.__board[i+2] and self.__board[i] != '':
                return self.__board[i]

        # Check columns
        for i in range(3):
            if self.__board[i] == self.__board[i+3] == self.__board[i+6] and self.__board[i] != '':
                return self.__board[i]

        # Check diagonals
        if self.__board[0] == self.__board[4] == self.__board[8] and self.__board[0] != '':
            return self.__board[0]
        if self.__board[2] == self.__board[4] == self.__board[6] and self.__board[2] != '':
            return self.__board[2]

        # Check for tie
        if '' not in self.__board:
            return 'TIE'

        # Game not over yet
        return 'NO VICTORY'
