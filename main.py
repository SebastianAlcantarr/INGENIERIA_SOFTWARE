
def twosum(nums:list[int],target:int):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]==target-nums[i]:
                return [i,j]
        return []
    return None


nums = [2,11,7,10,1]

target = 3

resultado = twosum(nums, target)

print(resultado)



