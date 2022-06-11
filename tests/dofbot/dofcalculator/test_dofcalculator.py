from math import inf

import pytest

from dofbot.dofcalculator.dofcalculator import DofCalculator
from dofbot.dofcalculator.dofconstants import DofConstants
from dofbot.dofcalculator.dofresult import DofResult


def test_calc_by_focal_length():
    result = DofCalculator(24, None, None).calc()
    assert len(DofConstants.APERTURE_LIST) * len(DofConstants.FOCUS_DISTANCE_LIST) == len(result)
    assert DofResult(focal_length=24,
                     aperture=1.2,
                     focus_distance=0.5,
                     dof_near=0.49,
                     dof_far=0.52,
                     dof_depth=0.03) == result[0]
    assert DofResult(focal_length=24,
                     aperture=22,
                     focus_distance=30,
                     dof_near=0.85,
                     dof_far=inf,
                     dof_depth=inf) == result[-1]


def test_calc_by_focal_length_and_focus_distance():
    result = DofCalculator(24, None, 5).calc()
    assert len(DofConstants.APERTURE_LIST) == len(result)
    assert DofResult(focal_length=24,
                     aperture=1.2,
                     focus_distance=5,
                     dof_near=3.81,
                     dof_far=7.26,
                     dof_depth=3.45) == result[0]
    assert DofResult(focal_length=24,
                     aperture=22,
                     focus_distance=5,
                     dof_near=0.75,
                     dof_far=inf,
                     dof_depth=inf) == result[-1]


def test_calc_by_focal_length_and_aperture():
    result = DofCalculator(24, 2.8, None).calc()
    assert len(DofConstants.FOCUS_DISTANCE_LIST) == len(result)
    assert DofResult(focal_length=24,
                     aperture=2.8,
                     focus_distance=0.5,
                     dof_near=0.47,
                     dof_far=0.54,
                     dof_depth=0.07) == result[0]
    assert DofResult(focal_length=24,
                     aperture=2.8,
                     focus_distance=30,
                     dof_near=5.59,
                     dof_far=inf,
                     dof_depth=inf) == result[-1]


@pytest.mark.parametrize(
    'focal_length,aperture,focus_distance,dof_near,dof_far,dof_depth',
    (
        (24, 1.2, 0.5, 0.49, 0.52, 0.03),
        (24, 1.2, 30, 10.44, inf, inf),
        (24, 3.2, 6, 3.01, 1500.00, 1496.99),
        (24, 22, 0.5, 0.32, 1.10, 0.78),
        (24, 22, 30, 0.85, inf, inf),
        #
        (50, 1.2, 0.5, 0.50, 0.50, 0.0),
        (50, 1.2, 30, 20.96, 52.75, 31.79),
        (50, 14, 6, 3.00, 15000.00, 14997.00),
        (50, 22, 0.5, 0.45, 0.57, 0.12),
        (50, 22, 30, 3.37, inf, inf),
        #
        (135, 1.2, 0.5, 0.50, 0.50, 0.0),
        (135, 1.2, 30, 28.33, 31.88, 3.55),
        (135, 22, 25, 13.15, 251.16, 238.01),
        (135, 22, 0.5, 0.49, 0.51, 0.02),
        (135, 22, 30, 14.41, inf, inf)
    )
)
def test_calc_by_all(focal_length, aperture, focus_distance, dof_near, dof_far, dof_depth):
    assert [DofResult(focal_length=focal_length,
                      aperture=aperture,
                      focus_distance=focus_distance,
                      dof_near=dof_near,
                      dof_far=dof_far,
                      dof_depth=dof_depth)] == DofCalculator(focal_length, aperture, focus_distance).calc()
