from player import Player
from gameboard import Gameboard
from main import Ui_MainWindow



def start(objectsExist: bool, window: Ui_MainWindow, Gb, p1, p2) -> None:
    '''
    Function called when start button is pressed
    :param window: MainWindow object
    :return: None
    '''

    #initialize players and gameboard
    if (objectsExist == False):
        Gb = Gameboard()
        p1 = Player(window.P1Textbox.text(), 'X')
        p2 = Player(window.P2Textbox.text(), 'O')

    #set Textboxes to be read only
    window.P1Textbox.setReadOnly(True)
    window.P2Textbox.setReadOnly(True)

    #change start button into reset button
    window.SRButton.setText('Reset')
    window.SRButton.clicked.connect(lambda:reset(Gb, window, p1, p2))

    #initialize gameboard buttons
    window.B0Button.clicked.connect(lambda:mark_board(Gb, p1, window, 0, p2, 9))
    window.B1Button.clicked.connect(lambda:mark_board(Gb, p1, window, 1, p2, 9))
    window.B2Button.clicked.connect(lambda:mark_board(Gb, p1, window, 2, p2, 9))
    window.B3Button.clicked.connect(lambda:mark_board(Gb, p1, window, 3, p2, 9))
    window.B4Button.clicked.connect(lambda:mark_board(Gb, p1, window, 4, p2, 9))
    window.B5Button.clicked.connect(lambda:mark_board(Gb, p1, window, 5, p2, 9))
    window.B6Button.clicked.connect(lambda:mark_board(Gb, p1, window, 6, p2, 9))
    window.B7Button.clicked.connect(lambda:mark_board(Gb, p1, window, 7, p2, 9))
    window.B8Button.clicked.connect(lambda:mark_board(Gb, p1, window, 8, p2, 9))
    pass

def reset(board: Gameboard, window: Ui_MainWindow, player1, player2) -> None:
    '''
    Function called when the reset button is pressed
    :param board: Gameboard object
    :param window: MainWindow object
    :param player1: Player 1 object
    :param player2: PLayer 2 object
    :return: None
    '''

    #destroy player and gameboard objects

    #reset player textboxes and gameboard buttons

    window.P1Textbox.setText('')
    window.P2Textbox.setText('')
    window.P1Textbox.setReadOnly(False)
    window.P2Textbox.setReadOnly(False)
    window.B0Button.setText('')
    window.B0Button.setEnabled(True)
    window.B1Button.setText('')
    window.B1Button.setEnabled(True)
    window.B2Button.setText('')
    window.B2Button.setEnabled(True)
    window.B3Button.setText('')
    window.B3Button.setEnabled(True)
    window.B4Button.setText('')
    window.B4Button.setEnabled(True)
    window.B5Button.setText('')
    window.B5Button.setEnabled(True)
    window.B6Button.setText('')
    window.B6Button.setEnabled(True)
    window.B7Button.setText('')
    window.B7Button.setEnabled(True)
    window.B8Button.setText('')
    window.B8Button.setEnabled(True)

    #change reset button into start button
    window.SRButton.setText('Start')
    window.SRButton.clicked.connect(lambda:start(True, window, board, player1, player2))

    #reset round counter
    window.RoundNum.setText('Round: 1')


    pass

