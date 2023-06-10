import numpy as np

class Load:
    def __init__(self, magnitude: float, angle: float):
        self.magnitude = magnitude
        self.angle = angle

    def get_cartesian(self) -> tuple[float, float]:
        x = self.magnitude * np.cos(self.angle)
        y = self.magnitude * np.sin(self.angle)

        return (x, y)
