#add your solution here

def maxProfit(prices):
  # TODO add you solution
  print('Hi')
  return 1





def twoSum(nums, target):
    # Dictionary to store number -> index
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    # If no solution found (usually the problem guarantees one solution)
    return []

