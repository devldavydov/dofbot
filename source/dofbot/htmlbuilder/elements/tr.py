from dofbot.htmlbuilder.elements.htmlelement import HtmlElement


class Tr(HtmlElement):
    def __init__(self):
        self._elements = []

    def add_element(self, html_element: HtmlElement) -> None:
        self._elements.append(html_element)

    def build(self) -> str:
        return f"<tr>{''.join(el.build() for el in self._elements)}</tr>"
