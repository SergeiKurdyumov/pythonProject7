class Road:
    _surface_spec_gravity: float = 0.05

    def __init__(self, length: [int, float], width: [int, float]):
        self._length = float(length)
        self._width = float(width)

    def get_surface_gravity(self, thickness: float) -> [float,None]:
        try:
            return(self._length * self._width * thickness * self._surface_spec_gravity)

        except TypeError:
            return None

if __name__ == '__main__':
    try:
        road = Road(5000,25)
        print ('масса равна', road.get_surface_gravity(20))

    except TypeError:
        print('Требуется две позиции')