from typing import List, Union

from dofbot.dofcalculator.dofconstants import DofConstants
from dofbot.dofcalculator.dofresult import DofResult
from dofbot.htmlbuilder.htmlbuilder import HtmlBuilder
from dofbot.htmlbuilder.elements import Header, Hr, Paragraph, Table, Td, Th, Tr


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

        op_code = f'{int(self._fnumber is not None)}{int(self._focus_distance is not None)}'
        {
            '00': self._format_by_focal_length,
            '01': self._format_by_focal_length_and_focus_distance,
            '10': self._format_by_focal_length_and_fnumber,
            '11': self._format_by_all
        }[op_code](bldr)

        return bldr.build()

    def _format_by_focal_length(self, bldr: HtmlBuilder) -> None:
        table = Table()
        self._add_common_header(table, len(DofConstants.FOCUS_DISTANCE_LIST))

        focus_distance_vals = Tr()
        for fd in DofConstants.FOCUS_DISTANCE_LIST:
            focus_distance_vals.add_element(Th(str(fd)))
        table.add_thead_element(focus_distance_vals)

        for i, fn in enumerate(DofConstants.FNUMBER_LIST):
            row = Tr()
            row.add_element(Th(str(fn)))

            slice_start = i * len(DofConstants.FOCUS_DISTANCE_LIST)
            slice_end = slice_start + len(DofConstants.FOCUS_DISTANCE_LIST)
            for v in self._dof_result[slice_start:slice_end]:
                row.add_element(Td(f'[{v.dof_near},{v.dof_far},{v.dof_depth}]'))

            table.add_tbody_element(row)

        bldr.add_element(table)

    def _format_by_focal_length_and_focus_distance(self, bldr: HtmlBuilder) -> None:
        table = Table()
        self._add_common_header(table)
        table.add_thead_element(Tr([Th(str(self._focus_distance))]))

        for i, fn in enumerate(DofConstants.FNUMBER_LIST):
            row = Tr()
            row.add_element(Th(str(fn)))

            v = self._dof_result[i]
            row.add_element(Td(f'[{v.dof_near},{v.dof_far},{v.dof_depth}]'))

            table.add_tbody_element(row)

        bldr.add_element(table)

    def _format_by_focal_length_and_fnumber(self, bldr: HtmlBuilder) -> None:
        table = Table()
        self._add_common_header(table, len(DofConstants.FOCUS_DISTANCE_LIST))

        focus_distance_vals = Tr()
        for fd in DofConstants.FOCUS_DISTANCE_LIST:
            focus_distance_vals.add_element(Th(str(fd)))
        table.add_thead_element(focus_distance_vals)

        row = Tr()
        row.add_element(Th(str(self._fnumber)))

        for v in self._dof_result:
            row.add_element(Td(f'[{v.dof_near},{v.dof_far},{v.dof_depth}]'))

        table.add_tbody_element(row)

        bldr.add_element(table)

    def _format_by_all(self, bldr: HtmlBuilder) -> None:
        table = Table()
        self._add_common_header(table)
        table.add_thead_element(Tr([Th(str(self._focus_distance))]))

        row = Tr()
        row.add_element(Th(str(self._fnumber)))

        v = self._dof_result[0]
        row.add_element(Td(f'[{v.dof_near},{v.dof_far},{v.dof_depth}]'))

        table.add_tbody_element(row)

        bldr.add_element(table)

    @staticmethod
    def _add_common_header(table: Table, focus_distance_colspan: int = 0) -> None:
        header = Tr()
        header.add_element(Th("F-number", rowspan=2))
        header.add_element(Th('Focus distance, m', colspan=focus_distance_colspan))
        table.add_thead_element(header)
