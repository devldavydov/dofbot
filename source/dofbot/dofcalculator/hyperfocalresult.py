from dataclasses import dataclass


@dataclass
class HyperFocalResult:
    focal_length: int
    fnumber: float
    hyperfocal: float

    def __str__(self) -> str:
        return f'HyperFocal(FL={self.focal_length} FN={self.fnumber}) [{self.hyperfocal}]'
