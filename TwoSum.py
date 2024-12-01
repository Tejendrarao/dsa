def sumTwo(nums,target):
    numMap={}
    n = len(nums)
    
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement],i]
        numMap[nums[i]] = i
        print(numMap)
    return []


nums = [3,6,7]#[3,6,1,2,5,6,7]
target = 10
res = sumTwo(nums,target)
print(res)