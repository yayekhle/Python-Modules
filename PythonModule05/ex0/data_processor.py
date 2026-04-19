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


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
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
            raise TypeError("Improper text data")
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
            raise TypeError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for entry in items:
            level = entry.get('log_level', '')
            msg = entry.get('log_message', '')
            self._store(f"{level}: {msg}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num = NumericProcessor()
    print(f" Trying to validate input '42': {num.validate(42)}")
    print(f" Trying to validate input 'Hello': {num.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")
    except TypeError as e:
        print(f" Got exception: {e}")
    num.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, val = num.output()
        print(f" Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    txt = TextProcessor()
    print(f" Trying to validate input '42': {txt.validate(42)}")
    txt.ingest(["Hello", "Nexus", "World"])
    print(" Extracting 1 value...")
    rank, val = txt.output()
    print(f" Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    log.ingest([
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ])
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, val = log.output()
        print(f" Log entry {rank}: {val}")
