from typing import Tuple, Type, Union

from dofbot.dofcalculator.exceptions import DofCalculatorInvalidQuery
from dofbot.dofcalculator.dofconstants import DofConstants


class DofQueryParser:
    @classmethod
    def parse_query(cls, query: str) -> Tuple[int, Union[float, None], Union[float, None]]:
        parts = [s.strip() for s in query.split(',')]
        if len(parts) > 3:
            raise DofCalculatorInvalidQuery()

        focal_length = cls._parse_focal_length(parts[0])
        aperture, focus_distance = None, None

        if len(parts) == 2:
            try:
                aperture = cls._parse_aperture(parts[1])
            except DofCalculatorInvalidQuery:
                focus_distance = cls._parse_focus_distance(parts[1])
        elif len(parts) == 3:
            aperture = cls._parse_aperture(parts[1])
            focus_distance = cls._parse_focus_distance(parts[2])

        return focal_length, aperture, focus_distance

    @classmethod
    def _parse_focal_length(cls, query: str) -> int:
        if not query.startswith('FL='):
            raise DofCalculatorInvalidQuery()

        return cls._parser_val_to_type(query[3:], int)

    @classmethod
    def _parse_aperture(cls, query: str) -> float:
        if not query.startswith('F='):
            raise DofCalculatorInvalidQuery()

        aperture = cls._parser_val_to_type(query[2:], float)
        if aperture not in DofConstants.APERTURE_LIST:
            raise DofCalculatorInvalidQuery()

        return aperture

    @classmethod
    def _parse_focus_distance(cls, query: str) -> float:
        if not query.startswith('FD='):
            raise DofCalculatorInvalidQuery()

        return cls._parser_val_to_type(query[3:], float)

    @classmethod
    def _parser_val_to_type(cls, val: str, val_type: Type) -> Union[int, float]:
        try:
            result = val_type(val)
        except Exception:
            raise DofCalculatorInvalidQuery()

        if result <= 0:
            raise DofCalculatorInvalidQuery()

        return result
