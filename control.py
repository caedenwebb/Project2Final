from player import Player
from gameboard import Gameboard
from main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

def start(window: Ui_MainWindow) -> None:
    '''
    Function called when start button is pressed
    :param window: MainWindow object
    :return: None
    '''

    #initialize players and gameboard
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
    window.B0Button.clicked.connect(lambda:mark_board(Gb, p1, window, 0, p2))
    window.B1Button.clicked.connect(lambda:mark_board(Gb, p1, window, 1, p2))
    window.B2Button.clicked.connect(lambda:mark_board(Gb, p1, window, 2, p2))
    window.B3Button.clicked.connect(lambda:mark_board(Gb, p1, window, 3, p2))
    window.B4Button.clicked.connect(lambda:mark_board(Gb, p1, window, 4, p2))
    window.B5Button.clicked.connect(lambda:mark_board(Gb, p1, window, 5, p2))
    window.B6Button.clicked.connect(lambda:mark_board(Gb, p1, window, 6, p2))
    window.B7Button.clicked.connect(lambda:mark_board(Gb, p1, window, 7, p2))
    window.B8Button.clicked.connect(lambda:mark_board(Gb, p1, window, 8, p2))
    pass

def reset(board: Gameboard, window: Ui_MainWindow, player1, player2) -> None:
    '''
    Function called when the reset button is pressed
    :param window: MainWindow object
    :return: None
    '''

    #destroy player and gameboard objects

    del board
    del player1
    del player2

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
    window.SRButton.clicked.connect(lambda:start(window))


    pass

def mark_board(Gb: Gameboard, player: Player, window: Ui_MainWindow, pos: int, altplayer: Player) -> None:
    '''
    Function called when any of the buttons constituting the board are pressed
    :param window: MainWindow object
    :param pos: number representing which position on the board was clicked
    :return: None
    '''
    #mark board
    if (pos == 0):
        window.B0Button.setText(player.char)
        window.B0Button.setEnabled(False)
    if (pos == 1):
        window.B1Button.setText(player.char)
        window.B1Button.setEnabled(False)
    if (pos == 2):
        window.B2Button.setText(player.char)
        window.B2Button.setEnabled(False)
    if (pos == 3):
        window.B3Button.setText(player.char)
        window.B3Button.setEnabled(False)
    if (pos == 4):
        window.B4Button.setText(player.char)
        window.B4Button.setEnabled(False)
    if (pos == 5):
        window.B5Button.setText(player.char)
        window.B5Button.setEnabled(False)
    if (pos == 6):
        window.B6Button.setText(player.char)
        window.B6Button.setEnabled(False)
    if (pos == 7):
        window.B7Button.setText(player.char)
        window.B7Button.setEnabled(False)
    if (pos == 8):
        window.B8Button.setText(player.char)
        window.B8Button.setEnabled(False)

    #switch players
    window.B0Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 0, player))
    window.B1Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 1, player))
    window.B2Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 2, player))
    window.B3Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 3, player))
    window.B4Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 4, player))
    window.B5Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 5, player))
    window.B6Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 6, player))
    window.B7Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 7, player))
    window.B8Button.clicked.connect(lambda:mark_board(Gb, altplayer, window, 8, player))


    pass