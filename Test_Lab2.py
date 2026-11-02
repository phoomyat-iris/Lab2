import lab2


def test_find_min_max():
    result = lab2.find_min_max([5, 3, 9, 1, 7])
    assert result == [1, 9]


def test_calc_average():
    assert lab2.calc_average([10, 20, 30]) == 20


def test_calc_median_odd():
    assert lab2.calc_median_temperature([30, 10, 20]) == 20.0


def test_calc_median_even():
    assert lab2.calc_median_temperature([10, 20, 30, 40]) == 25.0