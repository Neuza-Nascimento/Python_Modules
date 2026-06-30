#!/usr/bin/python3

from abc import ABC, abstractmethod
import typing


class DataProcessorError(Exception):
    def __init__(self, msg: str = "Unknown Processor Error") -> None:
        super().__init__(msg)


class NumericProcessorError(DataProcessorError):
    def __init__(self, msg: str = "Unknown NumericProcessor Error") -> None:
        super().__init__(msg)


class TextProcessorError(DataProcessorError):
    def __init__(self, msg: str = "Unknown TextProcessor Error") -> None:
        super().__init__(msg)


class LogProcessorError(DataProcessorError):
    def __init__(self, msg: str = "Unknown LogProcessor Error") -> None:
        super().__init__(msg)


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def __init__(self) -> None:
        super().__init__()
        self.strings: list[str] = []
        self.rank: list[int] = []
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
            raise NumericProcessorError("Improper numeric data")
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
            raise TextProcessorError("Improper text data")
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
        return isinstance(data, dict) and all(
                isinstance((key), (str)) and isinstance((value), (str))
                for key, value in data.items())

    def ingest(self, data: dict[str, str]
               | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise LogProcessorError("Improper log data")
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
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest('foo')
    except DataProcessorError as e:
        print(f"Got exception: {e}")
    dataNums: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {dataNums}")
    print("Extracting 3 values...")
    np.ingest(dataNums)
    for _ in range(0, 3):
        rank, value = np.output()
        print(f"Numeric value {rank}: {value}")
    print()
    print("Testing Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    dataText: list[str] = ['Hello', 'Nexus', 'Word']
    print(f"Processing data: {dataText}")
    print("Extracting 1 values...")
    tp.ingest(dataText)
    rank, value = tp.output()
    print(f"Text value {rank}: {value}")
    print()
    print("Testing Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    dataLog: list[dict] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {dataLog}")
    print("Extracting 2 values...")
    lp.ingest(dataLog)
    for _ in range(0, 2):
        rank, value = lp.output()
        print(f"Log value {rank}: {value}")


if __name__ == "__main__":
    main()
