# put your array_reverse challenge tests here
from data_structures_and_algorithms.challenges.array_reverse.array_reverse import reverse_array

# here's a test to get you started
def test_leave_as_is():
    actual = reverse_array([1, 2, 3, 4])
    expected = [4, 3, 2, 1]
    assert actual == expected
