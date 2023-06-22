from Load import Load
from Support import Support

class Joint:
    
    _instance_count = 0

    @classmethod
    def _increment_instance_count(cls):
        cls._instance_count += 1

    def __init__(self, x: float, y: float):
        self._increment_instance_count()
        self.id = self._instance_count
        self.label = chr(ord('@') + self.id)
        self.x = x
        self.y = y
        self.loads = list()
        self.support = None 

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.label

    def add_load(self, load: Load) -> None:
        if load not in self.loads:
            self.loads.append(load)

    def set_support(self, support: Support) -> None:
        if(self.support != support):
            self.support = support

    def get_total_load(self) -> tuple[float, float]:
        total_x, total_y = (0, 0)
        for load in self.loads:
            total_x += load.get_cartesian()[0]
            total_y += load.get_cartesian()[1]

        return (total_x, total_y)
