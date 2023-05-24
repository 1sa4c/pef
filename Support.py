from SupportType import SupportType

class Support():
    def __init__(self, x: float, y: float, support_type: SupportType):
        self.x = x
        self.y = y
        self.support_type = support_type
        print(type(self.support_type))

    def __str__(self):
        return f'<Support>[{self.support_type.name}] ({self.x}, {self.y})'
