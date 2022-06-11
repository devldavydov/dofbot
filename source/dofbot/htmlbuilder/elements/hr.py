from dofbot.htmlbuilder.elements.htmlelement import HtmlElement


class Hr(HtmlElement):
    def build(self) -> str:
        return '<hr>'
