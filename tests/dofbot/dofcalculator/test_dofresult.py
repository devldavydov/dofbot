from math import inf

import pytest

from dofbot.dofcalculator.dofresult import DofResult


@pytest.mark.parametrize(
    'vals,str_val',
    (
        (dict(focal_length=24, fnumber=5.6, focus_distance=20, dof_near=1.2, dof_far=inf, dof_depth=inf),
         'DoF(FL=24 FN=5.6 FD=20) [1.2, inf, inf]'),
        (dict(focal_length=50, fnumber=2.8, focus_distance=5, dof_near=1.2, dof_far=2.0, dof_depth=0.8),
         'DoF(FL=50 FN=2.8 FD=5) [1.2, 2.0, 0.8]'),
    )
)
def test_dofresult_str(vals, str_val):
    assert str_val == str(DofResult(**vals))
