import subprocess
import sys
import os


PYTHON_BINARY = sys.executable


def run_with_args(args):
    return subprocess.check_output(
        "{} main.py -p test_main_db.sqlite {}".format(PYTHON_BINARY, args),
        shell=True)


def test_sanity():
    try:
        os.remove('test_main_db.sqlite')
    except FileNotFoundError:
        pass

    assert run_with_args("add_interval 2021-05-03T10:00 2021-05-10T11:15") == b""
    assert run_with_args("get_slots -d 2021-05-03") == b"2021-05-03 10:00:00 - 2021-05-04 00:15:00\r\n"
    assert run_with_args("get_slots -w 2021-05-03") == b"2021-05-03 10:00:00 - 2021-05-10 00:15:00\r\n"
    assert run_with_args("delete_day 2021-05-03") == b""
    assert run_with_args("delete_interval 2021-05-03T10:00 2021-05-08T11:15") == b""
