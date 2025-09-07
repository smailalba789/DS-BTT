# creat virtual enviroment 
# 3python3 -m pip install pytest

import pytest
from my_solutions import solution

def test_maxProfit():
    assert solution.maxProfit([7,1,5,3,6,4]) == 5
    assert solution.maxProfit([7,6,4,3,1]) == 0
    assert solution.maxProfit([2,4,1]) == 2

def test_twoSum():
    result = solution.twoSum([2,7,11,15], 9)
    assert sorted(result) == [0,1]

    result = solution.twoSum([3,2,4], 6)
    assert sorted(result) == [1,2]

    result = solution.twoSum([3,3], 6)
    assert sorted(result) == [0,1]
