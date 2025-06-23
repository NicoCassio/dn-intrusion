from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, name: str, need_args: bool) -> None:
        self.name = name
        self.need_args = need_args

    @abstractmethod
    def handle(self) -> None:
        pass
