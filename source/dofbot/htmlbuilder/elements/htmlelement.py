from abc import ABC, abstractmethod


class HtmlElement(ABC):
    @abstractmethod
    def build(self) -> str:
        pass
