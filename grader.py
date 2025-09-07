import pytest
import sys
from pathlib import Path
import json

def run_tests():
    result = pytest.main(["-q", "tests/"])
    return result

if __name__ == "__main__":
    exit_code = run_tests()
    if exit_code == 0:
        print("✅ All tests passed! Score: 2/2")
    else:
        cache = Path(".pytest_cache/v/cache/lastfailed")
        if cache.exists():
            with open(cache) as f:
                failed = len(json.load(f))
        else:
            failed = 0
        passed = 2 - failed
        print(f"❌ Some tests failed. Score: {passed}/2")
    sys.exit(exit_code)
