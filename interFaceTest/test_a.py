#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest


@pytest.mark.parametrize("test_input,expect", [["3+5", 8], ["2*2", 4]])
# @pytest.mark.skip("阻塞")
@pytest.mark.test
@pytest.mark.api
def test_demo(test_input, expect):
    assert eval(test_input) == expect


@pytest.mark.parametrize("x", [2, 3, 4, 5])
@pytest.mark.parametrize("y", [1, 2, 3, 4])
def test_cartesian_product(x, y):
    print(x, y, x*y)
    assert x*y < 100


if __name__ == "__main__":
    pytest.main(["-s", "test_a.py"])
