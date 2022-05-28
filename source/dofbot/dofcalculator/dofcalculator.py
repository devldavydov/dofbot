from typing import Union


class DofCalculator:
    FOCUS_DISTANCE_LIST = [0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
    APERTURE_LIST = [1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.5, 2.8, 3.2, 3.5, 4, 4.5, 5, 5.6, 6.3, 7.1, 8, 9, 10, 11, 13, 14, 16,
                     18, 20, 22]
    CIRCLE_OF_CONFUSION = 0.03

    def __init__(self, focal_length: int, aperture: float = None, focus_distance: float = None):
        self._focal_length = focal_length
        self._aperture = aperture
        self._focus_distance = focus_distance

    @classmethod
    def from_query(cls, query: str) -> 'DofCalculator':
        return cls(1, 2, 3)

    @property
    def focal_length(self) -> int:
        return self._focal_length

    @property
    def aperture(self) -> Union[float, None]:
        return self._aperture

    @property
    def focus_distance(self) -> Union[float, None]:
        return self._focus_distance
