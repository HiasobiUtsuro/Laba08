def kbig(nums, k):     
    Uslovie = 1 
    for i in range(1,len(nums)):
        if Uslovie == k:
            break
        nums.remove(max(nums)) 
        Uslovie = Uslovie + 1
    return max(nums)

print(kbig(nums, k))
