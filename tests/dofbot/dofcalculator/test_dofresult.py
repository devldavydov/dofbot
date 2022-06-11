from math import inf

import pytest

from dofbot.dofcalculator.dofresult import DofResult


@pytest.mark.parametrize(
    'vals,str_val',
    (
        (dict(focal_length=24, aperture=5.6, focus_distance=20, dof_near=1.2, dof_far=inf, dof_depth=inf),
         'FL=24 F=5.6 FD=20 [1.2, inf, inf]'),
        (dict(focal_length=50, aperture=2.8, focus_distance=5, dof_near=1.2, dof_far=2.0, dof_depth=0.8),
         'FL=50 F=2.8 FD=5 [1.2, 2.0, 0.8]'),
    )
)
def test_dofresult_str(vals, str_val):
    assert str_val == str(DofResult(**vals))
