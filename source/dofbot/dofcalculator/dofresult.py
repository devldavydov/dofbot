from dataclasses import dataclass


@dataclass
class DofResult:
    focal_length: int
    aperture: float
    focus_distance: float
    dof_near: float
    dof_far: float
    dof_depth: float
