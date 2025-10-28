def twoSum(nums,target):

    num_lkp = dict()
    for i,n in enumerate(nums):
        num_lkp[n] = i

    indices = []
    for i,n in enumerate(nums):
        if target-n in num_lkp.keys():
            if num_lkp[target-n] != i:
                indices.append(i)
                indices.append(num_lkp[target-n])
                break
    
    return indices


nums = [3,3]
target = 6
print(f'output = {twoSum(nums,target)}')
