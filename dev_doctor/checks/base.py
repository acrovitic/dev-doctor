from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CheckResult:
    name: str
    passed: bool
    details: str
    required: bool = True


class BaseCheck(ABC):
    def __init__(self, name: str, config: dict):
        self.name = name
        self.config = config
        self.required = config.get("required", True)

    @abstractmethod
    def run(self) -> CheckResult:
        pass
