import subprocess
import sys

from tomoscan import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "tomoscan", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
