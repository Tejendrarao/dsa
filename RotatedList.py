def count_rotations(nums):
    position = 1
    if len(nums) == 0 or len(nums) == 1:
        return 0
    else:
        while position < len(nums):
            if nums[position] < nums[position-1]:
                return position
            position += 1 


print(count_rotations([]))