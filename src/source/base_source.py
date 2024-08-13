from abc import ABC, abstractmethod


class Source(ABC):

    @abstractmethod
    def handler(self, **kwargs):
        pass
