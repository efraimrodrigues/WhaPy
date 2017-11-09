from enum import Enum

class Browser(Enum):
    default             = 3
    chrome              = 1
    edge                = 2
    firefox             = 3
    safari              = 4
    

    def __str__(self):
        return self.name