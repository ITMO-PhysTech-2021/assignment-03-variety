# noinspection PyPackages
from .module import do_something_stupid as dss1
# noinspection PyPackages
from ..module.module import do_something_stupid as dss2

import inspect
import module


def test_import():
    dss1()
    dss2()


def test_private():
    assert len(inspect.getmembers(module, inspect.isfunction)) == 1
