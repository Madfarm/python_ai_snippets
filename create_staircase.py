def create_staircase1(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

    print(step)
  return subsets

def create_staircase2(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets


def tester(nums):
    print(f"Input: {nums}")
    print(f"Output1: {create_staircase1(nums)}")
    print(f"Output2: {create_staircase2(nums)}")

tester([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])