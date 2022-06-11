from dofbot.htmlbuilder.elements.htmlelement import HtmlElement


class Paragraph(HtmlElement):
    def __init__(self, text: str):
        self._text = text

    def build(self) -> str:
        return f'<p>{self._text}</p>'
