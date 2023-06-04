from TwoSumProgramm import two_sum
def test_empty_array():
    assert two_sum([],10) is None

def test_no_solution():
    assert two_sum([1,2,3],10) is None

def test_one_solution():
    assert two_sum([2,7,11,15],9)==[0,1]