from dofbot.dofcalculator.dofcalculator import DofCalculator
from dofbot.dofresultformatter import DofResultFormatter


class DofQueryProcessor:
    def __init__(self, query: str):
        self._query = query

    def process(self) -> str:
        dof_calc = DofCalculator.from_query(self._query)
        hyperfocal_result = dof_calc.calc_hyperfocal() if dof_calc.fnumber else None
        dof_formatter = DofResultFormatter(dof_calc.focal_length, dof_calc.fnumber, dof_calc.focus_distance,
                                           dof_calc.calc(), hyperfocal_result)
        return dof_formatter.format()
