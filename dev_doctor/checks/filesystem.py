from pathlib import Path
from dev_doctor.checks.base import BaseCheck, CheckResult


class FilesystemCheck(BaseCheck):
    def run(self) -> CheckResult:
        path = Path(self.config["path"])

        if not path.exists():
            return CheckResult(self.name, False, "Path does not exist", self.required)

        if self.config.get("expect", {}).get("non_empty") and not any(path.iterdir()):
            return CheckResult(self.name, False, "Directory is empty", self.required)

        return CheckResult(self.name, True, "Filesystem check passed", self.required)
