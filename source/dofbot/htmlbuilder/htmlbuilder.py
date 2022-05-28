from dofbot.htmlbuilder.elements.htmlelement import HtmlElement


class HtmlBuilder(HtmlElement):
    def __init__(self):
        self._elements = []

    def add_element(self, html_element: HtmlElement):
        self._elements.append(html_element)

    def build(self) -> str:
        return f"<html><body>{''.join(el.build() for el in self._elements)}</body></html>"
