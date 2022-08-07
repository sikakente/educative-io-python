import unittest
import pytest
from algorithms.recursion import compute_all_valid_ip_addresses as cav


@pytest.mark.parametrize("input_string,expected", [
    ("19216811", [
        '1.92.168.11',
        '19.2.168.11',
        '19.21.68.11',
        '19.216.8.11',
        '19.216.81.1',
        '192.1.68.11',
        '192.16.8.11',
        '192.16.81.1',
        '192.168.1.1',
    ]),
])
def test_test_compute_all_valid_ip_addresses(input_string, expected):
    assert expected == cav.compute_all_valid_ip_addresses(input_string)


if __name__ == '__main__':
    unittest.main()
