from dofbot.htmlbuilder.elements.htmlelement import HtmlElement


class Th(HtmlElement):
    def __init__(self, value: str, rowspan: int = 0, colspan: int = 0):
        self._value = value
        self._rowspan = rowspan
        self._colspan = colspan

    def build(self) -> str:
        return f'<th rowspan="{self._rowspan}" colspan="{self._colspan}">{self._value}</th>'
