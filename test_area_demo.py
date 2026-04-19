"""area_demo.py 的进阶测试示例（带注释）。"""

import math

from area_demo import calc_circle_area, parse_radius


def test_calc_circle_area_basic_value():
    expected = math.pi * 2 * 2
    result = calc_circle_area(2, pi=math.pi)
    assert abs(result - expected) < 1e-12


def test_calc_circle_area_zero():
    assert calc_circle_area(0) == 0


def test_parse_radius_valid_number():
    radius, error = parse_radius("2.5")
    assert radius == 2.5
    assert error is None


def test_parse_radius_empty_input_gives_reason():
    radius, error = parse_radius("   ")
    assert radius is None
    assert "输入为空" in error


def test_parse_radius_invalid_text_gives_reason():
    radius, error = parse_radius("abc")
    assert radius is None
    assert "无法识别" in error


def test_parse_radius_negative_number_gives_reason():
    radius, error = parse_radius("-1")
    assert radius is None
    assert "不能为负数" in error
