from typing import Tuple, Union

from dofbot.dofcalculator.exceptions import DofCalculatorInvalidQuery


class DofQueryParser:
    @classmethod
    def parse_query(cls, query: str) -> Tuple[int, Union[float, None], Union[float, None]]:
        parts = query.split(',')
        if len(parts) > 3:
            raise DofCalculatorInvalidQuery()

        return 1, 2, 3

    @classmethod
    def _parse_focal_length(cls, query: str) -> int:
        pass

    @classmethod
    def _parse_aperture(cls, query: str) -> Union[float, None]:
        pass

    @classmethod
    def _parse_focus_distance(cls, query: str) -> Union[float, None]:
        pass
