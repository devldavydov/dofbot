from math import inf

import pytest

from dofbot.dofcalculator.dofcalculator import DofCalculator
from dofbot.dofcalculator.dofresult import DofResult


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
