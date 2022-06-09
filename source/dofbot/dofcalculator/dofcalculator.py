from math import inf
from typing import List

from dofbot.dofcalculator.dofconstants import DofConstants
from dofbot.dofcalculator.dofqueryparser import DofQueryParser
from dofbot.dofcalculator.dofresult import DofResult


class DofCalculator:
    def __init__(self, focal_length: int, aperture: float = None, focus_distance: float = None):
        self._focal_length = focal_length
        self._aperture = aperture
        self._focus_distance = focus_distance

    @classmethod
    def from_query(cls, query: str) -> 'DofCalculator':
        return cls(*DofQueryParser.parse_query(query))

    @property
    def focal_length(self) -> int:
        return self._focal_length

    @property
    def aperture(self) -> float | None:
        return self._aperture

    @property
    def focus_distance(self) -> float | None:
        return self._focus_distance

    def calc(self) -> List[DofResult]:
        op_code = f'{int(self._aperture is not None)}{int(self._focus_distance is not None)}'
        return {
            '00': self._calc_by_focal_length,
            '01': self._calc_by_focal_length_and_focus_distance,
            '10': self._calc_by_focal_length_and_aperture,
            '11': self._calc_by_all
        }[op_code]()

    def _calc_by_focal_length(self) -> List[DofResult]:
        raise NotImplementedError()

    def _calc_by_focal_length_and_focus_distance(self) -> List[DofResult]:
        raise NotImplementedError()

    def _calc_by_focal_length_and_aperture(self) -> List[DofResult]:
        raise NotImplementedError()

    def _calc_by_all(self) -> List[DofResult]:
        return [self._calc_dof(self._focal_length, self._aperture, self._focus_distance)]

    @staticmethod
    def _calc_dof(focal_length: int, aperture: float, focus_distance: float) -> DofResult:
        f = focal_length * 0.001
        f2 = f ** 2
        r = focus_distance
        k = aperture
        z = DofConstants.CIRCLE_OF_CONFUSION * 0.001

        rf2 = r * f2
        kfz = k * f * z
        krz = k * r * z

        r1 = round(rf2 / (f2 - kfz + krz), 2)
        r2 = rf2 / (f2 + kfz - krz)
        r2 = inf if r2 < 0 else round(r2, 2)

        return DofResult(focal_length=focal_length, aperture=aperture, focus_distance=focus_distance,
                         dof_near=r1, dof_far=r2, dof_depth=inf if r2 == inf else round(r2 - r1, 2))
