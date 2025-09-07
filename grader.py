#!/usr/bin/env python3
"""
Simple Auto-Grader for DS-BTT-test Repository
Grades maxProfit and twoSum functions
"""

import sys
import json
import os
from datetime import datetime

def test_two_sum():
    """Test the twoSum function"""
    try:
        # Import the user's solution
        sys.path.insert(0, 'my_solutions')
        from solution import twoSum
        
        # Test cases
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([2, 5, 5, 11], 10, [1, 2]),
            ([1, 2, 3, 4, 5], 8, [2, 4])
        ]
        
        passed = 0
        total = len(test_cases)
        
        print("🧪 Testing twoSum function...")
        
        for i, (nums, target, expected) in enumerate(test_cases):
            try:
                result = twoSum(nums, target)
                # Check if result is correct (order doesn't matter)
                if sorted(result) == sorted(expected):
                    print(f"  ✅ Test {i+1}: PASSED")
                    passed += 1
                else:
                    print(f"  ❌ Test {i+1}: FAILED - Expected {expected}, got {result}")
            except Exception as e:
                print(f"  ❌ Test {i+1}: ERROR - {e}")
        
        return passed, total
        
    except ImportError:
        print("❌ Could not import twoSum function")
        return 0, 5
    except Exception as e:
        print(f"❌ Error testing twoSum: {e}")
        return 0, 5

def test_max_profit():
    """Test the maxProfit function"""
    try:
        # Import the user's solution
        sys.path.insert(0, 'my_solutions')
        from solution import maxProfit
        
        # Test cases
        test_cases = [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([1, 2, 3, 4, 5], 4),
            ([2, 4, 1], 2),
            ([3, 3, 5, 0, 0, 3, 1, 4], 4)
        ]
        
        passed = 0
        total = len(test_cases)
        
        print("🧪 Testing maxProfit function...")
        
        for i, (prices, expected) in enumerate(test_cases):
            try:
                result = maxProfit(prices)
                if result == expected:
                    print(f"  ✅ Test {i+1}: PASSED")
                    passed += 1
                else:
                    print(f"  ❌ Test {i+1}: FAILED - Expected {expected}, got {result}")
            except Exception as e:
                print(f"  ❌ Test {i+1}: ERROR - {e}")
        
        return passed, total
        
    except ImportError:
        print("❌ Could not import maxProfit function")
        return 0, 5
    except Exception as e:
        print(f"❌ Error testing maxProfit: {e}")
        return 0, 5

def main():
    """Main grading function"""
    print("=" * 60)
    print("🎯 DS-BTT-TEST AUTO-GRADER")
    print("=" * 60)
    print()
    
    # Test both functions
    two_sum_passed, two_sum_total = test_two_sum()
    print()
    max_profit_passed, max_profit_total = test_max_profit()
    
    # Calculate scores
    total_passed = two_sum_passed + max_profit_passed
    total_tests = two_sum_total + max_profit_total
    percentage = (total_passed / total_tests) * 100 if total_tests > 0 else 0
    
    # Show results
    print("\n" + "=" * 60)
    print("📊 GRADING RESULTS")
    print("=" * 60)
    
    print(f"Two Sum:    {two_sum_passed}/{two_sum_total} tests passed")
    print(f"Max Profit: {max_profit_passed}/{max_profit_total} tests passed")
    print()
    print(f"🏆 TOTAL SCORE: {total_passed}/{total_tests} ({percentage:.1f}%)")
    
    # Grade feedback
    if percentage == 100:
        print("🎉 PERFECT SCORE! Excellent work!")
    elif percentage >= 80:
        print("👍 GREAT JOB! Almost there!")
    elif percentage >= 60:
        print("📚 GOOD START! Keep improving!")
    else:
        print("🔄 NEEDS WORK! Review the problems and try again!")
    
    # Save results
    save_results(two_sum_passed, two_sum_total, max_profit_passed, max_profit_total, percentage)
    
    return 0 if percentage >= 70 else 1

def save_results(two_sum_passed, two_sum_total, max_profit_passed, max_profit_total, percentage):
    """Save grading results to files"""
    user = os.getenv('GITHUB_ACTOR', 'local_user')
    timestamp = datetime.now().isoformat()
    
    # Simple text results
    with open('grade_results.txt', 'w') as f:
        f.write(f"User: {user}\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Two Sum: {two_sum_passed}/{two_sum_total}\n")
        f.write(f"Max Profit: {max_profit_passed}/{max_profit_total}\n")
        f.write(f"Total Score: {two_sum_passed + max_profit_passed}/{two_sum_total + max_profit_total} ({percentage:.1f}%)\n")
    
    # JSON for leaderboard
    results = {
        'user': user,
        'timestamp': timestamp,
        'two_sum_score': two_sum_passed,
        'two_sum_total': two_sum_total,
        'max_profit_score': max_profit_passed,
        'max_profit_total': max_profit_total,
        'total_score': two_sum_passed + max_profit_passed,
        'total_possible': two_sum_total + max_profit_total,
        'percentage': percentage
    }
    
    with open('user_score.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Results saved for {user}")

if __name__ == "__main__":
    sys.exit(main())
