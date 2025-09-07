#!/usr/bin/env python3
"""
Minimal Auto-Grader
Grades maxProfit and twoSum, shows mistakes, stores user score + timestamp
"""

import sys, os, json
from datetime import datetime

def test_two_sum(func):
    cases = [
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2])
    ]
    passed = 0
    for nums, target, expected in cases:
        try:
            if sorted(func(nums, target)) == sorted(expected):
                passed += 1
            else:
                print(f"❌ twoSum failed: {nums}, target={target}, expected={expected}")
        except Exception as e:
            print(f"❌ twoSum error: {e}")
    return passed, len(cases)

def test_max_profit(func):
    cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0)
    ]
    passed = 0
    for prices, expected in cases:
        try:
            if func(prices) == expected:
                passed += 1
            else:
                print(f"❌ maxProfit failed: {prices}, expected={expected}")
        except Exception as e:
            print(f"❌ maxProfit error: {e}")
    return passed, len(cases)

def main():
    sys.path.insert(0, 'my_solutions')
    from solution import twoSum, maxProfit

    ts_passed, ts_total = test_two_sum(twoSum)
    mp_passed, mp_total = test_max_profit(maxProfit)

    total = ts_passed + mp_passed
    out_of = ts_total + mp_total
    pct = (total / out_of) * 100

    print(f"\n📊 SCORE: {total}/{out_of} ({pct:.1f}%)")

    results = {
        "user": os.getenv("GITHUB_ACTOR", "local"),
        "timestamp": datetime.now().isoformat(),
        "score": f"{total}/{out_of}",
        "percentage": pct
    }
    with open("user_score.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()

