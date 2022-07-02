from typing import List, Union

from dofbot.htmlbuilder.elements.htmlelement import HtmlElement


class Tr(HtmlElement):
    def __init__(self, elements: Union[None, List[HtmlElement]] = None):
        self._elements = [] if not elements else elements

    def add_element(self, html_element: HtmlElement) -> None:
        self._elements.append(html_element)

    def build(self) -> str:
        return f"<tr>{''.join(el.build() for el in self._elements)}</tr>"
