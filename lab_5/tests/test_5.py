import pytest
from utils import flatten_list


@pytest.mark.parametrize(
    "nested_list, expected",
    [
        ([1, 2, 3], [1, 2, 3]),
        ([1, [2, 3], [4, [5]]], [1, 2, 3, 4, 5]),
        ([], []),
        ([[[1]]], [1]),
        ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
    ],
)
def test_flatten_list(nested_list, expected):
    assert flatten_list(nested_list) == expected
