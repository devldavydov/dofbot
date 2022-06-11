from dataclasses import dataclass


@dataclass
class DofResult:
    focal_length: int
    fnumber: float
    focus_distance: float
    dof_near: float
    dof_far: float
    dof_depth: float

    def __str__(self) -> str:
        return f'FL={self.focal_length} FN={self.fnumber} FD={self.focus_distance} '\
               f'[{self.dof_near}, {self.dof_far}, {self.dof_depth}]'