def mark_board(Gb: Gameboard, player: Player, window: Ui_MainWindow, pos: int, altplayer: Player, spaces_open: int) -> None:
    '''
    Function called when any of the buttons constituting the board are pressed
    :param Gb: Gameboard object
    :param player: Player whose turn it is
    :param window: MainWindow object
    :param pos: number representing which position on the board was clicked
    :param altplayer: other player
    :param spaces_open: spaces not marked
    :
    :return: None
    '''
    #mark board
    round_incomplete = True
    if (pos == 0):
        window.B0Button.setText(player.get_character())
        window.B0Button.setEnabled(False)
        Gb.mark_gameboard(0, player)
        spaces_open = spaces_open - 1
        print(f'{pos} spot clicked;{spaces_open} spaces remaining')
    if (pos == 1):
        window.B1Button.setText(player.get_character())
        window.B1Button.setEnabled(False)
        Gb.mark_gameboard(1, player)
        spaces_open = spaces_open - 1
        print(f'{pos} spot clicked;{spaces_open} spaces remaining')
    if (pos == 2):
        window.B2Button.setText(player.get_character())
        window.B2Button.setEnabled(False)
        Gb.mark_gameboard(2, player)
        spaces_open = spaces_open - 1
        print(f'{pos} spot clicked;{spaces_open} spaces remaining')
    if (pos == 3):
        window.B3Button.setText(player.get_character())
        window.B3Button.setEnabled(False)
        Gb.mark_gameboard(3, player)
        spaces_open = spaces_open - 1
        print(f'{pos} spot clicked;{spaces_open} spaces remaining')
    if (pos == 4):
        window.B4Button.setText(player.get_character())
        window.B4Button.setEnabled(False)
        Gb.mark_gameboard(4, player)
        spaces_open = spaces_open - 1
        print(f'{pos} spot clicked;{spaces_open} spaces remaining')
    if (pos == 5):
        window.B5Button.setText(player.get_character())
        window.B5Button.setEnabled(False)
        Gb.mark_gameboard(5, player)
        spaces_open = spaces_open - 1
        print(f'{pos} spot clicked;{spaces_open} spaces remaining')
    if (pos == 6):
        window.B6Button.setText(player.get_character())
        window.B6Button.setEnabled(False)
        Gb.mark_gameboard(6, player)
        spaces_open = spaces_open - 1
        print(f'{pos} spot clicked;{spaces_open} spaces remaining')
    if (pos == 7):
        window.B7Button.setText(player.get_character())
        window.B7Button.setEnabled(False)
        Gb.mark_gameboard(7, player)
        spaces_open = spaces_open - 1
        print(f'{pos} spot clicked;{spaces_open} spaces remaining')
    if (pos == 8):
        window.B8Button.setText(player.get_character())
        window.B8Button.setEnabled(False)
        Gb.mark_gameboard(8, player)
        spaces_open = spaces_open - 1
        print(f'{pos} spot clicked;{spaces_open} spaces remaining')

    #check for victory or tie
    if (Gb.check_victory() == 'X'):
        enable_buttons(window)
        clear_buttons(window)
        round_incomplete = True
        #spaces_open = 9
    elif (Gb.check_victory() == 'O'):
        enable_buttons(window)
        clear_buttons(window)
        round_incomplete = False
        #spaces_open = 9
    elif (spaces_open == 0):
        enable_buttons(window)
        clear_buttons(window)
        round_incomplete = True
        #spaces_open = 9
    else:
        pass

    #switch players
    if (round_incomplete == True):
        window.B0Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 0, player, spaces_open))
        window.B1Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 1, player, spaces_open))
        window.B2Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 2, player, spaces_open))
        window.B3Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 3, player, spaces_open))
        window.B4Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 4, player, spaces_open))
        window.B5Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 5, player, spaces_open))
        window.B6Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 6, player, spaces_open))
        window.B7Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 7, player, spaces_open))
        window.B8Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 8, player, spaces_open))
    else:
        if (player == 'X'):
            window.B0Button.clicked.connect(lambda: mark_board(Gb, player, window, 0, altplayer, 9))
            window.B1Button.clicked.connect(lambda: mark_board(Gb, player, window, 1, altplayer, 9))
            window.B2Button.clicked.connect(lambda: mark_board(Gb, player, window, 2, altplayer, 9))
            window.B3Button.clicked.connect(lambda: mark_board(Gb, player, window, 3, altplayer, 9))
            window.B4Button.clicked.connect(lambda: mark_board(Gb, player, window, 4, altplayer, 9))
            window.B5Button.clicked.connect(lambda: mark_board(Gb, player, window, 5, altplayer, 9))
            window.B6Button.clicked.connect(lambda: mark_board(Gb, player, window, 6, altplayer, 9))
            window.B7Button.clicked.connect(lambda: mark_board(Gb, player, window, 7, altplayer, 9))
            window.B8Button.clicked.connect(lambda: mark_board(Gb, player, window, 8, altplayer, 9))
        else:
            window.B0Button.clicked.connect(lambda: mark_board(Gb, altplayer, window, 0, player, 9))
            window.B1Button.clicked.connect(lambda: mark_board(Gb, altplayer, window, 1, player, 9))
            window.B2Button.clicked.connect(lambda: mark_board(Gb, altplayer, window, 2, player, 9))
            window.B3Button.clicked.connect(lambda: mark_board(Gb, altplayer, window, 3, player, 9))
            window.B4Button.clicked.connect(lambda: mark_board(Gb, altplayer, window, 4, player, 9))
            window.B5Button.clicked.connect(lambda: mark_board(Gb, altplayer, window, 5, player, 9))
            window.B6Button.clicked.connect(lambda: mark_board(Gb, altplayer, window, 6, player, 9))
            window.B7Button.clicked.connect(lambda: mark_board(Gb, altplayer, window, 7, player, 9))
            window.B8Button.clicked.connect(lambda: mark_board(Gb, altplayer, window, 8, player, 9))

def enable_buttons(window):
    window.B0Button.setEnabled(True)
    window.B1Button.setEnabled(True)
    window.B2Button.setEnabled(True)
    window.B3Button.setEnabled(True)
    window.B4Button.setEnabled(True)
    window.B5Button.setEnabled(True)
    window.B6Button.setEnabled(True)
    window.B7Button.setEnabled(True)
    window.B8Button.setEnabled(True)
def disable_buttons(window):
    window.B0Button.setEnabled(False)
    window.B1Button.setEnabled(False)
    window.B2Button.setEnabled(False)
    window.B3Button.setEnabled(False)
    window.B4Button.setEnabled(False)
    window.B5Button.setEnabled(False)
    window.B6Button.setEnabled(False)
    window.B7Button.setEnabled(False)
    window.B8Button.setEnabled(False)
def clear_buttons(window):
    window.B0Button.setText('')
    window.B1Button.setText('')
    window.B2Button.setText('')
    window.B3Button.setText('')
    window.B4Button.setText('')
    window.B5Button.setText('')
    window.B6Button.setText('')
    window.B7Button.setText('')
    window.B8Button.setText('')