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
            raise IndexError("Error")
        else:
            rank: int = self.rank.pop(0)
            sentence: str = self.strings.pop(0)
        return rank, sentence


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
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

    def ingest(self, data: str | list[str]) -> None:
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
                    for key, value in item.items()
                )
                for item in data
            )
        return isinstance(data, dict) and all(
            isinstance((key), (str)) and isinstance((value), (str))
            for key, value in data.items()
        )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise LogProcessorError("Improper log data")
        if isinstance(data, list):
            for value in data:
                self._store(
                    f"{value['log_level'].strip()}"
                    f": {value['log_message'].strip()}"
                )
        else:
            self._store(
                f"{data['log_level'].strip()}"
                f": {data['log_message'].strip()}"
            )


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream:
    def __init__(self) -> None:
        self.procs: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.procs.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            isProc = False
            for proc in self.procs:
                if proc.validate(element):
                    proc.ingest(element)
                    isProc = True
                    break
            if not isProc:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.procs) == 0:
            print("No processor found, no data")
        else:
            for proc in self.procs:
                name = proc.__class__.__name__
                name.replace("Processor", " Processor")
                print(
                    f"{name}: "
                    f"total {proc.count} items processed,"
                    f"remaining {len(proc.strings)} on processor"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.procs:
            data = []
            for i in range(nb):
                try:
                    data.append(proc.output())
                except IndexError:
                    break
            plugin.process_output(data)


class CsvExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print(f"CSV Output: \n{','.join(values)}")


class JsonExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [f'"item_{index}": "{value}"' for index, value in data]
        print(f'JSON Output: \n {{{", ".join(values)}}}')


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    stream.register_processor(np)
    stream.register_processor(tp)
    stream.register_processor(lp)
    dataStream: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil isconnected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {dataStream}\n")
    stream.process_stream(dataStream)
    stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CsvExportPlugin())
    print()
    stream.print_processors_stats()
    dataStream2: list[typing.Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {dataStream2}")
    stream.process_stream(dataStream2)
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JsonExportPlugin())
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
