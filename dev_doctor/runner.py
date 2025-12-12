from dev_doctor.checks.env import EnvCheck
from dev_doctor.checks.command import CommandCheck
from dev_doctor.checks.filesystem import FilesystemCheck
from dev_doctor.checks.tcp import TCPCheck

CHECK_TYPES = {
    "env": EnvCheck,
    "command": CommandCheck,
    "filesystem": FilesystemCheck,
    "tcp": TCPCheck,
}


def run_checks(check_configs: list):
    results = []

    for cfg in check_configs:
        cls = CHECK_TYPES[cfg["type"]]
        check = cls(cfg["name"], cfg)
        results.append(check.run())

    return results
