import subprocess
import sys


def run(args):
    return subprocess.run(
        [sys.executable, "-m", "toolkit", *args],
        capture_output=True,
        text=True,
    )


def test_calc():
    r = run(["calc", "2+3"])
    assert r.returncode == 0
    assert r.stdout.strip() == "5.0"

def test_convert():
    r = run(["convert", "1000", "--from", "mm", "--to", "m"])
    assert r.returncode == 0
    assert r.stdout.strip() == "1.0"

def test_error():
    r = run(["calc", "5/0"])
    assert r.returncode == 2