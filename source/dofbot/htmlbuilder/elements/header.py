from dofbot.htmlbuilder.elements.htmlelement import HtmlElement


class Header(HtmlElement):
    def __init__(self, text: str, size: int = 3):
        self._text = text
        self._size = size if size in range(1, 7) else 3

    def build(self) -> str:
        return f'<h{self._size}>{self._text}</h{self._size}>'
