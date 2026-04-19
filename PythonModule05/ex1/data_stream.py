from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._storage: list[str] = []
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise Exception("No data available")
        rank = self._total - len(self._storage)
        value = self._storage.pop(0)
        return (rank, value)

    def _store(self, value: str) -> None:
        self._storage.append(value)
        self._total += 1

    def get_name(self) -> str:
        return self.__class__.__name__

    def get_total(self) -> int:
        return self._total

    def get_remaining(self) -> int:
        return len(self._storage)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(x, (int, float))
                and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for x in items:
            self._store(str(x))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        items = data if isinstance(data, list) else [data]
        for x in items:
            self._store(x)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def is_log(d: Any) -> bool:
            return isinstance(d, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in d.items()
                )

        if is_log(data):
            return True
        if isinstance(data, list):
            return all(is_log(x) for x in data)
        return False

    def ingest(
        self, data: Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        items = data if isinstance(data, list) else [data]
        for entry in items:
            level = entry.get("log_level", "")
            msg = entry.get("log_message", "")
            self._store(f"{level}: {msg}")


class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False

            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break

            if not handled:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            print(
                f"{proc.get_name()}: total "
                f"{proc.get_total()} items processed, "
                f"remaining {proc.get_remaining()} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    num = NumericProcessor()
    stream.register_processor(num)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    txt = TextProcessor()
    log = LogProcessor()
    stream.register_processor(txt)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        try:
            num.output()
        except Exception:
            pass
    for _ in range(2):
        try:
            txt.output()
        except Exception:
            pass
    try:
        log.output()
    except Exception:
        pass
    stream.print_processors_stats()
