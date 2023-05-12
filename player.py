class Player:
    '''
    A class to create player objects
    '''
    def __init__(self, name: str, character: str) -> None:
        '''
        Initializes a player object with a given name and character (either 'X' or 'O')
        :param name: The name of the player
        :param character: The character representing the player on the board
        '''
        self.__name = name
        self.__character = character
        self.__points = 0

    def get_name(self) -> str:
        '''
        Returns the name of the player
        '''
        return self.__name

    def get_character(self) -> str:
        '''
        Returns the character representing the player on the board ('X' or 'O')
        '''
        return self.__character

    def increase_points(self) -> None:
        '''
        Increments the number of points a player has by 1
        '''
        self.__points += 1

    def get_points(self) -> int:
        '''
        Returns the number of points a player has earned
        '''
        return self.__points
