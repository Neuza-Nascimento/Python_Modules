from abc import ABC , abstractmethod
import typing

class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def __init__(self) -> None:
        super().__init__()
        self.strings: list = []
        self.rank: list = []
        self.count: int = 0

    def _store(self, string: str) -> None:
        self.strings.append(string)
        self.rank.append(self.count)
        self.count += 1

    def output(self) -> tuple[int, str]:
        if len(self.strings) == 0:
            raise IndexError("error")
        else:
            rank: int = self.rank.pop(0)
            sentence: str = self.strings.pop(0)
        return rank, sentence

class NumericProcessor(DataProcessor):
    
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
           return all(isinstance(item, (int, float)) for item in data)
        return isinstance(data, (int, float))
    
    def ingest(self, data: int | float 
               | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Error")
        if isinstance(data, list):
            for value in data:
                self._store(str(value))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, (str)) for item in data)
        return isinstance(data, (str))
    
    def ingest(self, data: str 
               | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Error")
        if isinstance(data, list):
            for value in data:
                self._store(value)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance((key), (str)) and isinstance((value), (str))
                    for key, value in item.items())
                for item in data)
        return all(isinstance((key), (str)) and isinstance((value), (str))
                    for key, value in data.items())

    def ingest(self, data: dict[str, str] 
               | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Error")
        if isinstance(data, list):
            for value in data:
                self._store(f"{value['log_level'].strip()}" 
                            f": {value['log_message'].strip()}")
        else:
            self._store(f"{data['log_level'].strip()}"
                        f": {data['log_message'].strip()}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    np = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    
    print("")

    pass


if __name__ == "__main__":
    main()
