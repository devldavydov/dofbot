from dofbot.htmlbuilder.elements.htmlelement import HtmlElement


class Td(HtmlElement):
    def __init__(self, value: str):
        self._value = value

    def build(self) -> str:
        return f'<td>{self._value}</td>'
