import os
from dev_doctor.checks.base import BaseCheck, CheckResult


class EnvCheck(BaseCheck):
    def run(self) -> CheckResult:
        missing = [v for v in self.config["required"] if v not in os.environ]
        if missing:
            return CheckResult(
                self.name, False, f"Missing env vars: {', '.join(missing)}", self.required
            )
        return CheckResult(self.name, True, "All env vars present", self.required)
