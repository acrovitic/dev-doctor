import socket
from dev_doctor.checks.base import BaseCheck, CheckResult


class TCPCheck(BaseCheck):
    def run(self) -> CheckResult:
        host = self.config["host"]
        port = self.config["port"]

        try:
            with socket.create_connection((host, port), timeout=3):
                return CheckResult(
                    self.name, True, f"Connected to {host}:{port}", self.required
                )
        except Exception as e:
            return CheckResult(self.name, False, str(e), self.required)
