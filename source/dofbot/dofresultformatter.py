from typing import List, Union

from dofbot.dofcalculator.dofresult import DofResult
from dofbot.htmlbuilder.htmlbuilder import HtmlBuilder
from dofbot.htmlbuilder.elements import Header, Hr, Paragraph


class DofResultFormatter:
    def __init__(self, focal_length: int, fnumber: Union[float, None], focus_distance: Union[float, None],
                 dof_result: List[DofResult]):
        self._focal_length = focal_length
        self._fnumber = fnumber
        self._focus_distance = focus_distance
        self._dof_result = dof_result

    def format(self) -> str:
        bldr = HtmlBuilder()
        bldr.add_element(Header('Depth Of Field Calculation', 1))
        bldr.add_element(Header(f'Focal length = {self._focal_length}'))
        bldr.add_element(Header(f'F-number = {self._fnumber}'))
        bldr.add_element(Header(f'Focus distance = {self._focus_distance}'))
        bldr.add_element(Hr())
        bldr.add_element(Header('Results', 1))
        for i in self._dof_result:
            bldr.add_element(Paragraph(str(i)))
        return bldr.build()
