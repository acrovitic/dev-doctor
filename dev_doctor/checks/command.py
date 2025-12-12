import subprocess
from dev_doctor.checks.base import BaseCheck, CheckResult


class CommandCheck(BaseCheck):
    def run(self) -> CheckResult:
        proc = subprocess.run(
            self.config["command"],
            shell=True,
            capture_output=True,
            text=True,
        )

        expected = self.config.get("expect", {}).get("contains")
        output = proc.stdout.strip()

        if proc.returncode != 0:
            return CheckResult(self.name, False, proc.stderr.strip(), self.required)

        if expected and expected not in output:
            return CheckResult(
                self.name, False, f"Output did not contain '{expected}'", self.required
            )

        return CheckResult(self.name, True, output, self.required)
