class character2:
    def __init__(self, value):
        self.__value = value
    
    @property
    def value(self):
        return self.__value.count('s')