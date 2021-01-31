import os
import platform
from subprocess import getoutput


def test_valid_arg() -> None:
    """
    Checks for valid output with correct arg.
    """

    assert getoutput('python3 ./main.py --my_arg foo') == 'foo'



