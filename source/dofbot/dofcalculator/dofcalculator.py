from typing import Union


class DofCalculator:
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
