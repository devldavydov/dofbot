from dofbot.htmlbuilder.elements.htmlelement import HtmlElement


class Table(HtmlElement):
    def __init__(self):
        self._thead_elements = []
        self._tbody_elements = []

    def add_thead_element(self, html_element: HtmlElement) -> None:
        self._thead_elements.append(html_element)

    def add_tbody_element(self, html_element: HtmlElement) -> None:
        self._tbody_elements.append(html_element)

    def build(self) -> str:
        return f"""<table border="1"><thead>{''.join(el.build() for el in self._thead_elements)}</thead>""" \
               f"<tbody>{''.join(el.build() for el in self._tbody_elements)}</tbody></table>"
