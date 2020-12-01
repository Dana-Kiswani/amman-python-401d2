from data_structures_and_algorithms.challenges.binary_search.array_binary_search  import binarySearch

def testSearch():
    expected = 2
    received = binarySearch([4,8,15,16,23,42], 15)
    assert expected == received

def testFail():
    expected = -1
    received = binarySearch([11,22,33,44,55,66,77], 90)
    assert expected == received