#!/usr/bin/env python3
"""
grader.py - Automatic grading script for solutions
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path

def run_tests_for_solution(solution_file):
    """Run tests for a specific solution file"""
    print(f"Grading: {solution_file}")
    
    # Import the solution
    spec = importlib.util.spec_from_file_location("solution", solution_file)
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    
    # Run pytest on corresponding test file
    test_file = f"tests/test_{Path(solution_file).stem}.py"
    if os.path.exists(test_file):
        result = subprocess.run([
            sys.executable, "-m", "pytest", test_file, "-v", "--tb=short"
        ], capture_output=True, text=True)
        
        return result.returncode == 0, result.stdout, result.stderr
    else:
        print(f"Warning: No test file found for {solution_file}")
        return None, "", ""

def main():
    """Main grading function"""
    solutions_dir = "my_solutions"
    results = []
    total_score = 0
    total_problems = 0
    
    print("=" * 50)
    print("AUTOMATIC GRADING SYSTEM")
    print("=" * 50)
    
    if not os.path.exists(solutions_dir):
        print(f"Error: {solutions_dir} directory not found!")
        return 1
    
    # Find all Python solution files
    solution_files = list(Path(solutions_dir).glob("*.py"))
    
    if not solution_files:
        print("No solution files found!")
        return 1
    
    # Grade each solution
    for solution_file in solution_files:
        passed, stdout, stderr = run_tests_for_solution(solution_file)
        
        if passed is not None:
            total_problems += 1
            if passed:
                total_score += 1
                status = "✅ PASSED"
            else:
                status = "❌ FAILED"
            
            results.append(f"{solution_file.name}: {status}")
            print(f"{solution_file.name}: {status}")
            
            if stderr:
                print(f"Errors: {stderr}")
    
    # Calculate final grade
    if total_problems > 0:
        percentage = (total_score / total_problems) * 100
        print("\n" + "=" * 50)
        print(f"FINAL GRADE: {total_score}/{total_problems} ({percentage:.1f}%)")
        print("=" * 50)
        
        # Write results to file for GitHub Actions
        with open("grade_results.txt", "w") as f:
            f.write(f"Grade: {total_score}/{total_problems} ({percentage:.1f}%)\n")
            f.write("\nDetailed Results:\n")
            for result in results:
                f.write(f"- {result}\n")
        
        return 0 if percentage >= 70 else 1
    else:
        print("No problems were graded!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
